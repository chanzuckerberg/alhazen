# Auto generated from sciknow_dev.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-11-07T11:01:38
# Schema: czScientificKnowledge
#
# id: https://chanzuckerberg.github.io/alhazen/linkml/sciknow
# description: LinkML Schema for scientific knowledge.
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


class NoteId(InformationContentEntityId):
    pass


class NameValuePairId(InformationContentEntityId):
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
    provenance: Optional[Union[Union[str, NoteId], List[Union[str, NoteId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if not isinstance(self.provenance, list):
            self.provenance = [self.provenance] if self.provenance is not None else []
        self.provenance = [v if isinstance(v, NoteId) else NoteId(v) for v in self.provenance]

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
    type_str: Optional[Union[str, "ScientificPublicationType"]] = None
    part_of: Optional[Union[Union[str, ScientificPublicationCollectionId], List[Union[str, ScientificPublicationCollectionId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificPublicationId):
            self.id = ScientificPublicationId(self.id)

        if self.doi is not None and not isinstance(self.doi, str):
            self.doi = str(self.doi)

        if self.type_str is not None and not isinstance(self.type_str, ScientificPublicationType):
            self.type_str = ScientificPublicationType(self.type_str)

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, ScientificPublicationCollectionId) else ScientificPublicationCollectionId(v) for v in self.part_of]

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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OffsetTextSelectorId):
            self.id = OffsetTextSelectorId(self.id)

        if self.offset is not None and not isinstance(self.offset, int):
            self.offset = int(self.offset)

        if self.length is not None and not isinstance(self.length, int):
            self.length = int(self.length)

        super().__post_init__(**kwargs)


@dataclass
class Note(InformationContentEntity):
    """
    A structured piece of information with an author that is about another InformationContentEntity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.Note
    class_class_curie: ClassVar[str] = "czsk:Note"
    class_name: ClassVar[str] = "Note"
    class_model_uri: ClassVar[URIRef] = CZSK.Note

    id: Union[str, NoteId] = None
    is_about: Optional[Union[Union[str, EntityId], List[Union[str, EntityId]]]] = empty_list()
    authors: Optional[Union[Dict[Union[str, AuthorId], Union[dict, "Author"]], List[Union[dict, "Author"]]]] = empty_dict()
    format: Optional[str] = None
    type_str: Optional[Union[str, "NoteType"]] = None
    structured_content: Optional[Union[Union[str, NameValuePairId], List[Union[str, NameValuePairId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoteId):
            self.id = NoteId(self.id)

        if not isinstance(self.is_about, list):
            self.is_about = [self.is_about] if self.is_about is not None else []
        self.is_about = [v if isinstance(v, EntityId) else EntityId(v) for v in self.is_about]

        self._normalize_inlined_as_list(slot_name="authors", slot_type=Author, key_name="id", keyed=True)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.type_str is not None and not isinstance(self.type_str, NoteType):
            self.type_str = NoteType(self.type_str)

        if not isinstance(self.structured_content, list):
            self.structured_content = [self.structured_content] if self.structured_content is not None else []
        self.structured_content = [v if isinstance(v, NameValuePairId) else NameValuePairId(v) for v in self.structured_content]

        super().__post_init__(**kwargs)


@dataclass
class NameValuePair(InformationContentEntity):
    """
    A single map {string :- string} to track structured data in a note.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CZSK.NameValuePair
    class_class_curie: ClassVar[str] = "czsk:NameValuePair"
    class_name: ClassVar[str] = "NameValuePair"
    class_model_uri: ClassVar[URIRef] = CZSK.NameValuePair

    id: Union[str, NameValuePairId] = None
    variable: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NameValuePairId):
            self.id = NameValuePairId(self.id)

        if self.variable is not None and not isinstance(self.variable, str):
            self.variable = str(self.variable)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

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
class ScientificPublicationType(EnumDefinitionImpl):

    ScientificPrimaryResearchArticle = PermissibleValue(
        text="ScientificPrimaryResearchArticle",
        description="""A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, results, and discussion). These articles will have undergone  peer review.""")
    ScientificPrimaryResearchPreprint = PermissibleValue(
        text="ScientificPrimaryResearchPreprint",
        description="""A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion). These articles have been published as preprints and have NOT undergone peer review.""")
    ScientificReviewArticle = PermissibleValue(
        text="ScientificReviewArticle",
        description="""A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion).""")
    ScientificBook = PermissibleValue(
        text="ScientificBook",
        description="""A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion).""")
    ScientificBookChapter = PermissibleValue(
        text="ScientificBookChapter",
        description="""A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion).""")
    ScientificConferenceArticle = PermissibleValue(
        text="ScientificConferenceArticle",
        description="A scientific publication describing original research that was presented at a conference.")
    ScientificDissertation = PermissibleValue(
        text="ScientificDissertation",
        description="""A thesis or dissertation submitted by a researcher as  part of their work to qualify for an advanced degree - usually a  doctorate.""")

    _defn = EnumDefinition(
        name="ScientificPublicationType",
    )

class NoteType(EnumDefinitionImpl):

    NoteAboutProvenance = PermissibleValue(
        text="NoteAboutProvenance",
        description="""A note that describes the provenance of an InformationContentEntity by describing its source, when it was created and any other salient details written in natural language.""")
    NoteAboutPublication = PermissibleValue(
        text="NoteAboutPublication",
        description="A structured note about an ScientificPublication.")
    NoteAboutFragment = PermissibleValue(
        text="NoteAboutFragment",
        description="A structured note about an ScientificKnowledgeFragment.")

    _defn = EnumDefinition(
        name="NoteType",
    )

# Slots
class slots:
    pass

slots.abstract = Slot(uri=CZSK.abstract, name="abstract", curie=CZSK.curie('abstract'),
                   model_uri=CZSK.abstract, domain=ScientificKnowledgeExpression, range=Optional[str])

slots.affiliations = Slot(uri=CZSK.affiliations, name="affiliations", curie=CZSK.curie('affiliations'),
                   model_uri=CZSK.affiliations, domain=Author, range=Optional[Union[Union[str, OrganizationId], List[Union[str, OrganizationId]]]])

slots.authors = Slot(uri=CZSK.authors, name="authors", curie=CZSK.curie('authors'),
                   model_uri=CZSK.authors, domain=ScientificKnowledgeExpression, range=Optional[Union[Dict[Union[str, AuthorId], Union[dict, "Author"]], List[Union[dict, "Author"]]]])

slots.cites = Slot(uri=CZSK.cites, name="cites", curie=CZSK.curie('cites'),
                   model_uri=CZSK.cites, domain=ScientificKnowledgeExpression, range=Optional[Union[Union[str, ScientificKnowledgeExpressionId], List[Union[str, ScientificKnowledgeExpressionId]]]])

slots.content = Slot(uri=CZSK.content, name="content", curie=CZSK.curie('content'),
                   model_uri=CZSK.content, domain=InformationContentEntity, range=Optional[str])

slots.creation_date = Slot(uri=CZSK.creation_date, name="creation date", curie=CZSK.curie('creation_date'),
                   model_uri=CZSK.creation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.doi = Slot(uri=CZSK.doi, name="doi", curie=CZSK.curie('doi'),
                   model_uri=CZSK.doi, domain=None, range=Optional[str])

slots.format = Slot(uri=CZSK.format, name="format", curie=CZSK.curie('format'),
                   model_uri=CZSK.format, domain=InformationContentEntity, range=Optional[str])

slots.has_part = Slot(uri=CZSK.has_part, name="has part", curie=CZSK.curie('has_part'),
                   model_uri=CZSK.has_part, domain=None, range=Optional[Union[str, ScientificKnowledgeFragmentId]])

slots.has_notes = Slot(uri=CZSK.has_notes, name="has notes", curie=CZSK.curie('has_notes'),
                   model_uri=CZSK.has_notes, domain=Entity, range=Optional[Union[str, InformationContentEntityId]])

slots.id = Slot(uri=CZSK.id, name="id", curie=CZSK.curie('id'),
                   model_uri=CZSK.id, domain=Entity, range=Union[str, EntityId])

slots.iri = Slot(uri=CZSK.iri, name="iri", curie=CZSK.curie('iri'),
                   model_uri=CZSK.iri, domain=None, range=Optional[str])

slots.is_about = Slot(uri=CZSK.is_about, name="is about", curie=CZSK.curie('is_about'),
                   model_uri=CZSK.is_about, domain=InformationContentEntity, range=Optional[Union[Union[str, EntityId], List[Union[str, EntityId]]]])

slots.license = Slot(uri=CZSK.license, name="license", curie=CZSK.curie('license'),
                   model_uri=CZSK.license, domain=InformationContentEntity, range=Optional[str])

slots.logical_query = Slot(uri=CZSK.logical_query, name="logical query", curie=CZSK.curie('logical_query'),
                   model_uri=CZSK.logical_query, domain=ScientificKnowledgeCollection, range=Optional[str])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=CZSK.name, domain=Entity, range=Optional[str])

slots.orcid = Slot(uri=CZSK.orcid, name="orcid", curie=CZSK.curie('orcid'),
                   model_uri=CZSK.orcid, domain=None, range=Optional[str])

slots.part_of = Slot(uri=CZSK.part_of, name="part of", curie=CZSK.curie('part_of'),
                   model_uri=CZSK.part_of, domain=None, range=Optional[Union[str, ScientificKnowledgeExpressionId]])

slots.provenance = Slot(uri=CZSK.provenance, name="provenance", curie=CZSK.curie('provenance'),
                   model_uri=CZSK.provenance, domain=InformationContentEntity, range=Optional[Union[Union[str, NoteId], List[Union[str, NoteId]]]])

slots.publication_date = Slot(uri=CZSK.publication_date, name="publication date", curie=CZSK.curie('publication_date'),
                   model_uri=CZSK.publication_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.rights = Slot(uri=CZSK.rights, name="rights", curie=CZSK.curie('rights'),
                   model_uri=CZSK.rights, domain=InformationContentEntity, range=Optional[str])

slots.structured_content = Slot(uri=CZSK.structured_content, name="structured_content", curie=CZSK.curie('structured_content'),
                   model_uri=CZSK.structured_content, domain=Note, range=Optional[Union[Union[str, NameValuePairId], List[Union[str, NameValuePairId]]]])

slots.title = Slot(uri=CZSK.title, name="title", curie=CZSK.curie('title'),
                   model_uri=CZSK.title, domain=ScientificKnowledgeExpression, range=Optional[str])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=CZSK.type, domain=Entity, range=Optional[Union[str, List[str]]])

slots.type_str = Slot(uri=CZSK.type_str, name="type_str", curie=CZSK.curie('type_str'),
                   model_uri=CZSK.type_str, domain=Entity, range=Optional[str])

slots.xref = Slot(uri=CZSK.xref, name="xref", curie=CZSK.curie('xref'),
                   model_uri=CZSK.xref, domain=NamedThing, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.information_sources = Slot(uri=CZSK.information_sources, name="information sources", curie=CZSK.curie('information_sources'),
                   model_uri=CZSK.information_sources, domain=Note, range=Optional[Union[Union[str, InformationResourceId], List[Union[str, InformationResourceId]]]])

slots.selector = Slot(uri=CZSK.selector, name="selector", curie=CZSK.curie('selector'),
                   model_uri=CZSK.selector, domain=ScientificKnowledgeFragment, range=Optional[Union[str, SelectorId]])

slots.variable = Slot(uri=CZSK.variable, name="variable", curie=CZSK.curie('variable'),
                   model_uri=CZSK.variable, domain=NameValuePair, range=Optional[str])

slots.value = Slot(uri=CZSK.value, name="value", curie=CZSK.curie('value'),
                   model_uri=CZSK.value, domain=NameValuePair, range=Optional[str])

slots.offsetTextSelector__offset = Slot(uri=CZSK.offset, name="offsetTextSelector__offset", curie=CZSK.curie('offset'),
                   model_uri=CZSK.offsetTextSelector__offset, domain=None, range=Optional[int])

slots.offsetTextSelector__length = Slot(uri=CZSK.length, name="offsetTextSelector__length", curie=CZSK.curie('length'),
                   model_uri=CZSK.offsetTextSelector__length, domain=None, range=Optional[int])

slots.organization__city = Slot(uri=CZSK.city, name="organization__city", curie=CZSK.curie('city'),
                   model_uri=CZSK.organization__city, domain=None, range=Optional[Union[Union[str, CityId], List[Union[str, CityId]]]])

slots.organization__country = Slot(uri=CZSK.country, name="organization__country", curie=CZSK.curie('country'),
                   model_uri=CZSK.organization__country, domain=None, range=Optional[Union[Union[str, CountryId], List[Union[str, CountryId]]]])

slots.ScientificKnowledgeExpression_has_part = Slot(uri=CZSK.has_part, name="ScientificKnowledgeExpression_has part", curie=CZSK.curie('has_part'),
                   model_uri=CZSK.ScientificKnowledgeExpression_has_part, domain=ScientificKnowledgeExpression, range=Optional[Union[Union[str, ScientificKnowledgeFragmentId], List[Union[str, ScientificKnowledgeFragmentId]]]])

slots.ScientificPublication_type_str = Slot(uri=CZSK.type_str, name="ScientificPublication_type_str", curie=CZSK.curie('type_str'),
                   model_uri=CZSK.ScientificPublication_type_str, domain=ScientificPublication, range=Optional[Union[str, "ScientificPublicationType"]])

slots.ScientificPublication_part_of = Slot(uri=CZSK.part_of, name="ScientificPublication_part of", curie=CZSK.curie('part_of'),
                   model_uri=CZSK.ScientificPublication_part_of, domain=ScientificPublication, range=Optional[Union[Union[str, ScientificPublicationCollectionId], List[Union[str, ScientificPublicationCollectionId]]]])

slots.ScientificPublicationCollection_has_part = Slot(uri=CZSK.has_part, name="ScientificPublicationCollection_has part", curie=CZSK.curie('has_part'),
                   model_uri=CZSK.ScientificPublicationCollection_has_part, domain=ScientificPublicationCollection, range=Optional[Union[Union[str, ScientificPublicationId], List[Union[str, ScientificPublicationId]]]])

slots.ScientificKnowledgeFragment_part_of = Slot(uri=CZSK.part_of, name="ScientificKnowledgeFragment_part of", curie=CZSK.curie('part_of'),
                   model_uri=CZSK.ScientificKnowledgeFragment_part_of, domain=ScientificKnowledgeFragment, range=Optional[Union[str, ScientificKnowledgeExpressionId]])

slots.Note_type_str = Slot(uri=CZSK.type_str, name="Note_type_str", curie=CZSK.curie('type_str'),
                   model_uri=CZSK.Note_type_str, domain=Note, range=Optional[Union[str, "NoteType"]])
