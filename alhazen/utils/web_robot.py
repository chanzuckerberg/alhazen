# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/36_web_robot.ipynb.

# %% auto 0
__all__ = ['retrieve_pdf_from_doidotorg', 'retrieve_full_text_links_from_biorxiv', 'execute_search_on_biorxiv',
           'get_html_from_pmc_doi', 'clean_and_convert_tags', 'extract_reconstructed_nxml']

# %% ../../nbs/36_web_robot.ipynb 3
from bs4 import BeautifulSoup,Tag,Comment,NavigableString

import requests
from urllib.request import urlopen

import pickle as pkl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from splinter import Browser
from selenium.webdriver.chrome.service import Service
import re
from random import randint
from time import sleep
import requests
import os
from pathlib import Path


# %% ../../nbs/36_web_robot.ipynb 4
def retrieve_pdf_from_doidotorg(doi, base_dir):
    browser = Browser(headless=True)
    doi = doi.replace('https://doi.org/', '').replace('doi', '')
    stem = doi.split('/')[0]
    if os.path.exists(base_dir+'/'+stem) is False:
        os.makedirs(base_dir+'/'+stem)
    hrefs = set()
    try:
        # visit bioRxiv's paper page
        browser.visit('https://doi.org/'+doi)
        sleep(randint(5,10)*0.1)
        for link in browser.find_by_css('a'):
            if link['href'] is not None and 'pdf' in link['href']:
                hrefs.add(link['href'])
                        
    except Exception as e:
        print(e)

    browser.quit()

    link = min(hrefs, key=len) # prints "i"
    response = requests.get(link)
    with open(base_dir+'/'+doi+'.pdf', 'wb') as f:
        f.write(response.content)

#retrieve_pdf_from_doidotorg('10.1083/jcb.202204093', '/Users/gburns/alhazen/em_tech/temp/')

# %% ../../nbs/36_web_robot.ipynb 5
def retrieve_full_text_links_from_biorxiv(doi, base_dir):
    browser = Browser(headless=True)
    doi = doi.replace('https://doi.org/', '').replace('doi', '')
    if doi.startswith('10.1101/') is False:
        print('Not a BioRxiv DOI')
        return None
    if os.path.exists(base_dir+'/10.1101') is False:
        os.makedirs(base_dir+'/10.1101')
    hrefs = []
    try:
        # visit bioRxiv's paper page
        browser.visit('https://www.biorxiv.org/content/'+doi)
        sleep(randint(5,10)*0.1)
        for link in browser.find_by_css('a[class="dropdown-link"]'):
            if link['href']:
                hrefs.append(link['href'])
                        
    except Exception as e:
        print(e)

    browser.quit()

    files = []
    for link in hrefs:
        if link.endswith('.pdf'):
            response = requests.get(link)
            with open(base_dir+'/'+doi+'.pdf', 'wb') as f:
                f.write(response.content)
            files.append(base_dir+'/'+doi+'.pdf')
        elif link.endswith('.xml'):
            response = requests.get(link)
            with open(base_dir+'/'+doi+'.nxml', 'wb') as f:
                f.write(response.content)
            files.append(base_dir+'/'+doi+'.nxml')
    return files
        

# %% ../../nbs/36_web_robot.ipynb 6
def execute_search_on_biorxiv(search_term):
    browser = Browser(headless=True)
    all_dois = []

    try:
        # visit bioRxiv's search page
        browser.visit('https://www.biorxiv.org/search')

        # fill in the search form
        sleep(randint(5,10)*0.1)
        print('fill search term')
        browser.find_by_id('edit-txtsimple').fill(search_term)

        sleep(randint(5,10)*0.1)
        print('scroll to bottom')
        #browser.scroll_to('bottom')
        
        print('click search button')        
        browser.find_by_css('a[class="search-choice-close"]').click()    
        #browser.find_by_css('input[class="form-submit"]').click()    
        browser.find_by_id('edit-actions').find_by_value('Search').click()
        
        sleep(randint(5,10)*0.1)
        print('load next page')
        # Extract the number of results
        formatted_string = browser.find_by_id('page-title').text
        
        # Use regular expressions to get the number from a string formatted 'XXX Results'
        m = re.search(r'\d+ Results', formatted_string)
        if m:
            num_results = int(re.search(r'\d+', formatted_string).group())
            
            loop_count = 0
            while True:
                
                # Extract each result from the list of the web page
                doi_links = browser.find_by_css('span[class="highwire-cite-metadata-doi highwire-cite-metadata"]')
                all_dois.extend([re.sub('doi: ', '', t.text) for t in doi_links])
                #
                # Is next button absent?
                next_button_not_present = browser.is_element_not_present_by_css('a[class="link-icon link-icon-after"]')

                if next_button_not_present:
                    break
            
                # Find the next button on the page
                next_button = browser.find_by_css('a[class="link-icon link-icon-after"]')

                # Click the next button
                next_button.click()
                sleep(randint(5,10)*0.1)
                #print('load page number'+str(loop_count))

                loop_count += 1
                if loop_count > 100:
                    break
            
    except Exception as e:
        print(e)

    browser.quit()
    return all_dois

