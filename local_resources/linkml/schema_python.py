# Auto generated from sciknow.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-04-29T23:43:20
# Schema: ScientificKnowledgeExpressionModel
#
# id: https://chanzuckerberg.github.io/alhazen/linkml/sciknow
# description: LinkML Schema for scientific knowledge collections, expressions, items, and fragments.
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
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/entity/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/prop/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://doi.org/')
EPMCID = CurieNamespace('epmcid', 'https://europepmc.org/articles/')
FABIO = CurieNamespace('fabio', 'http://purl.org/spar/fabio/')
IAO = CurieNamespace('iao', 'http://purl.obolibrary.org/obo/IAO_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
ORCID = CurieNamespace('orcid', 'https://orcid.org/')
PMCID = CurieNamespace('pmcid', 'https://www.ncbi.nlm.nih.gov/pmc/articles/')
PMID = CurieNamespace('pmid', 'https://www.ncbi.nlm.nih.gov/pubmed/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKEM = CurieNamespace('skem', 'https://chanzuckerberg.github.io/alhazen/linkml/sciknow')
UMLS = CurieNamespace('umls', 'http://purl.bioontology.org/ontology/UMLS/')
DEFAULT_ = SKEM


# Types

# Class references
class EntityId(extended_str):
    pass


class NamedThingId(EntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class UserQuestionId(InformationContentEntityId):
    pass


class InformationResourceId(InformationContentEntityId):
    pass


class ScientificKnowledgeCollectionId(InformationContentEntityId):
    pass


class ScientificKnowledgeExpressionId(InformationContentEntityId):
    pass


class ScientificKnowledgeItemId(InformationContentEntityId):
    pass


class ScientificKnowledgeFragmentId(InformationContentEntityId):
    pass


class NoteId(InformationContentEntityId):
    pass


class AuthorId(InformationContentEntityId):
    pass


class OrganizationId(InformationContentEntityId):
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

    class_class_uri: ClassVar[URIRef] = SKEM["Entity"]
    class_class_curie: ClassVar[str] = "skem:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = SKEM.Entity

    id: Union[str, EntityId] = None
    type: str = None
    iri: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.iri, list):
            self.iri = [self.iri] if self.iri is not None else []
        self.iri = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.iri]

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(Entity):
    """
    an entity or concept/class described by a name
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKEM["NamedThing"]
    class_class_curie: ClassVar[str] = "skem:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = SKEM.NamedThing

    id: Union[str, NamedThingId] = None
    type: str = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntity(NamedThing):
    """
    A piece of information that is represented in the typically describes some topic of discourse or is used as
    support.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKEM["InformationContentEntity"]
    class_class_curie: ClassVar[str] = "skem:InformationContentEntity"
    class_name: ClassVar[str] = "InformationContentEntity"
    class_model_uri: ClassVar[URIRef] = SKEM.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    type: str = None
    creation_date: Optional[Union[str, XSDDate]] = None
    content: Optional[str] = None
    token_count: Optional[int] = None
    format: Optional[str] = None
    provenance: Optional[str] = None
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    license: Optional[str] = None
    has_notes: Optional[Union[Union[str, NoteId], List[Union[str, NoteId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        if self.token_count is not None and not isinstance(self.token_count, int):
            self.token_count = int(self.token_count)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.provenance is not None and not isinstance(self.provenance, str):
            self.provenance = str(self.provenance)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if not isinstance(self.has_notes, list):
            self.has_notes = [self.has_notes] if self.has_notes is not None else []
        self.has_notes = [v if isinstance(v, NoteId) else NoteId(v) for v in self.has_notes]

        super().__post_init__(**kwargs)


@dataclass
class UserQuestion(InformationContentEntity):
    """
    A question, inquiry, or instruction from an user of the Alhazen system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKEM["UserQuestion"]
    class_class_curie: ClassVar[str] = "skem:UserQuestion"
    class_name: ClassVar[str] = "UserQuestion"
    class_model_uri: ClassVar[URIRef] = SKEM.UserQuestion

    id: Union[str, UserQuestionId] = None
    type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UserQuestionId):
            self.id = UserQuestionId(self.id)

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

    class_class_uri: ClassVar[URIRef] = SKEM["InformationResource"]
    class_class_curie: ClassVar[str] = "skem:InformationResource"
    class_name: ClassVar[str] = "InformationResource"
    class_model_uri: ClassVar[URIRef] = SKEM.InformationResource

    id: Union[str, InformationResourceId] = None
    type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationResourceId):
            self.id = InformationResourceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ScientificKnowledgeCollection(InformationContentEntity):
    """
    A collection of expressions of scientific knowledge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKEM["ScientificKnowledgeCollection"]
    class_class_curie: ClassVar[str] = "skem:ScientificKnowledgeCollection"
    class_name: ClassVar[str] = "ScientificKnowledgeCollection"
    class_model_uri: ClassVar[URIRef] = SKEM.ScientificKnowledgeCollection

    id: Union[str, ScientificKnowledgeCollectionId] = None
    type: str = None
    has_members: Optional[Union[Union[str, ScientificKnowledgeExpressionId], List[Union[str, ScientificKnowledgeExpressionId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificKnowledgeCollectionId):
            self.id = ScientificKnowledgeCollectionId(self.id)

        if not isinstance(self.has_members, list):
            self.has_members = [self.has_members] if self.has_members is not None else []
        self.has_members = [v if isinstance(v, ScientificKnowledgeExpressionId) else ScientificKnowledgeExpressionId(v) for v in self.has_members]

        super().__post_init__(**kwargs)


@dataclass
class ScientificKnowledgeExpression(InformationContentEntity):
    """
    Any expression of scientific knowledge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKEM["ScientificKnowledgeExpression"]
    class_class_curie: ClassVar[str] = "skem:ScientificKnowledgeExpression"
    class_name: ClassVar[str] = "ScientificKnowledgeExpression"
    class_model_uri: ClassVar[URIRef] = SKEM.ScientificKnowledgeExpression

    id: Union[str, ScientificKnowledgeExpressionId] = None
    type: str = None
    has_representation: Optional[Union[Union[str, ScientificKnowledgeItemId], List[Union[str, ScientificKnowledgeItemId]]]] = empty_list()
    member_of: Optional[Union[Union[str, ScientificKnowledgeCollectionId], List[Union[str, ScientificKnowledgeCollectionId]]]] = empty_list()
    has_authors: Optional[Union[Union[str, AuthorId], List[Union[str, AuthorId]]]] = empty_list()
    publication_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificKnowledgeExpressionId):
            self.id = ScientificKnowledgeExpressionId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.has_representation, list):
            self.has_representation = [self.has_representation] if self.has_representation is not None else []
        self.has_representation = [v if isinstance(v, ScientificKnowledgeItemId) else ScientificKnowledgeItemId(v) for v in self.has_representation]

        if not isinstance(self.member_of, list):
            self.member_of = [self.member_of] if self.member_of is not None else []
        self.member_of = [v if isinstance(v, ScientificKnowledgeCollectionId) else ScientificKnowledgeCollectionId(v) for v in self.member_of]

        if not isinstance(self.has_authors, list):
            self.has_authors = [self.has_authors] if self.has_authors is not None else []
        self.has_authors = [v if isinstance(v, AuthorId) else AuthorId(v) for v in self.has_authors]

        if self.publication_date is not None and not isinstance(self.publication_date, XSDDate):
            self.publication_date = XSDDate(self.publication_date)

        super().__post_init__(**kwargs)


@dataclass
class ScientificKnowledgeItem(InformationContentEntity):
    """
    A specific instance of a ScientificKnowledgeExpression:- our internal representation of an EPMC citation record, a
    local copy of a full-text article. This is the substrate that forms the basis for a ScientificKnowledgeFragment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKEM["ScientificKnowledgeItem"]
    class_class_curie: ClassVar[str] = "skem:ScientificKnowledgeItem"
    class_name: ClassVar[str] = "ScientificKnowledgeItem"
    class_model_uri: ClassVar[URIRef] = SKEM.ScientificKnowledgeItem

    id: Union[str, ScientificKnowledgeItemId] = None
    type: str = None
    representation_of: Optional[Union[str, ScientificKnowledgeExpressionId]] = None
    has_part: Optional[Union[Union[str, ScientificKnowledgeFragmentId], List[Union[str, ScientificKnowledgeFragmentId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificKnowledgeItemId):
            self.id = ScientificKnowledgeItemId(self.id)

        if self.representation_of is not None and not isinstance(self.representation_of, ScientificKnowledgeExpressionId):
            self.representation_of = ScientificKnowledgeExpressionId(self.representation_of)

        if not isinstance(self.has_part, list):
            self.has_part = [self.has_part] if self.has_part is not None else []
        self.has_part = [v if isinstance(v, ScientificKnowledgeFragmentId) else ScientificKnowledgeFragmentId(v) for v in self.has_part]

        super().__post_init__(**kwargs)


@dataclass
class ScientificKnowledgeFragment(InformationContentEntity):
    """
    A selected subportion of the contents of a ScientificKnowledgeExpression, described by an selector.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKEM["ScientificKnowledgeFragment"]
    class_class_curie: ClassVar[str] = "skem:ScientificKnowledgeFragment"
    class_name: ClassVar[str] = "ScientificKnowledgeFragment"
    class_model_uri: ClassVar[URIRef] = SKEM.ScientificKnowledgeFragment

    id: Union[str, ScientificKnowledgeFragmentId] = None
    type: str = None
    part_of: Optional[Union[str, ScientificKnowledgeItemId]] = None
    offset: Optional[int] = None
    length: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificKnowledgeFragmentId):
            self.id = ScientificKnowledgeFragmentId(self.id)

        if self.part_of is not None and not isinstance(self.part_of, ScientificKnowledgeItemId):
            self.part_of = ScientificKnowledgeItemId(self.part_of)

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

    class_class_uri: ClassVar[URIRef] = SKEM["Note"]
    class_class_curie: ClassVar[str] = "skem:Note"
    class_name: ClassVar[str] = "Note"
    class_model_uri: ClassVar[URIRef] = SKEM.Note

    id: Union[str, NoteId] = None
    type: str = None
    is_about: Optional[Union[Union[str, InformationContentEntityId], List[Union[str, InformationContentEntityId]]]] = empty_list()
    format: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoteId):
            self.id = NoteId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.is_about, list):
            self.is_about = [self.is_about] if self.is_about is not None else []
        self.is_about = [v if isinstance(v, InformationContentEntityId) else InformationContentEntityId(v) for v in self.is_about]

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


@dataclass
class Author(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKEM["Author"]
    class_class_curie: ClassVar[str] = "skem:Author"
    class_name: ClassVar[str] = "Author"
    class_model_uri: ClassVar[URIRef] = SKEM.Author

    id: Union[str, AuthorId] = None
    type: str = None
    affiliations: Optional[Union[Union[str, OrganizationId], List[Union[str, OrganizationId]]]] = empty_list()
    is_author_of: Optional[Union[Union[str, ScientificKnowledgeExpressionId], List[Union[str, ScientificKnowledgeExpressionId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuthorId):
            self.id = AuthorId(self.id)

        if not isinstance(self.affiliations, list):
            self.affiliations = [self.affiliations] if self.affiliations is not None else []
        self.affiliations = [v if isinstance(v, OrganizationId) else OrganizationId(v) for v in self.affiliations]

        if not isinstance(self.is_author_of, list):
            self.is_author_of = [self.is_author_of] if self.is_author_of is not None else []
        self.is_author_of = [v if isinstance(v, ScientificKnowledgeExpressionId) else ScientificKnowledgeExpressionId(v) for v in self.is_author_of]

        super().__post_init__(**kwargs)


@dataclass
class Organization(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKEM["Organization"]
    class_class_curie: ClassVar[str] = "skem:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = SKEM.Organization

    id: Union[str, OrganizationId] = None
    type: str = None
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

    class_class_uri: ClassVar[URIRef] = SKEM["City"]
    class_class_curie: ClassVar[str] = "skem:City"
    class_name: ClassVar[str] = "City"
    class_model_uri: ClassVar[URIRef] = SKEM.City

    id: Union[str, CityId] = None
    type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CityId):
            self.id = CityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Country(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKEM["Country"]
    class_class_curie: ClassVar[str] = "skem:Country"
    class_name: ClassVar[str] = "Country"
    class_model_uri: ClassVar[URIRef] = SKEM.Country

    id: Union[str, CountryId] = None
    type: str = None
    code2: Optional[str] = None
    code3: Optional[str] = None
    region: Optional[str] = None
    income: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CountryId):
            self.id = CountryId(self.id)

        if self.code2 is not None and not isinstance(self.code2, str):
            self.code2 = str(self.code2)

        if self.code3 is not None and not isinstance(self.code3, str):
            self.code3 = str(self.code3)

        if self.region is not None and not isinstance(self.region, str):
            self.region = str(self.region)

        if self.income is not None and not isinstance(self.income, str):
            self.income = str(self.income)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.abstract = Slot(uri=SKEM.abstract, name="abstract", curie=SKEM.curie('abstract'),
                   model_uri=SKEM.abstract, domain=ScientificKnowledgeExpression, range=Optional[str])

slots.affiliations = Slot(uri=SKEM.affiliations, name="affiliations", curie=SKEM.curie('affiliations'),
                   model_uri=SKEM.affiliations, domain=Author, range=Optional[Union[Union[str, OrganizationId], List[Union[str, OrganizationId]]]])

slots.cites = Slot(uri=SKEM.cites, name="cites", curie=SKEM.curie('cites'),
                   model_uri=SKEM.cites, domain=ScientificKnowledgeExpression, range=Optional[Union[Union[str, ScientificKnowledgeExpressionId], List[Union[str, ScientificKnowledgeExpressionId]]]])

slots.content = Slot(uri=SKEM.content, name="content", curie=SKEM.curie('content'),
                   model_uri=SKEM.content, domain=InformationContentEntity, range=Optional[str])

slots.creation_date = Slot(uri=SKEM.creation_date, name="creation date", curie=SKEM.curie('creation_date'),
                   model_uri=SKEM.creation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.format = Slot(uri=SKEM.format, name="format", curie=SKEM.curie('format'),
                   model_uri=SKEM.format, domain=InformationContentEntity, range=Optional[str])

slots.has_authors = Slot(uri=SKEM.has_authors, name="has authors", curie=SKEM.curie('has_authors'),
                   model_uri=SKEM.has_authors, domain=ScientificKnowledgeExpression, range=Optional[Union[Union[str, AuthorId], List[Union[str, AuthorId]]]])

slots.has_members = Slot(uri=SKEM.has_members, name="has members", curie=SKEM.curie('has_members'),
                   model_uri=SKEM.has_members, domain=ScientificKnowledgeCollection, range=Optional[Union[Union[str, ScientificKnowledgeExpressionId], List[Union[str, ScientificKnowledgeExpressionId]]]])

slots.has_notes = Slot(uri=SKEM.has_notes, name="has notes", curie=SKEM.curie('has_notes'),
                   model_uri=SKEM.has_notes, domain=InformationContentEntity, range=Optional[Union[Union[str, NoteId], List[Union[str, NoteId]]]])

slots.has_part = Slot(uri=SKEM.has_part, name="has part", curie=SKEM.curie('has_part'),
                   model_uri=SKEM.has_part, domain=ScientificKnowledgeItem, range=Optional[Union[Union[str, ScientificKnowledgeFragmentId], List[Union[str, ScientificKnowledgeFragmentId]]]])

slots.has_representation = Slot(uri=SKEM.has_representation, name="has representation", curie=SKEM.curie('has_representation'),
                   model_uri=SKEM.has_representation, domain=ScientificKnowledgeExpression, range=Optional[Union[Union[str, ScientificKnowledgeItemId], List[Union[str, ScientificKnowledgeItemId]]]])

slots.iri = Slot(uri=SKEM.iri, name="iri", curie=SKEM.curie('iri'),
                   model_uri=SKEM.iri, domain=Entity, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.is_about = Slot(uri=SKEM.is_about, name="is about", curie=SKEM.curie('is_about'),
                   model_uri=SKEM.is_about, domain=Note, range=Optional[Union[Union[str, InformationContentEntityId], List[Union[str, InformationContentEntityId]]]])

slots.is_author_of = Slot(uri=SKEM.is_author_of, name="is author of", curie=SKEM.curie('is_author_of'),
                   model_uri=SKEM.is_author_of, domain=Author, range=Optional[Union[Union[str, ScientificKnowledgeExpressionId], List[Union[str, ScientificKnowledgeExpressionId]]]])

slots.license = Slot(uri=SKEM.license, name="license", curie=SKEM.curie('license'),
                   model_uri=SKEM.license, domain=InformationContentEntity, range=Optional[str])

slots.logical_query = Slot(uri=SKEM.logical_query, name="logical query", curie=SKEM.curie('logical_query'),
                   model_uri=SKEM.logical_query, domain=ScientificKnowledgeCollection, range=Optional[str])

slots.member_of = Slot(uri=SKEM.member_of, name="member of", curie=SKEM.curie('member_of'),
                   model_uri=SKEM.member_of, domain=ScientificKnowledgeExpression, range=Optional[Union[Union[str, ScientificKnowledgeCollectionId], List[Union[str, ScientificKnowledgeCollectionId]]]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=SKEM.name, domain=Entity, range=Optional[str])

slots.offset = Slot(uri=SKEM.offset, name="offset", curie=SKEM.curie('offset'),
                   model_uri=SKEM.offset, domain=ScientificKnowledgeFragment, range=Optional[int])

slots.length = Slot(uri=SKEM.length, name="length", curie=SKEM.curie('length'),
                   model_uri=SKEM.length, domain=ScientificKnowledgeFragment, range=Optional[int])

slots.part_of = Slot(uri=SKEM.part_of, name="part of", curie=SKEM.curie('part_of'),
                   model_uri=SKEM.part_of, domain=ScientificKnowledgeFragment, range=Optional[Union[str, ScientificKnowledgeItemId]])

slots.provenance = Slot(uri=SKEM.provenance, name="provenance", curie=SKEM.curie('provenance'),
                   model_uri=SKEM.provenance, domain=InformationContentEntity, range=Optional[str])

slots.publication_date = Slot(uri=SKEM.publication_date, name="publication date", curie=SKEM.curie('publication_date'),
                   model_uri=SKEM.publication_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.representation_of = Slot(uri=SKEM.representation_of, name="representation of", curie=SKEM.curie('representation_of'),
                   model_uri=SKEM.representation_of, domain=ScientificKnowledgeItem, range=Optional[Union[str, ScientificKnowledgeExpressionId]])

slots.rights = Slot(uri=SKEM.rights, name="rights", curie=SKEM.curie('rights'),
                   model_uri=SKEM.rights, domain=InformationContentEntity, range=Optional[str])

slots.token_count = Slot(uri=SKEM.token_count, name="token count", curie=SKEM.curie('token_count'),
                   model_uri=SKEM.token_count, domain=InformationContentEntity, range=Optional[int])

slots.type = Slot(uri=SKEM.type, name="type", curie=SKEM.curie('type'),
                   model_uri=SKEM.type, domain=Entity, range=str)

slots.id = Slot(uri=SKEM.id, name="id", curie=SKEM.curie('id'),
                   model_uri=SKEM.id, domain=None, range=URIRef)

slots.xref = Slot(uri=SKEM.xref, name="xref", curie=SKEM.curie('xref'),
                   model_uri=SKEM.xref, domain=InformationContentEntity, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.organization__city = Slot(uri=SKEM.city, name="organization__city", curie=SKEM.curie('city'),
                   model_uri=SKEM.organization__city, domain=None, range=Optional[Union[Union[str, CityId], List[Union[str, CityId]]]])

slots.organization__country = Slot(uri=SKEM.country, name="organization__country", curie=SKEM.curie('country'),
                   model_uri=SKEM.organization__country, domain=None, range=Optional[Union[Union[str, CountryId], List[Union[str, CountryId]]]])

slots.country__code2 = Slot(uri=SKEM.code2, name="country__code2", curie=SKEM.curie('code2'),
                   model_uri=SKEM.country__code2, domain=None, range=Optional[str])

slots.country__code3 = Slot(uri=SKEM.code3, name="country__code3", curie=SKEM.curie('code3'),
                   model_uri=SKEM.country__code3, domain=None, range=Optional[str])

slots.country__region = Slot(uri=SKEM.region, name="country__region", curie=SKEM.curie('region'),
                   model_uri=SKEM.country__region, domain=None, range=Optional[str])

slots.country__income = Slot(uri=SKEM.income, name="country__income", curie=SKEM.curie('income'),
                   model_uri=SKEM.country__income, domain=None, range=Optional[str])

slots.ScientificKnowledgeExpression_type = Slot(uri=SKEM.type, name="ScientificKnowledgeExpression_type", curie=SKEM.curie('type'),
                   model_uri=SKEM.ScientificKnowledgeExpression_type, domain=ScientificKnowledgeExpression, range=str)
