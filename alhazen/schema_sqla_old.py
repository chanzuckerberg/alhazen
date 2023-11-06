
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class Entity(Base):
    """
    Root Model class for all things and informational relationships, real or imagined.
    """
    __tablename__ = 'Entity'

    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    type_rel = relationship( "EntityType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: EntityType(type=x_))
    

    def __repr__(self):
        return f"Entity(id={self.id},iri={self.iri},)"



    


class EntityType(Base):
    """
    
    """
    __tablename__ = 'Entity_type'

    Entity_id = Column(Text(), ForeignKey('Entity.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Entity_type(Entity_id={self.Entity_id},type={self.type},)"



    


class NamedThingXref(Base):
    """
    
    """
    __tablename__ = 'NamedThing_xref'

    NamedThing_id = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"NamedThing_xref(NamedThing_id={self.NamedThing_id},xref={self.xref},)"



    


class NamedThingType(Base):
    """
    
    """
    __tablename__ = 'NamedThing_type'

    NamedThing_id = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"NamedThing_type(NamedThing_id={self.NamedThing_id},type={self.type},)"



    


class InformationContentEntityXref(Base):
    """
    
    """
    __tablename__ = 'InformationContentEntity_xref'

    InformationContentEntity_id = Column(Text(), ForeignKey('InformationContentEntity.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationContentEntity_xref(InformationContentEntity_id={self.InformationContentEntity_id},xref={self.xref},)"



    


class InformationContentEntityType(Base):
    """
    
    """
    __tablename__ = 'InformationContentEntity_type'

    InformationContentEntity_id = Column(Text(), ForeignKey('InformationContentEntity.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationContentEntity_type(InformationContentEntity_id={self.InformationContentEntity_id},type={self.type},)"



    


class ScientificKnowledgeExpressionHasPart(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeExpression_has_part'

    ScientificKnowledgeExpression_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'), primary_key=True)
    has_part_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeExpression_has_part(ScientificKnowledgeExpression_id={self.ScientificKnowledgeExpression_id},has_part_id={self.has_part_id},)"



    


class ScientificKnowledgeExpressionXref(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeExpression_xref'

    ScientificKnowledgeExpression_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeExpression_xref(ScientificKnowledgeExpression_id={self.ScientificKnowledgeExpression_id},xref={self.xref},)"



    


class ScientificKnowledgeExpressionType(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeExpression_type'

    ScientificKnowledgeExpression_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeExpression_type(ScientificKnowledgeExpression_id={self.ScientificKnowledgeExpression_id},type={self.type},)"



    


class ScientificPublicationHasPart(Base):
    """
    
    """
    __tablename__ = 'ScientificPublication_has_part'

    ScientificPublication_id = Column(Text(), ForeignKey('ScientificPublication.id'), primary_key=True)
    has_part_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPublication_has_part(ScientificPublication_id={self.ScientificPublication_id},has_part_id={self.has_part_id},)"



    


class ScientificPublicationXref(Base):
    """
    
    """
    __tablename__ = 'ScientificPublication_xref'

    ScientificPublication_id = Column(Text(), ForeignKey('ScientificPublication.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPublication_xref(ScientificPublication_id={self.ScientificPublication_id},xref={self.xref},)"



    


class ScientificPublicationType(Base):
    """
    
    """
    __tablename__ = 'ScientificPublication_type'

    ScientificPublication_id = Column(Text(), ForeignKey('ScientificPublication.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPublication_type(ScientificPublication_id={self.ScientificPublication_id},type={self.type},)"



    


class ScientificPrimaryResearchArticleHasPart(Base):
    """
    
    """
    __tablename__ = 'ScientificPrimaryResearchArticle_has_part'

    ScientificPrimaryResearchArticle_id = Column(Text(), ForeignKey('ScientificPrimaryResearchArticle.id'), primary_key=True)
    has_part_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPrimaryResearchArticle_has_part(ScientificPrimaryResearchArticle_id={self.ScientificPrimaryResearchArticle_id},has_part_id={self.has_part_id},)"



    


class ScientificPrimaryResearchArticleXref(Base):
    """
    
    """
    __tablename__ = 'ScientificPrimaryResearchArticle_xref'

    ScientificPrimaryResearchArticle_id = Column(Text(), ForeignKey('ScientificPrimaryResearchArticle.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPrimaryResearchArticle_xref(ScientificPrimaryResearchArticle_id={self.ScientificPrimaryResearchArticle_id},xref={self.xref},)"



    


class ScientificPrimaryResearchArticleType(Base):
    """
    
    """
    __tablename__ = 'ScientificPrimaryResearchArticle_type'

    ScientificPrimaryResearchArticle_id = Column(Text(), ForeignKey('ScientificPrimaryResearchArticle.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPrimaryResearchArticle_type(ScientificPrimaryResearchArticle_id={self.ScientificPrimaryResearchArticle_id},type={self.type},)"



    


class ScientificPrimaryResearchPreprintHasPart(Base):
    """
    
    """
    __tablename__ = 'ScientificPrimaryResearchPreprint_has_part'

    ScientificPrimaryResearchPreprint_id = Column(Text(), ForeignKey('ScientificPrimaryResearchPreprint.id'), primary_key=True)
    has_part_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPrimaryResearchPreprint_has_part(ScientificPrimaryResearchPreprint_id={self.ScientificPrimaryResearchPreprint_id},has_part_id={self.has_part_id},)"



    


class ScientificPrimaryResearchPreprintXref(Base):
    """
    
    """
    __tablename__ = 'ScientificPrimaryResearchPreprint_xref'

    ScientificPrimaryResearchPreprint_id = Column(Text(), ForeignKey('ScientificPrimaryResearchPreprint.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPrimaryResearchPreprint_xref(ScientificPrimaryResearchPreprint_id={self.ScientificPrimaryResearchPreprint_id},xref={self.xref},)"



    


class ScientificPrimaryResearchPreprintType(Base):
    """
    
    """
    __tablename__ = 'ScientificPrimaryResearchPreprint_type'

    ScientificPrimaryResearchPreprint_id = Column(Text(), ForeignKey('ScientificPrimaryResearchPreprint.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPrimaryResearchPreprint_type(ScientificPrimaryResearchPreprint_id={self.ScientificPrimaryResearchPreprint_id},type={self.type},)"



    


class ScientificReviewArticleHasPart(Base):
    """
    
    """
    __tablename__ = 'ScientificReviewArticle_has_part'

    ScientificReviewArticle_id = Column(Text(), ForeignKey('ScientificReviewArticle.id'), primary_key=True)
    has_part_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificReviewArticle_has_part(ScientificReviewArticle_id={self.ScientificReviewArticle_id},has_part_id={self.has_part_id},)"



    


class ScientificReviewArticleXref(Base):
    """
    
    """
    __tablename__ = 'ScientificReviewArticle_xref'

    ScientificReviewArticle_id = Column(Text(), ForeignKey('ScientificReviewArticle.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificReviewArticle_xref(ScientificReviewArticle_id={self.ScientificReviewArticle_id},xref={self.xref},)"



    


class ScientificReviewArticleType(Base):
    """
    
    """
    __tablename__ = 'ScientificReviewArticle_type'

    ScientificReviewArticle_id = Column(Text(), ForeignKey('ScientificReviewArticle.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificReviewArticle_type(ScientificReviewArticle_id={self.ScientificReviewArticle_id},type={self.type},)"



    


class ScientificBookHasPart(Base):
    """
    
    """
    __tablename__ = 'ScientificBook_has_part'

    ScientificBook_id = Column(Text(), ForeignKey('ScientificBook.id'), primary_key=True)
    has_part_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificBook_has_part(ScientificBook_id={self.ScientificBook_id},has_part_id={self.has_part_id},)"



    


class ScientificBookXref(Base):
    """
    
    """
    __tablename__ = 'ScientificBook_xref'

    ScientificBook_id = Column(Text(), ForeignKey('ScientificBook.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificBook_xref(ScientificBook_id={self.ScientificBook_id},xref={self.xref},)"



    


class ScientificBookType(Base):
    """
    
    """
    __tablename__ = 'ScientificBook_type'

    ScientificBook_id = Column(Text(), ForeignKey('ScientificBook.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificBook_type(ScientificBook_id={self.ScientificBook_id},type={self.type},)"



    


class ScientificBookChapterHasPart(Base):
    """
    
    """
    __tablename__ = 'ScientificBookChapter_has_part'

    ScientificBookChapter_id = Column(Text(), ForeignKey('ScientificBookChapter.id'), primary_key=True)
    has_part_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificBookChapter_has_part(ScientificBookChapter_id={self.ScientificBookChapter_id},has_part_id={self.has_part_id},)"



    


class ScientificBookChapterXref(Base):
    """
    
    """
    __tablename__ = 'ScientificBookChapter_xref'

    ScientificBookChapter_id = Column(Text(), ForeignKey('ScientificBookChapter.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificBookChapter_xref(ScientificBookChapter_id={self.ScientificBookChapter_id},xref={self.xref},)"



    


class ScientificBookChapterType(Base):
    """
    
    """
    __tablename__ = 'ScientificBookChapter_type'

    ScientificBookChapter_id = Column(Text(), ForeignKey('ScientificBookChapter.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificBookChapter_type(ScientificBookChapter_id={self.ScientificBookChapter_id},type={self.type},)"



    


class ScientificConferenceArticleHasPart(Base):
    """
    
    """
    __tablename__ = 'ScientificConferenceArticle_has_part'

    ScientificConferenceArticle_id = Column(Text(), ForeignKey('ScientificConferenceArticle.id'), primary_key=True)
    has_part_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificConferenceArticle_has_part(ScientificConferenceArticle_id={self.ScientificConferenceArticle_id},has_part_id={self.has_part_id},)"



    


class ScientificConferenceArticleXref(Base):
    """
    
    """
    __tablename__ = 'ScientificConferenceArticle_xref'

    ScientificConferenceArticle_id = Column(Text(), ForeignKey('ScientificConferenceArticle.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificConferenceArticle_xref(ScientificConferenceArticle_id={self.ScientificConferenceArticle_id},xref={self.xref},)"



    


class ScientificConferenceArticleType(Base):
    """
    
    """
    __tablename__ = 'ScientificConferenceArticle_type'

    ScientificConferenceArticle_id = Column(Text(), ForeignKey('ScientificConferenceArticle.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificConferenceArticle_type(ScientificConferenceArticle_id={self.ScientificConferenceArticle_id},type={self.type},)"



    


class ScientificDissertationHasPart(Base):
    """
    
    """
    __tablename__ = 'ScientificDissertation_has_part'

    ScientificDissertation_id = Column(Text(), ForeignKey('ScientificDissertation.id'), primary_key=True)
    has_part_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificDissertation_has_part(ScientificDissertation_id={self.ScientificDissertation_id},has_part_id={self.has_part_id},)"



    


class ScientificDissertationXref(Base):
    """
    
    """
    __tablename__ = 'ScientificDissertation_xref'

    ScientificDissertation_id = Column(Text(), ForeignKey('ScientificDissertation.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificDissertation_xref(ScientificDissertation_id={self.ScientificDissertation_id},xref={self.xref},)"



    


class ScientificDissertationType(Base):
    """
    
    """
    __tablename__ = 'ScientificDissertation_type'

    ScientificDissertation_id = Column(Text(), ForeignKey('ScientificDissertation.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificDissertation_type(ScientificDissertation_id={self.ScientificDissertation_id},type={self.type},)"



    


class InformationResourceXref(Base):
    """
    
    """
    __tablename__ = 'InformationResource_xref'

    InformationResource_id = Column(Text(), ForeignKey('InformationResource.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationResource_xref(InformationResource_id={self.InformationResource_id},xref={self.xref},)"



    


class InformationResourceType(Base):
    """
    
    """
    __tablename__ = 'InformationResource_type'

    InformationResource_id = Column(Text(), ForeignKey('InformationResource.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationResource_type(InformationResource_id={self.InformationResource_id},type={self.type},)"



    


class ScientificKnowledgeCollectionInformationSources(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeCollection_information_sources'

    ScientificKnowledgeCollection_id = Column(Text(), ForeignKey('ScientificKnowledgeCollection.id'), primary_key=True)
    information_sources_id = Column(Text(), ForeignKey('InformationResource.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeCollection_information_sources(ScientificKnowledgeCollection_id={self.ScientificKnowledgeCollection_id},information_sources_id={self.information_sources_id},)"



    


class ScientificKnowledgeCollectionXref(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeCollection_xref'

    ScientificKnowledgeCollection_id = Column(Text(), ForeignKey('ScientificKnowledgeCollection.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeCollection_xref(ScientificKnowledgeCollection_id={self.ScientificKnowledgeCollection_id},xref={self.xref},)"



    


class ScientificKnowledgeCollectionType(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeCollection_type'

    ScientificKnowledgeCollection_id = Column(Text(), ForeignKey('ScientificKnowledgeCollection.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeCollection_type(ScientificKnowledgeCollection_id={self.ScientificKnowledgeCollection_id},type={self.type},)"



    


class ScientificPublicationCollectionHasPart(Base):
    """
    
    """
    __tablename__ = 'ScientificPublicationCollection_has_part'

    ScientificPublicationCollection_id = Column(Text(), ForeignKey('ScientificPublicationCollection.id'), primary_key=True)
    has_part_id = Column(Text(), ForeignKey('ScientificPublication.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPublicationCollection_has_part(ScientificPublicationCollection_id={self.ScientificPublicationCollection_id},has_part_id={self.has_part_id},)"



    


class ScientificPublicationCollectionInformationSources(Base):
    """
    
    """
    __tablename__ = 'ScientificPublicationCollection_information_sources'

    ScientificPublicationCollection_id = Column(Text(), ForeignKey('ScientificPublicationCollection.id'), primary_key=True)
    information_sources_id = Column(Text(), ForeignKey('InformationResource.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPublicationCollection_information_sources(ScientificPublicationCollection_id={self.ScientificPublicationCollection_id},information_sources_id={self.information_sources_id},)"



    


class ScientificPublicationCollectionXref(Base):
    """
    
    """
    __tablename__ = 'ScientificPublicationCollection_xref'

    ScientificPublicationCollection_id = Column(Text(), ForeignKey('ScientificPublicationCollection.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPublicationCollection_xref(ScientificPublicationCollection_id={self.ScientificPublicationCollection_id},xref={self.xref},)"



    


class ScientificPublicationCollectionType(Base):
    """
    
    """
    __tablename__ = 'ScientificPublicationCollection_type'

    ScientificPublicationCollection_id = Column(Text(), ForeignKey('ScientificPublicationCollection.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPublicationCollection_type(ScientificPublicationCollection_id={self.ScientificPublicationCollection_id},type={self.type},)"



    


class ScientificKnowledgeFragmentXref(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeFragment_xref'

    ScientificKnowledgeFragment_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeFragment_xref(ScientificKnowledgeFragment_id={self.ScientificKnowledgeFragment_id},xref={self.xref},)"



    


class ScientificKnowledgeFragmentType(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeFragment_type'

    ScientificKnowledgeFragment_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeFragment_type(ScientificKnowledgeFragment_id={self.ScientificKnowledgeFragment_id},type={self.type},)"



    


class SelectorXref(Base):
    """
    
    """
    __tablename__ = 'Selector_xref'

    Selector_id = Column(Text(), ForeignKey('Selector.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Selector_xref(Selector_id={self.Selector_id},xref={self.xref},)"



    


class SelectorType(Base):
    """
    
    """
    __tablename__ = 'Selector_type'

    Selector_id = Column(Text(), ForeignKey('Selector.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Selector_type(Selector_id={self.Selector_id},type={self.type},)"



    


class OffsetTextSelectorXref(Base):
    """
    
    """
    __tablename__ = 'OffsetTextSelector_xref'

    OffsetTextSelector_id = Column(Text(), ForeignKey('OffsetTextSelector.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"OffsetTextSelector_xref(OffsetTextSelector_id={self.OffsetTextSelector_id},xref={self.xref},)"



    


class OffsetTextSelectorType(Base):
    """
    
    """
    __tablename__ = 'OffsetTextSelector_type'

    OffsetTextSelector_id = Column(Text(), ForeignKey('OffsetTextSelector.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"OffsetTextSelector_type(OffsetTextSelector_id={self.OffsetTextSelector_id},type={self.type},)"



    


class PersonXref(Base):
    """
    
    """
    __tablename__ = 'Person_xref'

    Person_id = Column(Text(), ForeignKey('Person.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Person_xref(Person_id={self.Person_id},xref={self.xref},)"



    


class PersonType(Base):
    """
    
    """
    __tablename__ = 'Person_type'

    Person_id = Column(Text(), ForeignKey('Person.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Person_type(Person_id={self.Person_id},type={self.type},)"



    


class AuthorAffiliations(Base):
    """
    
    """
    __tablename__ = 'Author_affiliations'

    Author_id = Column(Text(), ForeignKey('Author.id'), primary_key=True)
    affiliations_id = Column(Text(), ForeignKey('Organization.id'), primary_key=True)
    

    def __repr__(self):
        return f"Author_affiliations(Author_id={self.Author_id},affiliations_id={self.affiliations_id},)"



    


class AuthorXref(Base):
    """
    
    """
    __tablename__ = 'Author_xref'

    Author_id = Column(Text(), ForeignKey('Author.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Author_xref(Author_id={self.Author_id},xref={self.xref},)"



    


class AuthorType(Base):
    """
    
    """
    __tablename__ = 'Author_type'

    Author_id = Column(Text(), ForeignKey('Author.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Author_type(Author_id={self.Author_id},type={self.type},)"



    


class OrganizationCity(Base):
    """
    
    """
    __tablename__ = 'Organization_city'

    Organization_id = Column(Text(), ForeignKey('Organization.id'), primary_key=True)
    city_id = Column(Text(), ForeignKey('City.id'), primary_key=True)
    

    def __repr__(self):
        return f"Organization_city(Organization_id={self.Organization_id},city_id={self.city_id},)"



    


class OrganizationCountry(Base):
    """
    
    """
    __tablename__ = 'Organization_country'

    Organization_id = Column(Text(), ForeignKey('Organization.id'), primary_key=True)
    country_id = Column(Text(), ForeignKey('Country.id'), primary_key=True)
    

    def __repr__(self):
        return f"Organization_country(Organization_id={self.Organization_id},country_id={self.country_id},)"



    


class OrganizationXref(Base):
    """
    
    """
    __tablename__ = 'Organization_xref'

    Organization_id = Column(Text(), ForeignKey('Organization.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Organization_xref(Organization_id={self.Organization_id},xref={self.xref},)"



    


class OrganizationType(Base):
    """
    
    """
    __tablename__ = 'Organization_type'

    Organization_id = Column(Text(), ForeignKey('Organization.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Organization_type(Organization_id={self.Organization_id},type={self.type},)"



    


class CityXref(Base):
    """
    
    """
    __tablename__ = 'City_xref'

    City_id = Column(Text(), ForeignKey('City.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"City_xref(City_id={self.City_id},xref={self.xref},)"



    


class CityType(Base):
    """
    
    """
    __tablename__ = 'City_type'

    City_id = Column(Text(), ForeignKey('City.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"City_type(City_id={self.City_id},type={self.type},)"



    


class CountryXref(Base):
    """
    
    """
    __tablename__ = 'Country_xref'

    Country_id = Column(Text(), ForeignKey('Country.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Country_xref(Country_id={self.Country_id},xref={self.xref},)"



    


class CountryType(Base):
    """
    
    """
    __tablename__ = 'Country_type'

    Country_id = Column(Text(), ForeignKey('Country.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Country_type(Country_id={self.Country_id},type={self.type},)"



    


class NamedThing(Entity):
    """
    an entity or concept/class described by a name
    """
    __tablename__ = 'NamedThing'

    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    xref_rel = relationship( "NamedThingXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: NamedThingXref(xref=x_))
    
    
    type_rel = relationship( "NamedThingType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: NamedThingType(type=x_))
    

    def __repr__(self):
        return f"NamedThing(name={self.name},id={self.id},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    __tablename__ = 'InformationContentEntity'

    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    xref_rel = relationship( "InformationContentEntityXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: InformationContentEntityXref(xref=x_))
    
    
    type_rel = relationship( "InformationContentEntityType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: InformationContentEntityType(type=x_))
    

    def __repr__(self):
        return f"InformationContentEntity(license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},id={self.id},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Person(NamedThing):
    """
    
    """
    __tablename__ = 'Person'

    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    xref_rel = relationship( "PersonXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: PersonXref(xref=x_))
    
    
    type_rel = relationship( "PersonType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: PersonType(type=x_))
    

    def __repr__(self):
        return f"Person(name={self.name},id={self.id},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Organization(NamedThing):
    """
    
    """
    __tablename__ = 'Organization'

    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    # ManyToMany
    city = relationship( "City", secondary="Organization_city")
    
    
    # ManyToMany
    country = relationship( "Country", secondary="Organization_country")
    
    
    xref_rel = relationship( "OrganizationXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: OrganizationXref(xref=x_))
    
    
    type_rel = relationship( "OrganizationType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: OrganizationType(type=x_))
    

    def __repr__(self):
        return f"Organization(name={self.name},id={self.id},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class City(NamedThing):
    """
    
    """
    __tablename__ = 'City'

    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    xref_rel = relationship( "CityXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: CityXref(xref=x_))
    
    
    type_rel = relationship( "CityType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: CityType(type=x_))
    

    def __repr__(self):
        return f"City(name={self.name},id={self.id},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Country(NamedThing):
    """
    
    """
    __tablename__ = 'Country'

    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    xref_rel = relationship( "CountryXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: CountryXref(xref=x_))
    
    
    type_rel = relationship( "CountryType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: CountryType(type=x_))
    

    def __repr__(self):
        return f"Country(name={self.name},id={self.id},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ScientificKnowledgeExpression(InformationContentEntity):
    """
    Any expression of scientific knowledge.   
    """
    __tablename__ = 'ScientificKnowledgeExpression'

    id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text())
    abstract = Column(Text())
    full_text = Column(Text())
    publication_date = Column(Date())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    iri = Column(Text())
    
    
    # ManyToMany
    has_part = relationship( "ScientificKnowledgeFragment", secondary="ScientificKnowledgeExpression_has_part")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ScientificKnowledgeExpression', source_slot='authors', mapping_type=None, target_class='Author', target_slot='ScientificKnowledgeExpression_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.ScientificKnowledgeExpression_id]")
    
    
    xref_rel = relationship( "ScientificKnowledgeExpressionXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificKnowledgeExpressionXref(xref=x_))
    
    
    type_rel = relationship( "ScientificKnowledgeExpressionType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificKnowledgeExpressionType(type=x_))
    

    def __repr__(self):
        return f"ScientificKnowledgeExpression(id={self.id},title={self.title},abstract={self.abstract},full_text={self.full_text},publication_date={self.publication_date},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InformationResource(InformationContentEntity):
    """
    A database or knowledgebase and its supporting ecosystem of interfaces  and services that deliver content to consumers (e.g. web portals, APIs,  query endpoints, streaming services, data downloads, etc.). A single Information Resource by this definition may span many different datasets or databases, and include many access endpoints and user interfaces. Information Resources include project-specific resources such as a Translator Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb.
    """
    __tablename__ = 'InformationResource'

    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    iri = Column(Text())
    
    
    xref_rel = relationship( "InformationResourceXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: InformationResourceXref(xref=x_))
    
    
    type_rel = relationship( "InformationResourceType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: InformationResourceType(type=x_))
    

    def __repr__(self):
        return f"InformationResource(id={self.id},name={self.name},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ScientificKnowledgeCollection(InformationContentEntity):
    """
    A collection of expressions of scientific knowledge.
    """
    __tablename__ = 'ScientificKnowledgeCollection'

    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    logical_query = Column(Text())
    creation_date = Column(Date())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    iri = Column(Text())
    
    
    # ManyToMany
    information_sources = relationship( "InformationResource", secondary="ScientificKnowledgeCollection_information_sources")
    
    
    xref_rel = relationship( "ScientificKnowledgeCollectionXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificKnowledgeCollectionXref(xref=x_))
    
    
    type_rel = relationship( "ScientificKnowledgeCollectionType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificKnowledgeCollectionType(type=x_))
    

    def __repr__(self):
        return f"ScientificKnowledgeCollection(id={self.id},name={self.name},logical_query={self.logical_query},creation_date={self.creation_date},license={self.license},rights={self.rights},format={self.format},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ScientificKnowledgeFragment(InformationContentEntity):
    """
    A selected subportion of the contents of a ScientificKnowledgeExpression, described by an selector.
    """
    __tablename__ = 'ScientificKnowledgeFragment'

    part_of = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'))
    selector = Column(Text(), ForeignKey('Selector.id'))
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    xref_rel = relationship( "ScientificKnowledgeFragmentXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificKnowledgeFragmentXref(xref=x_))
    
    
    type_rel = relationship( "ScientificKnowledgeFragmentType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificKnowledgeFragmentType(type=x_))
    

    def __repr__(self):
        return f"ScientificKnowledgeFragment(part_of={self.part_of},selector={self.selector},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},id={self.id},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Selector(InformationContentEntity):
    """
    A way of localizing and describing a ScientificKnowledgeFragment within a ScientificKnowledgeExpression.
    """
    __tablename__ = 'Selector'

    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    xref_rel = relationship( "SelectorXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: SelectorXref(xref=x_))
    
    
    type_rel = relationship( "SelectorType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: SelectorType(type=x_))
    

    def __repr__(self):
        return f"Selector(license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},id={self.id},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Author(Person):
    """
    
    """
    __tablename__ = 'Author'

    orcid = Column(Text())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    ScientificKnowledgeExpression_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'))
    ScientificPublication_id = Column(Text(), ForeignKey('ScientificPublication.id'))
    ScientificPrimaryResearchArticle_id = Column(Text(), ForeignKey('ScientificPrimaryResearchArticle.id'))
    ScientificPrimaryResearchPreprint_id = Column(Text(), ForeignKey('ScientificPrimaryResearchPreprint.id'))
    ScientificReviewArticle_id = Column(Text(), ForeignKey('ScientificReviewArticle.id'))
    ScientificBook_id = Column(Text(), ForeignKey('ScientificBook.id'))
    ScientificBookChapter_id = Column(Text(), ForeignKey('ScientificBookChapter.id'))
    ScientificConferenceArticle_id = Column(Text(), ForeignKey('ScientificConferenceArticle.id'))
    ScientificDissertation_id = Column(Text(), ForeignKey('ScientificDissertation.id'))
    
    
    # ManyToMany
    affiliations = relationship( "Organization", secondary="Author_affiliations")
    
    
    xref_rel = relationship( "AuthorXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: AuthorXref(xref=x_))
    
    
    type_rel = relationship( "AuthorType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: AuthorType(type=x_))
    

    def __repr__(self):
        return f"Author(orcid={self.orcid},name={self.name},id={self.id},iri={self.iri},ScientificKnowledgeExpression_id={self.ScientificKnowledgeExpression_id},ScientificPublication_id={self.ScientificPublication_id},ScientificPrimaryResearchArticle_id={self.ScientificPrimaryResearchArticle_id},ScientificPrimaryResearchPreprint_id={self.ScientificPrimaryResearchPreprint_id},ScientificReviewArticle_id={self.ScientificReviewArticle_id},ScientificBook_id={self.ScientificBook_id},ScientificBookChapter_id={self.ScientificBookChapter_id},ScientificConferenceArticle_id={self.ScientificConferenceArticle_id},ScientificDissertation_id={self.ScientificDissertation_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ScientificPublication(ScientificKnowledgeExpression):
    """
    A published expression of scientific knowledge,  such as a paper, book, thesis, conference proceedings, etc.   
    """
    __tablename__ = 'ScientificPublication'

    doi = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text())
    abstract = Column(Text())
    full_text = Column(Text())
    publication_date = Column(Date())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    iri = Column(Text())
       
    # ManyToMany
    has_part = relationship( "ScientificKnowledgeFragment", secondary="ScientificPublication_has_part")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ScientificPublication', source_slot='authors', mapping_type=None, target_class='Author', target_slot='ScientificPublication_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.ScientificPublication_id]")
    
    
    xref_rel = relationship( "ScientificPublicationXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificPublicationXref(xref=x_))
    
    
    type_rel = relationship( "ScientificPublicationType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificPublicationType(type=x_))
    

    def __repr__(self):
        return f"ScientificPublication(doi={self.doi},id={self.id},title={self.title},abstract={self.abstract},full_text={self.full_text},publication_date={self.publication_date},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'ScientificPublication',
        "polymorphic_on": pub_type,
        'concrete': True
    }
    


class ScientificPublicationCollection(ScientificKnowledgeCollection):
    """
    A collection of scientific publications.
    """
    __tablename__ = 'ScientificPublicationCollection'

    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    logical_query = Column(Text())
    creation_date = Column(Date())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    iri = Column(Text())
    
    
    # ManyToMany
    has_part = relationship( "ScientificPublication", secondary="ScientificPublicationCollection_has_part")
    
    
    # ManyToMany
    information_sources = relationship( "InformationResource", secondary="ScientificPublicationCollection_information_sources")
    
    
    xref_rel = relationship( "ScientificPublicationCollectionXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificPublicationCollectionXref(xref=x_))
    
    
    type_rel = relationship( "ScientificPublicationCollectionType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificPublicationCollectionType(type=x_))
    

    def __repr__(self):
        return f"ScientificPublicationCollection(id={self.id},name={self.name},logical_query={self.logical_query},creation_date={self.creation_date},license={self.license},rights={self.rights},format={self.format},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class OffsetTextSelector(Selector):
    """
    A way of localizing and describing a fragment of text within a larger body of text using offsets and lengths.
    """
    __tablename__ = 'OffsetTextSelector'

    offset = Column(Integer())
    length = Column(Integer())
    text = Column(Text())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    xref_rel = relationship( "OffsetTextSelectorXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: OffsetTextSelectorXref(xref=x_))
    
    
    type_rel = relationship( "OffsetTextSelectorType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: OffsetTextSelectorType(type=x_))
    

    def __repr__(self):
        return f"OffsetTextSelector(offset={self.offset},length={self.length},text={self.text},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},id={self.id},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ScientificPrimaryResearchArticle(ScientificPublication):
    """
    A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion). These articles will have undergone  peer review. 
    """
    __tablename__ = 'ScientificPrimaryResearchArticle'

    doi = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text())
    abstract = Column(Text())
    full_text = Column(Text())
    publication_date = Column(Date())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    iri = Column(Text())
    
    
    # ManyToMany
    has_part = relationship( "ScientificKnowledgeFragment", secondary="ScientificPrimaryResearchArticle_has_part")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ScientificPrimaryResearchArticle', source_slot='authors', mapping_type=None, target_class='Author', target_slot='ScientificPrimaryResearchArticle_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.ScientificPrimaryResearchArticle_id]")
    
    
    xref_rel = relationship( "ScientificPrimaryResearchArticleXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificPrimaryResearchArticleXref(xref=x_))
    
    
    type_rel = relationship( "ScientificPrimaryResearchArticleType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificPrimaryResearchArticleType(type=x_))
    

    def __repr__(self):
        return f"ScientificPrimaryResearchArticle(doi={self.doi},id={self.id},title={self.title},abstract={self.abstract},full_text={self.full_text},publication_date={self.publication_date},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},iri={self.iri},)"

    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'ScientificPrimaryResearchArticle',
        'concrete': True
    }



class ScientificPrimaryResearchPreprint(ScientificPublication):
    """
    A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion). These articles have been published as preprints and have NOT undergone peer review. 
    """
    __tablename__ = 'ScientificPrimaryResearchPreprint'

    doi = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text())
    abstract = Column(Text())
    full_text = Column(Text())
    publication_date = Column(Date())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    iri = Column(Text())
    
    
    # ManyToMany
    has_part = relationship( "ScientificKnowledgeFragment", secondary="ScientificPrimaryResearchPreprint_has_part")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ScientificPrimaryResearchPreprint', source_slot='authors', mapping_type=None, target_class='Author', target_slot='ScientificPrimaryResearchPreprint_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.ScientificPrimaryResearchPreprint_id]")
    
    
    xref_rel = relationship( "ScientificPrimaryResearchPreprintXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificPrimaryResearchPreprintXref(xref=x_))
    
    
    type_rel = relationship( "ScientificPrimaryResearchPreprintType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificPrimaryResearchPreprintType(type=x_))
    

    def __repr__(self):
        return f"ScientificPrimaryResearchPreprint(doi={self.doi},id={self.id},title={self.title},abstract={self.abstract},full_text={self.full_text},publication_date={self.publication_date},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'ScientificPrimaryResearchPreprint',
        'concrete': True
    }
    


class ScientificReviewArticle(ScientificPublication):
    """
    A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion).   
    """
    __tablename__ = 'ScientificReviewArticle'

    doi = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text())
    abstract = Column(Text())
    full_text = Column(Text())
    publication_date = Column(Date())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    iri = Column(Text())
    
    
    # ManyToMany
    has_part = relationship( "ScientificKnowledgeFragment", secondary="ScientificReviewArticle_has_part")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ScientificReviewArticle', source_slot='authors', mapping_type=None, target_class='Author', target_slot='ScientificReviewArticle_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.ScientificReviewArticle_id]")
    
    
    xref_rel = relationship( "ScientificReviewArticleXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificReviewArticleXref(xref=x_))
    
    
    type_rel = relationship( "ScientificReviewArticleType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificReviewArticleType(type=x_))
    

    def __repr__(self):
        return f"ScientificReviewArticle(doi={self.doi},id={self.id},title={self.title},abstract={self.abstract},full_text={self.full_text},publication_date={self.publication_date},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'ScientificReviewArticle',
        'concrete': True
    }
    


class ScientificBook(ScientificPublication):
    """
    A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion).   
    """
    __tablename__ = 'ScientificBook'

    doi = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text())
    abstract = Column(Text())
    full_text = Column(Text())
    publication_date = Column(Date())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    iri = Column(Text())
    
    
    # ManyToMany
    has_part = relationship( "ScientificKnowledgeFragment", secondary="ScientificBook_has_part")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ScientificBook', source_slot='authors', mapping_type=None, target_class='Author', target_slot='ScientificBook_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.ScientificBook_id]")
    
    
    xref_rel = relationship( "ScientificBookXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificBookXref(xref=x_))
    
    
    type_rel = relationship( "ScientificBookType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificBookType(type=x_))
    

    def __repr__(self):
        return f"ScientificBook(doi={self.doi},id={self.id},title={self.title},abstract={self.abstract},full_text={self.full_text},publication_date={self.publication_date},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'ScientificBook',
        'concrete': True
    }
    


class ScientificBookChapter(ScientificPublication):
    """
    A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion).   
    """
    __tablename__ = 'ScientificBookChapter'

    part_of = Column(Text(), ForeignKey('ScientificBook.id'))
    doi = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text())
    abstract = Column(Text())
    full_text = Column(Text())
    publication_date = Column(Date())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    iri = Column(Text())
    
    
    # ManyToMany
    has_part = relationship( "ScientificKnowledgeFragment", secondary="ScientificBookChapter_has_part")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ScientificBookChapter', source_slot='authors', mapping_type=None, target_class='Author', target_slot='ScientificBookChapter_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.ScientificBookChapter_id]")
    
    
    xref_rel = relationship( "ScientificBookChapterXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificBookChapterXref(xref=x_))
    
    
    type_rel = relationship( "ScientificBookChapterType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificBookChapterType(type=x_))
    

    def __repr__(self):
        return f"ScientificBookChapter(part_of={self.part_of},doi={self.doi},id={self.id},title={self.title},abstract={self.abstract},full_text={self.full_text},publication_date={self.publication_date},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'ScientificBookChapter',
        'concrete': True
    }
    


class ScientificConferenceArticle(ScientificPublication):
    """
    A scientific publication describing original research that was presented at a conference.   
    """
    __tablename__ = 'ScientificConferenceArticle'

    part_of = Column(Text(), ForeignKey('ScientificBook.id'))
    doi = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text())
    abstract = Column(Text())
    full_text = Column(Text())
    publication_date = Column(Date())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    iri = Column(Text())
    
    
    # ManyToMany
    has_part = relationship( "ScientificKnowledgeFragment", secondary="ScientificConferenceArticle_has_part")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ScientificConferenceArticle', source_slot='authors', mapping_type=None, target_class='Author', target_slot='ScientificConferenceArticle_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.ScientificConferenceArticle_id]")
    
    
    xref_rel = relationship( "ScientificConferenceArticleXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificConferenceArticleXref(xref=x_))
    
    
    type_rel = relationship( "ScientificConferenceArticleType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificConferenceArticleType(type=x_))
    

    def __repr__(self):
        return f"ScientificConferenceArticle(part_of={self.part_of},doi={self.doi},id={self.id},title={self.title},abstract={self.abstract},full_text={self.full_text},publication_date={self.publication_date},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'ScientificConferenceArticle',
        'concrete': True
    }
    
class ScientificDissertation(ScientificPublication):
    """
    A thesis or dissertation submitted by a researcher as  part of their work to qualify for an advanced degree - usually a  doctorate.   
    """
    __tablename__ = 'ScientificDissertation'

    doi = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text())
    abstract = Column(Text())
    full_text = Column(Text())
    publication_date = Column(Date())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    iri = Column(Text())
    
    
    # ManyToMany
    has_part = relationship( "ScientificKnowledgeFragment", secondary="ScientificDissertation_has_part")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ScientificDissertation', source_slot='authors', mapping_type=None, target_class='Author', target_slot='ScientificDissertation_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.ScientificDissertation_id]")
    
    
    xref_rel = relationship( "ScientificDissertationXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificDissertationXref(xref=x_))
    
    
    type_rel = relationship( "ScientificDissertationType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificDissertationType(type=x_))
    

    def __repr__(self):
        return f"ScientificDissertation(doi={self.doi},id={self.id},title={self.title},abstract={self.abstract},full_text={self.full_text},publication_date={self.publication_date},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'ScientificDissertation',
        'concrete': True
    }
    