# %% ../../nbs/36_web_robot.ipynb 7
def get_html_from_pmc_doi(doi, base_file_path):    
    """
    Given a DOI, navigate to the PMC HTML page and reconstruct NXML from that 
    """
    if os.environ.get('NCBI_API_KEY') is None:
        raise Exception('Error attempting to query NCBI for URL data, did you set the NCBI_API_KEY environment variable?')
    api_key = os.environ.get('NCBI_API_KEY')

    esearch_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?api_key='+api_key+'&db=pmc&term='+doi+'[doi]&retmode=xml'
    sleep(0.1)
    print(esearch_url)
    esearch_response = urlopen(esearch_url)
    esearch_data = esearch_response.read().decode('utf-8')
    esearch_soup = BeautifulSoup(esearch_data, "lxml-xml")
    id_tag = esearch_soup.find('Id')    
    if id_tag is None:
      print('No paper found with that DOI')
      return []
    pmc_id = id_tag.string

    # navigate to the PMC HTML page (https://www.ncbi.nlm.nih.gov/pmc/articles/<PMC_ID>/)
    try:
        browser = Browser(headless=True)
        browser.visit('https://www.ncbi.nlm.nih.gov/pmc/articles/'+pmc_id+'/')
        screenshot_path = browser.html_snapshot(base_file_path)
        temp_html = base_file_path + '/' + doi + '.html'
        p = Path(temp_html)
        d = p.parent
        if d.exists is False:
            os.makedirs(d.absolute()) 
        os.rename(screenshot_path, temp_html)
    except Exception as e:
        print(e)
        return []
    finally:
        browser.quit()

    return [screenshot_path]

def clean_and_convert_tags(soup, tag):

    new_tag = soup.new_tag(tag.name)
    
    if( re.match('^h\d', tag.name) ):
        new_tag.name = 'title'
            
    # Add a placeholder tag for this figure but don't fill it in currently
    elif( tag.name == 'div' and 'class' in tag.attrs and 'fig' in tag.attrs['class'] ):
        new_tag = soup.new_tag('fig')
        new_tag.attrs['id'] = tag.attrs['id']
        new_tag.attrs['position'] = 'float'
        return new_tag

    # Treat all other div tags as new 'sec' tags in new version 
    elif( tag.name == 'div' ):
        new_tag.name = 'sec'
    
    # top-level link tag to external reference, strip away tags from within the tag
    elif( tag.name == 'a' and 'class' in tag.attrs and 'bibr' in tag.attrs['class'] ):
        new_tag = soup.new_tag('xref')
        new_tag.attrs['ref-type'] = 'bibr' 
        new_tag.append(NavigableString(tag.string))
        return new_tag

    # top-level link tag to figure / table (<xref rid="fig4" ref-type="fig">)
    elif( tag.name == 'a' and 'class' in tag.attrs and 'fig' in tag.attrs['class'] ):
        new_tag = soup.new_tag('xref')
        new_tag.attrs['ref-type'] = 'fig' 
        new_tag.append(NavigableString(tag.string))
        return new_tag
    
    for c in tag.contents:
        if( type(c) is Tag ):
            new_c = clean_and_convert_tags(soup, c)
            if( new_c is not None ):
                new_tag.append(new_c)
        elif( type(c) is NavigableString ):
            new_tag.append(NavigableString(c))
                
    return new_tag

def extract_reconstructed_nxml(html):
    
    soup = BeautifulSoup(html, "lxml")
    
    title = soup.find('h1', attrs={'class': 'content-title'})  
    pmcid = soup.find('li', attrs={'class': 'accid'})  
    sections = soup.find_all('div', attrs={'class': 'tsec sec'})
    
    if( pmcid is None ):
        return None

    making_soup = BeautifulSoup("<article></article>", "lxml")
    article = making_soup.article
    
    front = making_soup.new_tag("front")
    article.append(front)
    
    meta = making_soup.new_tag('article-meta')
    front.append(meta)
    
    article_id = making_soup.new_tag('article-id')
    meta.append(article_id)
    article_id.append( NavigableString( pmcid.text ) )
    
    title_group = making_soup.new_tag('title-group')
    front.append(title_group)
    
    article_title = making_soup.new_tag('article-title')
    article_title.append(NavigableString(title.text))
    title_group.append(article_title)
       
    for sec in sections:
        for h2 in sec.children:
            if( type(h2) is Tag and h2.name=='h2' and h2.text=='Abstract'):
                abstract = making_soup.new_tag('abstract')
                front.append(abstract)
                for node in h2.next_siblings:
                    if( type(node) is Tag):
                        abstract.append(clean_and_convert_tags(making_soup, node))
    
    body = making_soup.new_tag('body')
    article.append(body)
    for sec in sections:
        for h2 in sec.children:
            sec = making_soup.new_tag('sec')
            if( type(h2) is Tag and h2.name=='h2' 
                    and h2.text!='Abstract'
                    and h2.text!='References'
                    and h2.text!='Footnotes'
                    and h2.text!='Acknowledgments'):
                body.append(sec)
                sec.append(clean_and_convert_tags(making_soup, h2))
                for p in h2.next_siblings:
                    if( type(p) is Tag ):
                        new_tag = clean_and_convert_tags(making_soup, p)
                        if( new_tag is not None ):
                            sec.append(new_tag)
                   
    return making_soup
