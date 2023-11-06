# Auto generated from sciknow.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-11-06T11:13:15
# Schema: czScientificKnowledge
#
# id: https://chanzuckerberg.github.io/alhazen/linkml/sciknow
# description: LinkML Schema for Entities that serves as vehicles that contain scientific knowledge.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
MESH = CurieNamespace('MESH', 'http://id.nlm.nih.gov/mesh/')
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/entity/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/prop/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
CZSK = CurieNamespace('czsk', 'https://chanzuckerberg.github.io/alhazen/linkml/sciknow')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
FABIO = CurieNamespace('fabio', 'http://purl.org/spar/fabio/')
IAO = CurieNamespace('iao', 'http://purl.obolibrary.org/obo/IAO_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CZSK


# Types

# Class references
class EntityId(extended_str):
    pass


class NamedThingId(EntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class ScientificKnowledgeExpressionId(InformationContentEntityId):
    pass


class ScientificPublicationId(ScientificKnowledgeExpressionId):
    pass


class ScientificPrimaryResearchArticleId(ScientificPublicationId):
    pass


class ScientificPrimaryResearchPreprintId(ScientificPublicationId):
    pass


class ScientificReviewArticleId(ScientificPublicationId):
    pass


class ScientificBookId(ScientificPublicationId):
    pass


class ScientificBookChapterId(ScientificPublicationId):
    pass


class ScientificConferenceArticleId(ScientificPublicationId):
    pass


class ScientificDissertationId(ScientificPublicationId):
    pass


class InformationResourceId(InformationContentEntityId):
    pass


class ScientificKnowledgeCollectionId(InformationContentEntityId):
    pass


class ScientificPublicationCollectionId(ScientificKnowledgeCollectionId):
    pass


class ScientificKnowledgeFragmentId(InformationContentEntityId):
    pass


class SelectorId(InformationContentEntityId):
    pass


class OffsetTextSelectorId(SelectorId):
    pass


class PersonId(NamedThingId):
    pass


class AuthorId(PersonId):
    pass


class OrganizationId(NamedThingId):
    pass


class CityId(NamedThingId):
    pass


class CountryId(NamedThingId):
    pass


@dataclass
class Entity(YAMLRoot):
    """
    Root Model class for all things and informational relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.Entity
    class_class_curie: ClassVar[str] = "czsk:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = CZSK.Entity

    id: Union[str, EntityId] = None
    iri: Optional[str] = None
    type: Optional[Union[str, List[str]]] = empty_list()
    type_str: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.iri is not None and not isinstance(self.iri, str):
            self.iri = str(self.iri)

        if not isinstance(self.type, list):
            self.type = [self.type] if self.type is not None else []
        self.type = [v if isinstance(v, str) else str(v) for v in self.type]

        if self.type_str is not None and not isinstance(self.type_str, str):
            self.type_str = str(self.type_str)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(Entity):
    """
    an entity or concept/class described by a name
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.NamedThing
    class_class_curie: ClassVar[str] = "czsk:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = CZSK.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.InformationContentEntity
    class_class_curie: ClassVar[str] = "czsk:InformationContentEntity"
    class_name: ClassVar[str] = "InformationContentEntity"
    class_model_uri: ClassVar[URIRef] = CZSK.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    license: Optional[str] = None
    rights: Optional[str] = None
    format: Optional[str] = None
    creation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        super().__post_init__(**kwargs)


@dataclass
class ScientificKnowledgeExpression(InformationContentEntity):
    """
    Any expression of scientific knowledge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.ScientificKnowledgeExpression
    class_class_curie: ClassVar[str] = "czsk:ScientificKnowledgeExpression"
    class_name: ClassVar[str] = "ScientificKnowledgeExpression"
    class_model_uri: ClassVar[URIRef] = CZSK.ScientificKnowledgeExpression

    id: Union[str, ScientificKnowledgeExpressionId] = None
    has_part: Optional[Union[Union[str, ScientificKnowledgeFragmentId], List[Union[str, ScientificKnowledgeFragmentId]]]] = empty_list()
    authors: Optional[Union[Dict[Union[str, AuthorId], Union[dict, "Author"]], List[Union[dict, "Author"]]]] = empty_dict()
    title: Optional[str] = None
    abstract: Optional[str] = None
    full_text: Optional[str] = None
    publication_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificKnowledgeExpressionId):
            self.id = ScientificKnowledgeExpressionId(self.id)

        if not isinstance(self.has_part, list):
            self.has_part = [self.has_part] if self.has_part is not None else []
        self.has_part = [v if isinstance(v, ScientificKnowledgeFragmentId) else ScientificKnowledgeFragmentId(v) for v in self.has_part]

        self._normalize_inlined_as_list(slot_name="authors", slot_type=Author, key_name="id", keyed=True)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.full_text is not None and not isinstance(self.full_text, str):
            self.full_text = str(self.full_text)

        if self.publication_date is not None and not isinstance(self.publication_date, XSDDate):
            self.publication_date = XSDDate(self.publication_date)

        super().__post_init__(**kwargs)


@dataclass
class ScientificPublication(ScientificKnowledgeExpression):
    """
    A published expression of scientific knowledge,  such as a paper, book, thesis, conference proceedings, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.ScientificPublication
    class_class_curie: ClassVar[str] = "czsk:ScientificPublication"
    class_name: ClassVar[str] = "ScientificPublication"
    class_model_uri: ClassVar[URIRef] = CZSK.ScientificPublication

    id: Union[str, ScientificPublicationId] = None
    doi: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificPublicationId):
            self.id = ScientificPublicationId(self.id)

        if self.doi is not None and not isinstance(self.doi, str):
            self.doi = str(self.doi)

        super().__post_init__(**kwargs)


@dataclass
class ScientificPrimaryResearchArticle(ScientificPublication):
    """
    A scientific publication describing original research typically formatted in an IMRaD structure (introduction,
    methods, resulst, and discussion). These articles will have undergone peer review.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.ScientificPrimaryResearchArticle
    class_class_curie: ClassVar[str] = "czsk:ScientificPrimaryResearchArticle"
    class_name: ClassVar[str] = "ScientificPrimaryResearchArticle"
    class_model_uri: ClassVar[URIRef] = CZSK.ScientificPrimaryResearchArticle

    id: Union[str, ScientificPrimaryResearchArticleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificPrimaryResearchArticleId):
            self.id = ScientificPrimaryResearchArticleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ScientificPrimaryResearchPreprint(ScientificPublication):
    """
    A scientific publication describing original research typically formatted in an IMRaD structure (introduction,
    methods, resulst, and discussion). These articles have been published as preprints and have NOT undergone peer
    review.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.ScientificPrimaryResearchPreprint
    class_class_curie: ClassVar[str] = "czsk:ScientificPrimaryResearchPreprint"
    class_name: ClassVar[str] = "ScientificPrimaryResearchPreprint"
    class_model_uri: ClassVar[URIRef] = CZSK.ScientificPrimaryResearchPreprint

    id: Union[str, ScientificPrimaryResearchPreprintId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificPrimaryResearchPreprintId):
            self.id = ScientificPrimaryResearchPreprintId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ScientificReviewArticle(ScientificPublication):
    """
    A scientific publication describing original research typically formatted in an IMRaD structure (introduction,
    methods, resulst, and discussion).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.ScientificReviewArticle
    class_class_curie: ClassVar[str] = "czsk:ScientificReviewArticle"
    class_name: ClassVar[str] = "ScientificReviewArticle"
    class_model_uri: ClassVar[URIRef] = CZSK.ScientificReviewArticle

    id: Union[str, ScientificReviewArticleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificReviewArticleId):
            self.id = ScientificReviewArticleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ScientificBook(ScientificPublication):
    """
    A scientific publication describing original research typically formatted in an IMRaD structure (introduction,
    methods, resulst, and discussion).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.ScientificBook
    class_class_curie: ClassVar[str] = "czsk:ScientificBook"
    class_name: ClassVar[str] = "ScientificBook"
    class_model_uri: ClassVar[URIRef] = CZSK.ScientificBook

    id: Union[str, ScientificBookId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificBookId):
            self.id = ScientificBookId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ScientificBookChapter(ScientificPublication):
    """
    A scientific publication describing original research typically formatted in an IMRaD structure (introduction,
    methods, resulst, and discussion).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.ScientificBookChapter
    class_class_curie: ClassVar[str] = "czsk:ScientificBookChapter"
    class_name: ClassVar[str] = "ScientificBookChapter"
    class_model_uri: ClassVar[URIRef] = CZSK.ScientificBookChapter

    id: Union[str, ScientificBookChapterId] = None
    part_of: Optional[Union[str, ScientificBookId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificBookChapterId):
            self.id = ScientificBookChapterId(self.id)

        if self.part_of is not None and not isinstance(self.part_of, ScientificBookId):
            self.part_of = ScientificBookId(self.part_of)

        super().__post_init__(**kwargs)


@dataclass
class ScientificConferenceArticle(ScientificPublication):
    """
    A scientific publication describing original research that was presented at a conference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.ScientificConferenceArticle
    class_class_curie: ClassVar[str] = "czsk:ScientificConferenceArticle"
    class_name: ClassVar[str] = "ScientificConferenceArticle"
    class_model_uri: ClassVar[URIRef] = CZSK.ScientificConferenceArticle

    id: Union[str, ScientificConferenceArticleId] = None
    part_of: Optional[Union[str, ScientificBookId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificConferenceArticleId):
            self.id = ScientificConferenceArticleId(self.id)

        if self.part_of is not None and not isinstance(self.part_of, ScientificBookId):
            self.part_of = ScientificBookId(self.part_of)

        super().__post_init__(**kwargs)


@dataclass
class ScientificDissertation(ScientificPublication):
    """
    A thesis or dissertation submitted by a researcher as part of their work to qualify for an advanced degree -
    usually a doctorate.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.ScientificDissertation
    class_class_curie: ClassVar[str] = "czsk:ScientificDissertation"
    class_name: ClassVar[str] = "ScientificDissertation"
    class_model_uri: ClassVar[URIRef] = CZSK.ScientificDissertation

    id: Union[str, ScientificDissertationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificDissertationId):
            self.id = ScientificDissertationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class InformationResource(InformationContentEntity):
    """
    A database or knowledgebase and its supporting ecosystem of interfaces and services that deliver content to
    consumers (e.g. web portals, APIs, query endpoints, streaming services, data downloads, etc.). A single
    Information Resource by this definition may span many different datasets or databases, and include many access
    endpoints and user interfaces. Information Resources include project-specific resources such as a Translator
    Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.InformationResource
    class_class_curie: ClassVar[str] = "czsk:InformationResource"
    class_name: ClassVar[str] = "InformationResource"
    class_model_uri: ClassVar[URIRef] = CZSK.InformationResource

    id: Union[str, InformationResourceId] = None
    name: Optional[str] = None
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationResourceId):
            self.id = InformationResourceId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class ScientificKnowledgeCollection(InformationContentEntity):
    """
    A collection of expressions of scientific knowledge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.ScientificKnowledgeCollection
    class_class_curie: ClassVar[str] = "czsk:ScientificKnowledgeCollection"
    class_name: ClassVar[str] = "ScientificKnowledgeCollection"
    class_model_uri: ClassVar[URIRef] = CZSK.ScientificKnowledgeCollection

    id: Union[str, ScientificKnowledgeCollectionId] = None
    name: Optional[str] = None
    logical_query: Optional[str] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    information_sources: Optional[Union[Union[str, InformationResourceId], List[Union[str, InformationResourceId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificKnowledgeCollectionId):
            self.id = ScientificKnowledgeCollectionId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.logical_query is not None and not isinstance(self.logical_query, str):
            self.logical_query = str(self.logical_query)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if not isinstance(self.information_sources, list):
            self.information_sources = [self.information_sources] if self.information_sources is not None else []
        self.information_sources = [v if isinstance(v, InformationResourceId) else InformationResourceId(v) for v in self.information_sources]

        super().__post_init__(**kwargs)


@dataclass
class ScientificPublicationCollection(ScientificKnowledgeCollection):
    """
    A collection of scientific publications.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.ScientificPublicationCollection
    class_class_curie: ClassVar[str] = "czsk:ScientificPublicationCollection"
    class_name: ClassVar[str] = "ScientificPublicationCollection"
    class_model_uri: ClassVar[URIRef] = CZSK.ScientificPublicationCollection

    id: Union[str, ScientificPublicationCollectionId] = None
    has_part: Optional[Union[Union[str, ScientificPublicationId], List[Union[str, ScientificPublicationId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificPublicationCollectionId):
            self.id = ScientificPublicationCollectionId(self.id)

        if not isinstance(self.has_part, list):
            self.has_part = [self.has_part] if self.has_part is not None else []
        self.has_part = [v if isinstance(v, ScientificPublicationId) else ScientificPublicationId(v) for v in self.has_part]

        super().__post_init__(**kwargs)


@dataclass
class ScientificKnowledgeFragment(InformationContentEntity):
    """
    A selected subportion of the contents of a ScientificKnowledgeExpression, described by an selector.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.ScientificKnowledgeFragment
    class_class_curie: ClassVar[str] = "czsk:ScientificKnowledgeFragment"
    class_name: ClassVar[str] = "ScientificKnowledgeFragment"
    class_model_uri: ClassVar[URIRef] = CZSK.ScientificKnowledgeFragment

    id: Union[str, ScientificKnowledgeFragmentId] = None
    part_of: Optional[Union[str, ScientificKnowledgeExpressionId]] = None
    selector: Optional[Union[str, SelectorId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificKnowledgeFragmentId):
            self.id = ScientificKnowledgeFragmentId(self.id)

        if self.part_of is not None and not isinstance(self.part_of, ScientificKnowledgeExpressionId):
            self.part_of = ScientificKnowledgeExpressionId(self.part_of)

        if self.selector is not None and not isinstance(self.selector, SelectorId):
            self.selector = SelectorId(self.selector)

        super().__post_init__(**kwargs)


@dataclass
class Selector(InformationContentEntity):
    """
    A way of localizing and describing a ScientificKnowledgeFragment within a ScientificKnowledgeExpression.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.Selector
    class_class_curie: ClassVar[str] = "czsk:Selector"
    class_name: ClassVar[str] = "Selector"
    class_model_uri: ClassVar[URIRef] = CZSK.Selector

    id: Union[str, SelectorId] = None

@dataclass
class OffsetTextSelector(Selector):
    """
    A way of localizing and describing a fragment of text within a larger body of text using offsets and lengths.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.OffsetTextSelector
    class_class_curie: ClassVar[str] = "czsk:OffsetTextSelector"
    class_name: ClassVar[str] = "OffsetTextSelector"
    class_model_uri: ClassVar[URIRef] = CZSK.OffsetTextSelector

    id: Union[str, OffsetTextSelectorId] = None
    offset: Optional[int] = None
    length: Optional[int] = None
    text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OffsetTextSelectorId):
            self.id = OffsetTextSelectorId(self.id)

        if self.offset is not None and not isinstance(self.offset, int):
            self.offset = int(self.offset)

        if self.length is not None and not isinstance(self.length, int):
            self.length = int(self.length)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.Person
    class_class_curie: ClassVar[str] = "czsk:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = CZSK.Person

    id: Union[str, PersonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Author(Person):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.Author
    class_class_curie: ClassVar[str] = "czsk:Author"
    class_name: ClassVar[str] = "Author"
    class_model_uri: ClassVar[URIRef] = CZSK.Author

    id: Union[str, AuthorId] = None
    orcid: Optional[str] = None
    affiliations: Optional[Union[Union[str, OrganizationId], List[Union[str, OrganizationId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuthorId):
            self.id = AuthorId(self.id)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        if not isinstance(self.affiliations, list):
            self.affiliations = [self.affiliations] if self.affiliations is not None else []
        self.affiliations = [v if isinstance(v, OrganizationId) else OrganizationId(v) for v in self.affiliations]

        super().__post_init__(**kwargs)


@dataclass
class Organization(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.Organization
    class_class_curie: ClassVar[str] = "czsk:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = CZSK.Organization

    id: Union[str, OrganizationId] = None
    city: Optional[Union[Union[str, CityId], List[Union[str, CityId]]]] = empty_list()
    country: Optional[Union[Union[str, CountryId], List[Union[str, CountryId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        if not isinstance(self.city, list):
            self.city = [self.city] if self.city is not None else []
        self.city = [v if isinstance(v, CityId) else CityId(v) for v in self.city]

        if not isinstance(self.country, list):
            self.country = [self.country] if self.country is not None else []
        self.country = [v if isinstance(v, CountryId) else CountryId(v) for v in self.country]

        super().__post_init__(**kwargs)


@dataclass
class City(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.City
    class_class_curie: ClassVar[str] = "czsk:City"
    class_name: ClassVar[str] = "City"
    class_model_uri: ClassVar[URIRef] = CZSK.City

    id: Union[str, CityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CityId):
            self.id = CityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Country(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.Country
    class_class_curie: ClassVar[str] = "czsk:Country"
    class_name: ClassVar[str] = "Country"
    class_model_uri: ClassVar[URIRef] = CZSK.Country

    id: Union[str, CountryId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CountryId):
            self.id = CountryId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=CZSK.id, name="id", curie=CZSK.curie('id'),
                   model_uri=CZSK.id, domain=Entity, range=Union[str, EntityId])

slots.orcid = Slot(uri=CZSK.orcid, name="orcid", curie=CZSK.curie('orcid'),
                   model_uri=CZSK.orcid, domain=None, range=Optional[str])

slots.iri = Slot(uri=CZSK.iri, name="iri", curie=CZSK.curie('iri'),
                   model_uri=CZSK.iri, domain=None, range=Optional[str])

slots.doi = Slot(uri=CZSK.doi, name="doi", curie=CZSK.curie('doi'),
                   model_uri=CZSK.doi, domain=None, range=Optional[str])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=CZSK.type, domain=Entity, range=Optional[Union[str, List[str]]])

slots.type_str = Slot(uri=CZSK.type_str, name="type_str", curie=CZSK.curie('type_str'),
                   model_uri=CZSK.type_str, domain=Entity, range=Optional[str])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=CZSK.name, domain=Entity, range=Optional[str])

slots.xref = Slot(uri=CZSK.xref, name="xref", curie=CZSK.curie('xref'),
                   model_uri=CZSK.xref, domain=NamedThing, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.license = Slot(uri=CZSK.license, name="license", curie=CZSK.curie('license'),
                   model_uri=CZSK.license, domain=InformationContentEntity, range=Optional[str])

slots.rights = Slot(uri=CZSK.rights, name="rights", curie=CZSK.curie('rights'),
                   model_uri=CZSK.rights, domain=InformationContentEntity, range=Optional[str])

slots.format = Slot(uri=CZSK.format, name="format", curie=CZSK.curie('format'),
                   model_uri=CZSK.format, domain=InformationContentEntity, range=Optional[str])

slots.creation_date = Slot(uri=CZSK.creation_date, name="creation date", curie=CZSK.curie('creation_date'),
                   model_uri=CZSK.creation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.publication_date = Slot(uri=CZSK.publication_date, name="publication date", curie=CZSK.curie('publication_date'),
                   model_uri=CZSK.publication_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.has_part = Slot(uri=CZSK.has_part, name="has part", curie=CZSK.curie('has_part'),
                   model_uri=CZSK.has_part, domain=None, range=Optional[Union[str, ScientificBookChapterId]])

slots.part_of = Slot(uri=CZSK.part_of, name="part of", curie=CZSK.curie('part_of'),
                   model_uri=CZSK.part_of, domain=None, range=Optional[Union[str, ScientificKnowledgeExpressionId]])

slots.logical_query = Slot(uri=CZSK.logical_query, name="logical query", curie=CZSK.curie('logical_query'),
                   model_uri=CZSK.logical_query, domain=ScientificKnowledgeCollection, range=Optional[str])

slots.authors = Slot(uri=CZSK.authors, name="authors", curie=CZSK.curie('authors'),
                   model_uri=CZSK.authors, domain=ScientificKnowledgeExpression, range=Optional[Union[Dict[Union[str, AuthorId], Union[dict, "Author"]], List[Union[dict, "Author"]]]])

slots.title = Slot(uri=CZSK.title, name="title", curie=CZSK.curie('title'),
                   model_uri=CZSK.title, domain=ScientificKnowledgeExpression, range=Optional[str])

slots.abstract = Slot(uri=CZSK.abstract, name="abstract", curie=CZSK.curie('abstract'),
                   model_uri=CZSK.abstract, domain=ScientificKnowledgeExpression, range=Optional[str])

slots.full_text = Slot(uri=CZSK.full_text, name="full text", curie=CZSK.curie('full_text'),
                   model_uri=CZSK.full_text, domain=ScientificKnowledgeExpression, range=Optional[str])

slots.cites = Slot(uri=CZSK.cites, name="cites", curie=CZSK.curie('cites'),
                   model_uri=CZSK.cites, domain=ScientificKnowledgeExpression, range=Optional[Union[Union[str, ScientificKnowledgeExpressionId], List[Union[str, ScientificKnowledgeExpressionId]]]])

slots.information_sources = Slot(uri=CZSK.information_sources, name="information sources", curie=CZSK.curie('information_sources'),
                   model_uri=CZSK.information_sources, domain=ScientificKnowledgeCollection, range=Optional[Union[Union[str, InformationResourceId], List[Union[str, InformationResourceId]]]])

slots.selector = Slot(uri=CZSK.selector, name="selector", curie=CZSK.curie('selector'),
                   model_uri=CZSK.selector, domain=ScientificKnowledgeFragment, range=Optional[Union[str, SelectorId]])

slots.affiliations = Slot(uri=CZSK.affiliations, name="affiliations", curie=CZSK.curie('affiliations'),
                   model_uri=CZSK.affiliations, domain=Author, range=Optional[Union[Union[str, OrganizationId], List[Union[str, OrganizationId]]]])

slots.offsetTextSelector__offset = Slot(uri=CZSK.offset, name="offsetTextSelector__offset", curie=CZSK.curie('offset'),
                   model_uri=CZSK.offsetTextSelector__offset, domain=None, range=Optional[int])

slots.offsetTextSelector__length = Slot(uri=CZSK.length, name="offsetTextSelector__length", curie=CZSK.curie('length'),
                   model_uri=CZSK.offsetTextSelector__length, domain=None, range=Optional[int])

slots.offsetTextSelector__text = Slot(uri=CZSK.text, name="offsetTextSelector__text", curie=CZSK.curie('text'),
                   model_uri=CZSK.offsetTextSelector__text, domain=None, range=Optional[str])

slots.organization__city = Slot(uri=CZSK.city, name="organization__city", curie=CZSK.curie('city'),
                   model_uri=CZSK.organization__city, domain=None, range=Optional[Union[Union[str, CityId], List[Union[str, CityId]]]])

slots.organization__country = Slot(uri=CZSK.country, name="organization__country", curie=CZSK.curie('country'),
                   model_uri=CZSK.organization__country, domain=None, range=Optional[Union[Union[str, CountryId], List[Union[str, CountryId]]]])

slots.ScientificKnowledgeExpression_has_part = Slot(uri=CZSK.has_part, name="ScientificKnowledgeExpression_has part", curie=CZSK.curie('has_part'),
                   model_uri=CZSK.ScientificKnowledgeExpression_has_part, domain=ScientificKnowledgeExpression, range=Optional[Union[Union[str, ScientificKnowledgeFragmentId], List[Union[str, ScientificKnowledgeFragmentId]]]])

slots.ScientificBookChapter_part_of = Slot(uri=CZSK.part_of, name="ScientificBookChapter_part of", curie=CZSK.curie('part_of'),
                   model_uri=CZSK.ScientificBookChapter_part_of, domain=ScientificBookChapter, range=Optional[Union[str, ScientificBookId]])

slots.ScientificConferenceArticle_part_of = Slot(uri=CZSK.part_of, name="ScientificConferenceArticle_part of", curie=CZSK.curie('part_of'),
                   model_uri=CZSK.ScientificConferenceArticle_part_of, domain=ScientificConferenceArticle, range=Optional[Union[str, ScientificBookId]])

slots.ScientificPublicationCollection_has_part = Slot(uri=CZSK.has_part, name="ScientificPublicationCollection_has part", curie=CZSK.curie('has_part'),
                   model_uri=CZSK.ScientificPublicationCollection_has_part, domain=ScientificPublicationCollection, range=Optional[Union[Union[str, ScientificPublicationId], List[Union[str, ScientificPublicationId]]]])

slots.ScientificKnowledgeFragment_part_of = Slot(uri=CZSK.part_of, name="ScientificKnowledgeFragment_part of", curie=CZSK.curie('part_of'),
                   model_uri=CZSK.ScientificKnowledgeFragment_part_of, domain=ScientificKnowledgeFragment, range=Optional[Union[str, ScientificKnowledgeExpressionId]])
