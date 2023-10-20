-- # Class: "Entity" Description: "Root Model class for all things and informational relationships, real or imagined."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
-- # Class: "NamedThing" Description: "an entity or concept/class described by a name"
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
-- # Class: "InformationContentEntity" Description: "a piece of information that typically describes some topic of discourse or is used as support."
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
-- # Class: "Work" Description: "A published work"
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: title Description: The Title of a work.
--     * Slot: abstract Description: The written abstract of a work. This is typically a paragraph of text providing  a summary of the main findings of the work.
--     * Slot: full_text Description: The full textual content of a work, expressed as a string (usually with an associated specified encoding / schema / format).
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
-- # Class: "InformationResource" Description: "A database or knowledgebase and its supporting ecosystem of interfaces  and services that deliver content to consumers (e.g. web portals, APIs,  query endpoints, streaming services, data downloads, etc.). A single Information Resource by this definition may span many different datasets or databases, and include many access endpoints and user interfaces. Information Resources include project-specific resources such as a Translator Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb."
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
-- # Class: "WorkCollection" Description: "A collection of works."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: logical_query Description: A logical query that can be used to retrieve a set of entities from a  knowledgebase. Typically expressed as a boolean logic expression over  terms to be searched for.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
-- # Class: "WorkFragment" Description: "A selected subportion of the contents of a Work, described by an selector."
--     * Slot: part_of Description: The work that this fragment is a part of
--     * Slot: selector Description: A way of specifying a location within a Work that describes where a WorkFragment comes from
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
-- # Class: "Selector" Description: "A way of localizing and describing a WorkFragment within a Work."
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
-- # Class: "OffsetTextSelector" Description: "A way of localizing and describing a fragment of text within a larger body of text using offsets and lengths."
--     * Slot: offset Description: The offset of the start of the fragment from the start of the text.
--     * Slot: length Description: The length of the fragment.
--     * Slot: text Description: The text of the fragment.
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
-- # Class: "Person" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
-- # Class: "Author" Description: ""
--     * Slot: orcid Description: An ORCID for an entity. 
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
--     * Slot: Work_id Description: Autocreated FK slot
-- # Class: "Organization" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
-- # Class: "City" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
-- # Class: "Country" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity. This is determined by the id using expansion rules.
-- # Class: "Entity_type" Description: ""
--     * Slot: Entity_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "NamedThing_xref" Description: ""
--     * Slot: NamedThing_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "NamedThing_type" Description: ""
--     * Slot: NamedThing_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "InformationContentEntity_xref" Description: ""
--     * Slot: InformationContentEntity_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "InformationContentEntity_type" Description: ""
--     * Slot: InformationContentEntity_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "Work_has_part" Description: ""
--     * Slot: Work_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: Fragments that have been highlighted as as part of this work.
-- # Class: "Work_xref" Description: ""
--     * Slot: Work_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "Work_type" Description: ""
--     * Slot: Work_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "InformationResource_xref" Description: ""
--     * Slot: InformationResource_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "InformationResource_type" Description: ""
--     * Slot: InformationResource_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "WorkCollection_information_sources" Description: ""
--     * Slot: WorkCollection_id Description: Autocreated FK slot
--     * Slot: information_sources_id Description: The InformationResources that are queried to build a WorkCollection.
-- # Class: "WorkCollection_has_part" Description: ""
--     * Slot: WorkCollection_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: The works that are part of the collection.
-- # Class: "WorkCollection_xref" Description: ""
--     * Slot: WorkCollection_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "WorkCollection_type" Description: ""
--     * Slot: WorkCollection_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "WorkFragment_xref" Description: ""
--     * Slot: WorkFragment_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "WorkFragment_type" Description: ""
--     * Slot: WorkFragment_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "Selector_xref" Description: ""
--     * Slot: Selector_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "Selector_type" Description: ""
--     * Slot: Selector_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "OffsetTextSelector_xref" Description: ""
--     * Slot: OffsetTextSelector_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "OffsetTextSelector_type" Description: ""
--     * Slot: OffsetTextSelector_id Description: Autocreated FK slot
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
	PRIMARY KEY (id)
);
CREATE TABLE "NamedThing" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
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
	PRIMARY KEY (id)
);
CREATE TABLE "Work" (
	id TEXT NOT NULL, 
	title TEXT, 
	abstract TEXT, 
	full_text TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "InformationResource" (
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "WorkCollection" (
	id TEXT NOT NULL, 
	name TEXT, 
	logical_query TEXT, 
	creation_date DATE, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	iri TEXT, 
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
	PRIMARY KEY (id)
);
CREATE TABLE "OffsetTextSelector" (
	"offset" INTEGER, 
	length INTEGER, 
	text TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Person" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Organization" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "City" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Country" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "WorkFragment" (
	part_of TEXT, 
	selector TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(part_of) REFERENCES "Work" (id), 
	FOREIGN KEY(selector) REFERENCES "Selector" (id)
);
CREATE TABLE "Author" (
	orcid TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	"Work_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Work_id") REFERENCES "Work" (id)
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
CREATE TABLE "Work_xref" (
	"Work_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("Work_id", xref), 
	FOREIGN KEY("Work_id") REFERENCES "Work" (id)
);
CREATE TABLE "Work_type" (
	"Work_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("Work_id", type), 
	FOREIGN KEY("Work_id") REFERENCES "Work" (id)
);
CREATE TABLE "InformationResource_xref" (
	"InformationResource_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("InformationResource_id", xref), 
	FOREIGN KEY("InformationResource_id") REFERENCES "InformationResource" (id)
);
CREATE TABLE "InformationResource_type" (
	"InformationResource_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("InformationResource_id", type), 
	FOREIGN KEY("InformationResource_id") REFERENCES "InformationResource" (id)
);
CREATE TABLE "WorkCollection_information_sources" (
	"WorkCollection_id" TEXT, 
	information_sources_id TEXT, 
	PRIMARY KEY ("WorkCollection_id", information_sources_id), 
	FOREIGN KEY("WorkCollection_id") REFERENCES "WorkCollection" (id), 
	FOREIGN KEY(information_sources_id) REFERENCES "InformationResource" (id)
);
CREATE TABLE "WorkCollection_has_part" (
	"WorkCollection_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("WorkCollection_id", has_part_id), 
	FOREIGN KEY("WorkCollection_id") REFERENCES "WorkCollection" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "Work" (id)
);
CREATE TABLE "WorkCollection_xref" (
	"WorkCollection_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("WorkCollection_id", xref), 
	FOREIGN KEY("WorkCollection_id") REFERENCES "WorkCollection" (id)
);
CREATE TABLE "WorkCollection_type" (
	"WorkCollection_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("WorkCollection_id", type), 
	FOREIGN KEY("WorkCollection_id") REFERENCES "WorkCollection" (id)
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
CREATE TABLE "Work_has_part" (
	"Work_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("Work_id", has_part_id), 
	FOREIGN KEY("Work_id") REFERENCES "Work" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "WorkFragment" (id)
);
CREATE TABLE "WorkFragment_xref" (
	"WorkFragment_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("WorkFragment_id", xref), 
	FOREIGN KEY("WorkFragment_id") REFERENCES "WorkFragment" (id)
);
CREATE TABLE "WorkFragment_type" (
	"WorkFragment_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("WorkFragment_id", type), 
	FOREIGN KEY("WorkFragment_id") REFERENCES "WorkFragment" (id)
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
