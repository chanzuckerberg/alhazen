-- # Class: "Entity" Description: "Root Model class for all things and informational relationships, real or imagined."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "NamedThing" Description: "an entity or concept/class described by a name"
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "InformationContentEntity" Description: "a piece of information that typically describes some topic of discourse or is used as support."
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "ScientificKnowledgeExpression" Description: "Any expression of scientific knowledge.   "
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: title Description: The title of a ScientificKnowledgeExpression.
--     * Slot: abstract Description: The written abstract of a ScientificKnowledgeExpression.  This is typically a paragraph of text providing  a summary of the expression.
--     * Slot: publication_date Description: date on which an entity was published (i.e., made available to the public).
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "ScientificPublication" Description: "A published expression of scientific knowledge,  such as a paper, book, thesis, conference proceedings, etc.   "
--     * Slot: doi Description: A digital object identifier (see http://doi.org/).
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: title Description: The title of a ScientificKnowledgeExpression.
--     * Slot: abstract Description: The written abstract of a ScientificKnowledgeExpression.  This is typically a paragraph of text providing  a summary of the expression.
--     * Slot: publication_date Description: date on which an entity was published (i.e., made available to the public).
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "InformationResource" Description: "A database or knowledgebase and its supporting ecosystem of interfaces  and services that deliver content to consumers (e.g. web portals, APIs,  query endpoints, streaming services, data downloads, etc.). A single Information Resource by this definition may span many different datasets or databases, and include many access endpoints and user interfaces. Information Resources include project-specific resources such as a Translator Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "ScientificKnowledgeCollection" Description: "A collection of expressions of scientific knowledge."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: logical_query Description: A logical query that can be used to retrieve a set of entities from a  knowledgebase. Typically expressed as a boolean logic expression over  terms to be searched for.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "ScientificPublicationCollection" Description: "A collection of scientific publications."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: logical_query Description: A logical query that can be used to retrieve a set of entities from a  knowledgebase. Typically expressed as a boolean logic expression over  terms to be searched for.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "ScientificKnowledgeFragment" Description: "A selected subportion of the contents of a ScientificKnowledgeExpression, described by an selector."
--     * Slot: part_of Description: The SKE that this fragment is a part of
--     * Slot: selector Description: A way of specifying a location within a ScientificKnowledgeExpression that describes where a ScientificKnowledgeFragment comes from
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "Selector" Description: "A way of localizing and describing a ScientificKnowledgeFragment within a ScientificKnowledgeExpression."
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "OffsetTextSelector" Description: "A way of localizing and describing a fragment of text within a larger body of text using offsets and lengths."
--     * Slot: offset Description: The offset of the start of the fragment from the start of the text.
--     * Slot: length Description: The length of the fragment.
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "Note" Description: "A structured piece of information with an author that is about another InformationContentEntity."
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "NameValuePair" Description: "A single map {string :- string} to track structured data in a note."
--     * Slot: variable Description: The name of an attribute recorded in a Note. This is currently stored as an unstructured string.
--     * Slot: value Description: The value of an attribute recorded in a Note. This is currently stored as an unstructured string.
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "Person" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "Author" Description: ""
--     * Slot: orcid Description: An ORCID for an entity. 
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: ScientificPublication_id Description: Autocreated FK slot
--     * Slot: Note_id Description: Autocreated FK slot
-- # Class: "Organization" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "City" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "Country" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: type_str Description: A simple textual representation of the entity's type (for polymorphism mechansisms)
-- # Class: "Entity_type" Description: ""
--     * Slot: Entity_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "NamedThing_xref" Description: ""
--     * Slot: NamedThing_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "NamedThing_type" Description: ""
--     * Slot: NamedThing_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "InformationContentEntity_provenance" Description: ""
--     * Slot: InformationContentEntity_id Description: Autocreated FK slot
--     * Slot: provenance_id Description: A description of the provenance of an information content entity.
-- # Class: "InformationContentEntity_xref" Description: ""
--     * Slot: InformationContentEntity_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "InformationContentEntity_type" Description: ""
--     * Slot: InformationContentEntity_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificKnowledgeExpression_has_part" Description: ""
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: Fragments that have been highlighted as as part of this SKE.
-- # Class: "ScientificKnowledgeExpression_provenance" Description: ""
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: provenance_id Description: A description of the provenance of an information content entity.
-- # Class: "ScientificKnowledgeExpression_xref" Description: ""
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificKnowledgeExpression_type" Description: ""
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificPublication_has_part" Description: ""
--     * Slot: ScientificPublication_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: Fragments that have been highlighted as as part of this SKE.
-- # Class: "ScientificPublication_provenance" Description: ""
--     * Slot: ScientificPublication_id Description: Autocreated FK slot
--     * Slot: provenance_id Description: A description of the provenance of an information content entity.
-- # Class: "ScientificPublication_xref" Description: ""
--     * Slot: ScientificPublication_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificPublication_type" Description: ""
--     * Slot: ScientificPublication_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "InformationResource_xref" Description: ""
--     * Slot: InformationResource_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "InformationResource_provenance" Description: ""
--     * Slot: InformationResource_id Description: Autocreated FK slot
--     * Slot: provenance_id Description: A description of the provenance of an information content entity.
-- # Class: "InformationResource_type" Description: ""
--     * Slot: InformationResource_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificKnowledgeCollection_information_sources" Description: ""
--     * Slot: ScientificKnowledgeCollection_id Description: Autocreated FK slot
--     * Slot: information_sources_id Description: The source of information described in a Note.
-- # Class: "ScientificKnowledgeCollection_provenance" Description: ""
--     * Slot: ScientificKnowledgeCollection_id Description: Autocreated FK slot
--     * Slot: provenance_id Description: A description of the provenance of an information content entity.
-- # Class: "ScientificKnowledgeCollection_xref" Description: ""
--     * Slot: ScientificKnowledgeCollection_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificKnowledgeCollection_type" Description: ""
--     * Slot: ScientificKnowledgeCollection_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificPublicationCollection_has_part" Description: ""
--     * Slot: ScientificPublicationCollection_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: The publications that are part of the collection.
-- # Class: "ScientificPublicationCollection_information_sources" Description: ""
--     * Slot: ScientificPublicationCollection_id Description: Autocreated FK slot
--     * Slot: information_sources_id Description: The source of information described in a Note.
-- # Class: "ScientificPublicationCollection_provenance" Description: ""
--     * Slot: ScientificPublicationCollection_id Description: Autocreated FK slot
--     * Slot: provenance_id Description: A description of the provenance of an information content entity.
-- # Class: "ScientificPublicationCollection_xref" Description: ""
--     * Slot: ScientificPublicationCollection_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificPublicationCollection_type" Description: ""
--     * Slot: ScientificPublicationCollection_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificKnowledgeFragment_provenance" Description: ""
--     * Slot: ScientificKnowledgeFragment_id Description: Autocreated FK slot
--     * Slot: provenance_id Description: A description of the provenance of an information content entity.
-- # Class: "ScientificKnowledgeFragment_xref" Description: ""
--     * Slot: ScientificKnowledgeFragment_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificKnowledgeFragment_type" Description: ""
--     * Slot: ScientificKnowledgeFragment_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "Selector_provenance" Description: ""
--     * Slot: Selector_id Description: Autocreated FK slot
--     * Slot: provenance_id Description: A description of the provenance of an information content entity.
-- # Class: "Selector_xref" Description: ""
--     * Slot: Selector_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "Selector_type" Description: ""
--     * Slot: Selector_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "OffsetTextSelector_provenance" Description: ""
--     * Slot: OffsetTextSelector_id Description: Autocreated FK slot
--     * Slot: provenance_id Description: A description of the provenance of an information content entity.
-- # Class: "OffsetTextSelector_xref" Description: ""
--     * Slot: OffsetTextSelector_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "OffsetTextSelector_type" Description: ""
--     * Slot: OffsetTextSelector_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "Note_is_about" Description: ""
--     * Slot: Note_id Description: Autocreated FK slot
--     * Slot: is_about_id Description: A (currently) primitive relation that relates an information artifact to an entity. 
-- # Class: "Note_structured_content" Description: ""
--     * Slot: Note_id Description: Autocreated FK slot
--     * Slot: structured_content_id Description: A collection of structured information contained in a Note.
-- # Class: "Note_provenance" Description: ""
--     * Slot: Note_id Description: Autocreated FK slot
--     * Slot: provenance_id Description: A description of the provenance of an information content entity.
-- # Class: "Note_xref" Description: ""
--     * Slot: Note_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "Note_type" Description: ""
--     * Slot: Note_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "NameValuePair_provenance" Description: ""
--     * Slot: NameValuePair_id Description: Autocreated FK slot
--     * Slot: provenance_id Description: A description of the provenance of an information content entity.
-- # Class: "NameValuePair_xref" Description: ""
--     * Slot: NameValuePair_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "NameValuePair_type" Description: ""
--     * Slot: NameValuePair_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "Person_xref" Description: ""
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "Person_type" Description: ""
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "Author_affiliations" Description: ""
--     * Slot: Author_id Description: Autocreated FK slot
--     * Slot: affiliations_id Description: The affiliations of an author. 
-- # Class: "Author_xref" Description: ""
--     * Slot: Author_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "Author_type" Description: ""
--     * Slot: Author_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "Organization_city" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: city_id Description: 
-- # Class: "Organization_country" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: country_id Description: 
-- # Class: "Organization_xref" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "Organization_type" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "City_xref" Description: ""
--     * Slot: City_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "City_type" Description: ""
--     * Slot: City_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "Country_xref" Description: ""
--     * Slot: Country_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "Country_type" Description: ""
--     * Slot: Country_id Description: Autocreated FK slot
--     * Slot: type Description: 

CREATE TABLE "Entity" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "NamedThing" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "InformationContentEntity" (
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificKnowledgeExpression" (
	id TEXT NOT NULL, 
	title TEXT, 
	abstract TEXT, 
	publication_date DATE, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificPublication" (
	doi TEXT, 
	type_str VARCHAR(33), 
	id TEXT NOT NULL, 
	title TEXT, 
	abstract TEXT, 
	publication_date DATE, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "InformationResource" (
	id TEXT NOT NULL, 
	name TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificKnowledgeCollection" (
	id TEXT NOT NULL, 
	name TEXT, 
	logical_query TEXT, 
	creation_date DATE, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificPublicationCollection" (
	id TEXT NOT NULL, 
	name TEXT, 
	logical_query TEXT, 
	creation_date DATE, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Selector" (
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "OffsetTextSelector" (
	"offset" INTEGER, 
	length INTEGER, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Note" (
	format TEXT, 
	type_str VARCHAR(20), 
	license TEXT, 
	rights TEXT, 
	creation_date DATE, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "NameValuePair" (
	variable TEXT, 
	value TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Person" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Organization" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "City" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Country" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificKnowledgeFragment" (
	part_of TEXT, 
	selector TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	type_str TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(part_of) REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY(selector) REFERENCES "Selector" (id)
);
CREATE TABLE "Author" (
	orcid TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	type_str TEXT, 
	"ScientificKnowledgeExpression_id" TEXT, 
	"ScientificPublication_id" TEXT, 
	"Note_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY("ScientificPublication_id") REFERENCES "ScientificPublication" (id), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id)
);
CREATE TABLE "Entity_type" (
	"Entity_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("Entity_id", type), 
	FOREIGN KEY("Entity_id") REFERENCES "Entity" (id)
);
CREATE TABLE "NamedThing_xref" (
	"NamedThing_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("NamedThing_id", xref), 
	FOREIGN KEY("NamedThing_id") REFERENCES "NamedThing" (id)
);
CREATE TABLE "NamedThing_type" (
	"NamedThing_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("NamedThing_id", type), 
	FOREIGN KEY("NamedThing_id") REFERENCES "NamedThing" (id)
);
CREATE TABLE "InformationContentEntity_provenance" (
	"InformationContentEntity_id" TEXT, 
	provenance_id TEXT, 
	PRIMARY KEY ("InformationContentEntity_id", provenance_id), 
	FOREIGN KEY("InformationContentEntity_id") REFERENCES "InformationContentEntity" (id), 
	FOREIGN KEY(provenance_id) REFERENCES "Note" (id)
);
CREATE TABLE "InformationContentEntity_xref" (
	"InformationContentEntity_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("InformationContentEntity_id", xref), 
	FOREIGN KEY("InformationContentEntity_id") REFERENCES "InformationContentEntity" (id)
);
CREATE TABLE "InformationContentEntity_type" (
	"InformationContentEntity_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("InformationContentEntity_id", type), 
	FOREIGN KEY("InformationContentEntity_id") REFERENCES "InformationContentEntity" (id)
);
CREATE TABLE "ScientificKnowledgeExpression_provenance" (
	"ScientificKnowledgeExpression_id" TEXT, 
	provenance_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", provenance_id), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY(provenance_id) REFERENCES "Note" (id)
);
CREATE TABLE "ScientificKnowledgeExpression_xref" (
	"ScientificKnowledgeExpression_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", xref), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id)
);
CREATE TABLE "ScientificKnowledgeExpression_type" (
	"ScientificKnowledgeExpression_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", type), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id)
);
CREATE TABLE "ScientificPublication_provenance" (
	"ScientificPublication_id" TEXT, 
	provenance_id TEXT, 
	PRIMARY KEY ("ScientificPublication_id", provenance_id), 
	FOREIGN KEY("ScientificPublication_id") REFERENCES "ScientificPublication" (id), 
	FOREIGN KEY(provenance_id) REFERENCES "Note" (id)
);
CREATE TABLE "ScientificPublication_xref" (
	"ScientificPublication_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificPublication_id", xref), 
	FOREIGN KEY("ScientificPublication_id") REFERENCES "ScientificPublication" (id)
);
CREATE TABLE "ScientificPublication_type" (
	"ScientificPublication_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("ScientificPublication_id", type), 
	FOREIGN KEY("ScientificPublication_id") REFERENCES "ScientificPublication" (id)
);
CREATE TABLE "InformationResource_xref" (
	"InformationResource_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("InformationResource_id", xref), 
	FOREIGN KEY("InformationResource_id") REFERENCES "InformationResource" (id)
);
CREATE TABLE "InformationResource_provenance" (
	"InformationResource_id" TEXT, 
	provenance_id TEXT, 
	PRIMARY KEY ("InformationResource_id", provenance_id), 
	FOREIGN KEY("InformationResource_id") REFERENCES "InformationResource" (id), 
	FOREIGN KEY(provenance_id) REFERENCES "Note" (id)
);
CREATE TABLE "InformationResource_type" (
	"InformationResource_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("InformationResource_id", type), 
	FOREIGN KEY("InformationResource_id") REFERENCES "InformationResource" (id)
);
CREATE TABLE "ScientificKnowledgeCollection_information_sources" (
	"ScientificKnowledgeCollection_id" TEXT, 
	information_sources_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", information_sources_id), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id), 
	FOREIGN KEY(information_sources_id) REFERENCES "InformationResource" (id)
);
CREATE TABLE "ScientificKnowledgeCollection_provenance" (
	"ScientificKnowledgeCollection_id" TEXT, 
	provenance_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", provenance_id), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id), 
	FOREIGN KEY(provenance_id) REFERENCES "Note" (id)
);
CREATE TABLE "ScientificKnowledgeCollection_xref" (
	"ScientificKnowledgeCollection_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", xref), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id)
);
CREATE TABLE "ScientificKnowledgeCollection_type" (
	"ScientificKnowledgeCollection_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", type), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id)
);
CREATE TABLE "ScientificPublicationCollection_has_part" (
	"ScientificPublicationCollection_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("ScientificPublicationCollection_id", has_part_id), 
	FOREIGN KEY("ScientificPublicationCollection_id") REFERENCES "ScientificPublicationCollection" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ScientificPublication" (id)
);
CREATE TABLE "ScientificPublicationCollection_information_sources" (
	"ScientificPublicationCollection_id" TEXT, 
	information_sources_id TEXT, 
	PRIMARY KEY ("ScientificPublicationCollection_id", information_sources_id), 
	FOREIGN KEY("ScientificPublicationCollection_id") REFERENCES "ScientificPublicationCollection" (id), 
	FOREIGN KEY(information_sources_id) REFERENCES "InformationResource" (id)
);
CREATE TABLE "ScientificPublicationCollection_provenance" (
	"ScientificPublicationCollection_id" TEXT, 
	provenance_id TEXT, 
	PRIMARY KEY ("ScientificPublicationCollection_id", provenance_id), 
	FOREIGN KEY("ScientificPublicationCollection_id") REFERENCES "ScientificPublicationCollection" (id), 
	FOREIGN KEY(provenance_id) REFERENCES "Note" (id)
);
CREATE TABLE "ScientificPublicationCollection_xref" (
	"ScientificPublicationCollection_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificPublicationCollection_id", xref), 
	FOREIGN KEY("ScientificPublicationCollection_id") REFERENCES "ScientificPublicationCollection" (id)
);
CREATE TABLE "ScientificPublicationCollection_type" (
	"ScientificPublicationCollection_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("ScientificPublicationCollection_id", type), 
	FOREIGN KEY("ScientificPublicationCollection_id") REFERENCES "ScientificPublicationCollection" (id)
);
CREATE TABLE "Selector_provenance" (
	"Selector_id" TEXT, 
	provenance_id TEXT, 
	PRIMARY KEY ("Selector_id", provenance_id), 
	FOREIGN KEY("Selector_id") REFERENCES "Selector" (id), 
	FOREIGN KEY(provenance_id) REFERENCES "Note" (id)
);
CREATE TABLE "Selector_xref" (
	"Selector_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("Selector_id", xref), 
	FOREIGN KEY("Selector_id") REFERENCES "Selector" (id)
);
CREATE TABLE "Selector_type" (
	"Selector_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("Selector_id", type), 
	FOREIGN KEY("Selector_id") REFERENCES "Selector" (id)
);
CREATE TABLE "OffsetTextSelector_provenance" (
	"OffsetTextSelector_id" TEXT, 
	provenance_id TEXT, 
	PRIMARY KEY ("OffsetTextSelector_id", provenance_id), 
	FOREIGN KEY("OffsetTextSelector_id") REFERENCES "OffsetTextSelector" (id), 
	FOREIGN KEY(provenance_id) REFERENCES "Note" (id)
);
CREATE TABLE "OffsetTextSelector_xref" (
	"OffsetTextSelector_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("OffsetTextSelector_id", xref), 
	FOREIGN KEY("OffsetTextSelector_id") REFERENCES "OffsetTextSelector" (id)
);
CREATE TABLE "OffsetTextSelector_type" (
	"OffsetTextSelector_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("OffsetTextSelector_id", type), 
	FOREIGN KEY("OffsetTextSelector_id") REFERENCES "OffsetTextSelector" (id)
);
CREATE TABLE "Note_is_about" (
	"Note_id" TEXT, 
	is_about_id TEXT, 
	PRIMARY KEY ("Note_id", is_about_id), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id), 
	FOREIGN KEY(is_about_id) REFERENCES "Entity" (id)
);
CREATE TABLE "Note_structured_content" (
	"Note_id" TEXT, 
	structured_content_id TEXT, 
	PRIMARY KEY ("Note_id", structured_content_id), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id), 
	FOREIGN KEY(structured_content_id) REFERENCES "NameValuePair" (id)
);
CREATE TABLE "Note_provenance" (
	"Note_id" TEXT, 
	provenance_id TEXT, 
	PRIMARY KEY ("Note_id", provenance_id), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id), 
	FOREIGN KEY(provenance_id) REFERENCES "Note" (id)
);
CREATE TABLE "Note_xref" (
	"Note_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("Note_id", xref), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id)
);
CREATE TABLE "Note_type" (
	"Note_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("Note_id", type), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id)
);
CREATE TABLE "NameValuePair_provenance" (
	"NameValuePair_id" TEXT, 
	provenance_id TEXT, 
	PRIMARY KEY ("NameValuePair_id", provenance_id), 
	FOREIGN KEY("NameValuePair_id") REFERENCES "NameValuePair" (id), 
	FOREIGN KEY(provenance_id) REFERENCES "Note" (id)
);
CREATE TABLE "NameValuePair_xref" (
	"NameValuePair_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("NameValuePair_id", xref), 
	FOREIGN KEY("NameValuePair_id") REFERENCES "NameValuePair" (id)
);
CREATE TABLE "NameValuePair_type" (
	"NameValuePair_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("NameValuePair_id", type), 
	FOREIGN KEY("NameValuePair_id") REFERENCES "NameValuePair" (id)
);
CREATE TABLE "Person_xref" (
	"Person_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("Person_id", xref), 
	FOREIGN KEY("Person_id") REFERENCES "Person" (id)
);
CREATE TABLE "Person_type" (
	"Person_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("Person_id", type), 
	FOREIGN KEY("Person_id") REFERENCES "Person" (id)
);
CREATE TABLE "Organization_city" (
	"Organization_id" TEXT, 
	city_id TEXT, 
	PRIMARY KEY ("Organization_id", city_id), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id), 
	FOREIGN KEY(city_id) REFERENCES "City" (id)
);
CREATE TABLE "Organization_country" (
	"Organization_id" TEXT, 
	country_id TEXT, 
	PRIMARY KEY ("Organization_id", country_id), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id), 
	FOREIGN KEY(country_id) REFERENCES "Country" (id)
);
CREATE TABLE "Organization_xref" (
	"Organization_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("Organization_id", xref), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE TABLE "Organization_type" (
	"Organization_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("Organization_id", type), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE TABLE "City_xref" (
	"City_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("City_id", xref), 
	FOREIGN KEY("City_id") REFERENCES "City" (id)
);
CREATE TABLE "City_type" (
	"City_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("City_id", type), 
	FOREIGN KEY("City_id") REFERENCES "City" (id)
);
CREATE TABLE "Country_xref" (
	"Country_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("Country_id", xref), 
	FOREIGN KEY("Country_id") REFERENCES "Country" (id)
);
CREATE TABLE "Country_type" (
	"Country_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("Country_id", type), 
	FOREIGN KEY("Country_id") REFERENCES "Country" (id)
);
CREATE TABLE "ScientificKnowledgeExpression_has_part" (
	"ScientificKnowledgeExpression_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", has_part_id), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "ScientificPublication_has_part" (
	"ScientificPublication_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("ScientificPublication_id", has_part_id), 
	FOREIGN KEY("ScientificPublication_id") REFERENCES "ScientificPublication" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "ScientificKnowledgeFragment_provenance" (
	"ScientificKnowledgeFragment_id" TEXT, 
	provenance_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeFragment_id", provenance_id), 
	FOREIGN KEY("ScientificKnowledgeFragment_id") REFERENCES "ScientificKnowledgeFragment" (id), 
	FOREIGN KEY(provenance_id) REFERENCES "Note" (id)
);
CREATE TABLE "ScientificKnowledgeFragment_xref" (
	"ScientificKnowledgeFragment_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificKnowledgeFragment_id", xref), 
	FOREIGN KEY("ScientificKnowledgeFragment_id") REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "ScientificKnowledgeFragment_type" (
	"ScientificKnowledgeFragment_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("ScientificKnowledgeFragment_id", type), 
	FOREIGN KEY("ScientificKnowledgeFragment_id") REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "Author_affiliations" (
	"Author_id" TEXT, 
	affiliations_id TEXT, 
	PRIMARY KEY ("Author_id", affiliations_id), 
	FOREIGN KEY("Author_id") REFERENCES "Author" (id), 
	FOREIGN KEY(affiliations_id) REFERENCES "Organization" (id)
);
CREATE TABLE "Author_xref" (
	"Author_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("Author_id", xref), 
	FOREIGN KEY("Author_id") REFERENCES "Author" (id)
);
CREATE TABLE "Author_type" (
	"Author_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("Author_id", type), 
	FOREIGN KEY("Author_id") REFERENCES "Author" (id)
);
