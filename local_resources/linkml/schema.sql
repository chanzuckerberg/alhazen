-- # Class: "Entity" Description: "Root Model class for all things and informational relationships, real or imagined."
--     * Slot: id Description: A simple, locally-generated unique identifier specific with different heuristic formatting for each application.
--     * Slot: type Description: The type of an Entity expressed as curi.
-- # Class: "NamedThing" Description: "an entity or concept/class described by a name"
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A simple, locally-generated unique identifier specific with different heuristic formatting for each application.
--     * Slot: type Description: The type of an Entity expressed as curi.
-- # Class: "InformationContentEntity" Description: "a piece of information that typically describes some topic of discourse or is used as support."
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: content Description: The content of an InformationContentEntity expressed as a string.
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A simple, locally-generated unique identifier specific with different heuristic formatting for each application.
--     * Slot: type Description: The type of an Entity expressed as curi.
-- # Class: "InformationResource" Description: "A database or knowledgebase and its supporting ecosystem of interfaces  and services that deliver content to consumers (e.g. web portals, APIs,  query endpoints, streaming services, data downloads, etc.). A single Information Resource by this definition may span many different datasets or databases, and include many access endpoints and user interfaces. Information Resources include project-specific resources such as a Translator Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb."
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: content Description: The content of an InformationContentEntity expressed as a string.
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A simple, locally-generated unique identifier specific with different heuristic formatting for each application.
--     * Slot: type Description: The type of an Entity expressed as curi.
-- # Class: "ScientificKnowledgeCollection" Description: "A collection of expressions of scientific knowledge."
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: content Description: The content of an InformationContentEntity expressed as a string.
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A simple, locally-generated unique identifier specific with different heuristic formatting for each application.
--     * Slot: type Description: The type of an Entity expressed as curi.
-- # Class: "ScientificKnowledgeExpression" Description: "Any expression of scientific knowledge.   "
--     * Slot: publication_date Description: date on which an entity was published (i.e., made available to the public).
--     * Slot: type Description: The type of an Entity expressed as curi.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: content Description: The content of an InformationContentEntity expressed as a string.
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A simple, locally-generated unique identifier specific with different heuristic formatting for each application.
-- # Class: "ScientificKnowledgeItem" Description: "A specific instance of a ScientificKnowledgeExpression:- our internal representation of an EPMC citation record, a local copy of a full-text article. This is the substrate that forms the basis for a ScientificKnowledgeFragment."
--     * Slot: representation_of Description: The ScientificKnowledgeExpression that this ScientificKnowledgeItem  is a representation of.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: content Description: The content of an InformationContentEntity expressed as a string.
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A simple, locally-generated unique identifier specific with different heuristic formatting for each application.
--     * Slot: type Description: The type of an Entity expressed as curi.
-- # Class: "ScientificKnowledgeFragment" Description: "A selected subportion of the contents of a ScientificKnowledgeExpression, described by an selector."
--     * Slot: part_of Description: holds between parts and wholes (material entities or processes)
--     * Slot: offset Description: The offset of the start of the fragment from the start of the text.
--     * Slot: length Description: The length of the fragment.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: content Description: The content of an InformationContentEntity expressed as a string.
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A simple, locally-generated unique identifier specific with different heuristic formatting for each application.
--     * Slot: type Description: The type of an Entity expressed as curi.
-- # Class: "Note" Description: "A structured piece of information with an author that is about another InformationContentEntity."
--     * Slot: format Description: The format (JSON, XML, BINARY) of the content of an InformationContentEntity.
--     * Slot: type Description: The type of an Entity expressed as curi.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: content Description: The content of an InformationContentEntity expressed as a string.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A simple, locally-generated unique identifier specific with different heuristic formatting for each application.
-- # Class: "Author" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A simple, locally-generated unique identifier specific with different heuristic formatting for each application.
--     * Slot: type Description: The type of an Entity expressed as curi.
--     * Slot: InformationContentEntity_id Description: Autocreated FK slot
--     * Slot: InformationResource_id Description: Autocreated FK slot
--     * Slot: ScientificKnowledgeCollection_id Description: Autocreated FK slot
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: ScientificKnowledgeItem_id Description: Autocreated FK slot
--     * Slot: ScientificKnowledgeFragment_id Description: Autocreated FK slot
--     * Slot: Note_id Description: Autocreated FK slot
-- # Class: "Organization" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A simple, locally-generated unique identifier specific with different heuristic formatting for each application.
--     * Slot: type Description: The type of an Entity expressed as curi.
-- # Class: "City" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A simple, locally-generated unique identifier specific with different heuristic formatting for each application.
--     * Slot: type Description: The type of an Entity expressed as curi.
-- # Class: "Country" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A simple, locally-generated unique identifier specific with different heuristic formatting for each application.
--     * Slot: type Description: The type of an Entity expressed as curi.
-- # Class: "Entity_iri" Description: ""
--     * Slot: Entity_id Description: Autocreated FK slot
--     * Slot: iri Description: An IRI for an entity. 
-- # Class: "NamedThing_iri" Description: ""
--     * Slot: NamedThing_id Description: Autocreated FK slot
--     * Slot: iri Description: An IRI for an entity. 
-- # Class: "InformationContentEntity_provenance" Description: ""
--     * Slot: InformationContentEntity_id Description: Autocreated FK slot
--     * Slot: provenance Description: A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.             
-- # Class: "InformationContentEntity_xref" Description: ""
--     * Slot: InformationContentEntity_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. 
-- # Class: "InformationContentEntity_has_notes" Description: ""
--     * Slot: InformationContentEntity_id Description: Autocreated FK slot
--     * Slot: has_notes_id Description: Points to notes that are about a given entity.
-- # Class: "InformationContentEntity_iri" Description: ""
--     * Slot: InformationContentEntity_id Description: Autocreated FK slot
--     * Slot: iri Description: An IRI for an entity. 
-- # Class: "InformationResource_provenance" Description: ""
--     * Slot: InformationResource_id Description: Autocreated FK slot
--     * Slot: provenance Description: A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.             
-- # Class: "InformationResource_xref" Description: ""
--     * Slot: InformationResource_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. 
-- # Class: "InformationResource_has_notes" Description: ""
--     * Slot: InformationResource_id Description: Autocreated FK slot
--     * Slot: has_notes_id Description: Points to notes that are about a given entity.
-- # Class: "InformationResource_iri" Description: ""
--     * Slot: InformationResource_id Description: Autocreated FK slot
--     * Slot: iri Description: An IRI for an entity. 
-- # Class: "ScientificKnowledgeCollection_has_members" Description: ""
--     * Slot: ScientificKnowledgeCollection_id Description: Autocreated FK slot
--     * Slot: has_members_id Description: holds between collections and their members
-- # Class: "ScientificKnowledgeCollection_provenance" Description: ""
--     * Slot: ScientificKnowledgeCollection_id Description: Autocreated FK slot
--     * Slot: provenance Description: A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.             
-- # Class: "ScientificKnowledgeCollection_xref" Description: ""
--     * Slot: ScientificKnowledgeCollection_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. 
-- # Class: "ScientificKnowledgeCollection_has_notes" Description: ""
--     * Slot: ScientificKnowledgeCollection_id Description: Autocreated FK slot
--     * Slot: has_notes_id Description: Points to notes that are about a given entity.
-- # Class: "ScientificKnowledgeCollection_iri" Description: ""
--     * Slot: ScientificKnowledgeCollection_id Description: Autocreated FK slot
--     * Slot: iri Description: An IRI for an entity. 
-- # Class: "ScientificKnowledgeExpression_has_representation" Description: ""
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: has_representation_id Description: holds between wholes and their parts (material entities or processes)
-- # Class: "ScientificKnowledgeExpression_member_of" Description: ""
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: member_of_id Description: holds between individuals and collections that they are members of
-- # Class: "ScientificKnowledgeExpression_provenance" Description: ""
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: provenance Description: A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.             
-- # Class: "ScientificKnowledgeExpression_xref" Description: ""
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. 
-- # Class: "ScientificKnowledgeExpression_has_notes" Description: ""
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: has_notes_id Description: Points to notes that are about a given entity.
-- # Class: "ScientificKnowledgeExpression_iri" Description: ""
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: iri Description: An IRI for an entity. 
-- # Class: "ScientificKnowledgeItem_has_part" Description: ""
--     * Slot: ScientificKnowledgeItem_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: holds between wholes and their parts (material entities or processes)
-- # Class: "ScientificKnowledgeItem_provenance" Description: ""
--     * Slot: ScientificKnowledgeItem_id Description: Autocreated FK slot
--     * Slot: provenance Description: A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.             
-- # Class: "ScientificKnowledgeItem_xref" Description: ""
--     * Slot: ScientificKnowledgeItem_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. 
-- # Class: "ScientificKnowledgeItem_has_notes" Description: ""
--     * Slot: ScientificKnowledgeItem_id Description: Autocreated FK slot
--     * Slot: has_notes_id Description: Points to notes that are about a given entity.
-- # Class: "ScientificKnowledgeItem_iri" Description: ""
--     * Slot: ScientificKnowledgeItem_id Description: Autocreated FK slot
--     * Slot: iri Description: An IRI for an entity. 
-- # Class: "ScientificKnowledgeFragment_provenance" Description: ""
--     * Slot: ScientificKnowledgeFragment_id Description: Autocreated FK slot
--     * Slot: provenance Description: A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.             
-- # Class: "ScientificKnowledgeFragment_xref" Description: ""
--     * Slot: ScientificKnowledgeFragment_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. 
-- # Class: "ScientificKnowledgeFragment_has_notes" Description: ""
--     * Slot: ScientificKnowledgeFragment_id Description: Autocreated FK slot
--     * Slot: has_notes_id Description: Points to notes that are about a given entity.
-- # Class: "ScientificKnowledgeFragment_iri" Description: ""
--     * Slot: ScientificKnowledgeFragment_id Description: Autocreated FK slot
--     * Slot: iri Description: An IRI for an entity. 
-- # Class: "Note_is_about" Description: ""
--     * Slot: Note_id Description: Autocreated FK slot
--     * Slot: is_about_id Description: A (currently) primitive relation that relates an information artifact to an entity. 
-- # Class: "Note_provenance" Description: ""
--     * Slot: Note_id Description: Autocreated FK slot
--     * Slot: provenance Description: A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.             
-- # Class: "Note_xref" Description: ""
--     * Slot: Note_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. 
-- # Class: "Note_has_notes" Description: ""
--     * Slot: Note_id Description: Autocreated FK slot
--     * Slot: has_notes_id Description: Points to notes that are about a given entity.
-- # Class: "Note_iri" Description: ""
--     * Slot: Note_id Description: Autocreated FK slot
--     * Slot: iri Description: An IRI for an entity. 
-- # Class: "Author_affiliations" Description: ""
--     * Slot: Author_id Description: Autocreated FK slot
--     * Slot: affiliations_id Description: The affiliations of an author. 
-- # Class: "Author_iri" Description: ""
--     * Slot: Author_id Description: Autocreated FK slot
--     * Slot: iri Description: An IRI for an entity. 
-- # Class: "Organization_city" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: city_id Description: 
-- # Class: "Organization_country" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: country_id Description: 
-- # Class: "Organization_iri" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: iri Description: An IRI for an entity. 
-- # Class: "City_iri" Description: ""
--     * Slot: City_id Description: Autocreated FK slot
--     * Slot: iri Description: An IRI for an entity. 
-- # Class: "Country_iri" Description: ""
--     * Slot: Country_id Description: Autocreated FK slot
--     * Slot: iri Description: An IRI for an entity. 

CREATE TABLE "Entity" (
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "NamedThing" (
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "InformationContentEntity" (
	creation_date DATE, 
	content TEXT, 
	format TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "InformationResource" (
	creation_date DATE, 
	content TEXT, 
	format TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificKnowledgeCollection" (
	creation_date DATE, 
	content TEXT, 
	format TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificKnowledgeExpression" (
	publication_date DATE, 
	type VARCHAR(33) NOT NULL, 
	creation_date DATE, 
	content TEXT, 
	format TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Note" (
	format TEXT, 
	type VARCHAR(19) NOT NULL, 
	creation_date DATE, 
	content TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Organization" (
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "City" (
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Country" (
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificKnowledgeItem" (
	representation_of TEXT, 
	creation_date DATE, 
	content TEXT, 
	format TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(representation_of) REFERENCES "ScientificKnowledgeExpression" (id)
);
CREATE TABLE "Entity_iri" (
	"Entity_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("Entity_id", iri), 
	FOREIGN KEY("Entity_id") REFERENCES "Entity" (id)
);
CREATE TABLE "NamedThing_iri" (
	"NamedThing_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("NamedThing_id", iri), 
	FOREIGN KEY("NamedThing_id") REFERENCES "NamedThing" (id)
);
CREATE TABLE "InformationContentEntity_provenance" (
	"InformationContentEntity_id" TEXT, 
	provenance TEXT, 
	PRIMARY KEY ("InformationContentEntity_id", provenance), 
	FOREIGN KEY("InformationContentEntity_id") REFERENCES "InformationContentEntity" (id)
);
CREATE TABLE "InformationContentEntity_xref" (
	"InformationContentEntity_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("InformationContentEntity_id", xref), 
	FOREIGN KEY("InformationContentEntity_id") REFERENCES "InformationContentEntity" (id)
);
CREATE TABLE "InformationContentEntity_has_notes" (
	"InformationContentEntity_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("InformationContentEntity_id", has_notes_id), 
	FOREIGN KEY("InformationContentEntity_id") REFERENCES "InformationContentEntity" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "InformationContentEntity_iri" (
	"InformationContentEntity_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("InformationContentEntity_id", iri), 
	FOREIGN KEY("InformationContentEntity_id") REFERENCES "InformationContentEntity" (id)
);
CREATE TABLE "InformationResource_provenance" (
	"InformationResource_id" TEXT, 
	provenance TEXT, 
	PRIMARY KEY ("InformationResource_id", provenance), 
	FOREIGN KEY("InformationResource_id") REFERENCES "InformationResource" (id)
);
CREATE TABLE "InformationResource_xref" (
	"InformationResource_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("InformationResource_id", xref), 
	FOREIGN KEY("InformationResource_id") REFERENCES "InformationResource" (id)
);
CREATE TABLE "InformationResource_has_notes" (
	"InformationResource_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("InformationResource_id", has_notes_id), 
	FOREIGN KEY("InformationResource_id") REFERENCES "InformationResource" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "InformationResource_iri" (
	"InformationResource_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("InformationResource_id", iri), 
	FOREIGN KEY("InformationResource_id") REFERENCES "InformationResource" (id)
);
CREATE TABLE "ScientificKnowledgeCollection_has_members" (
	"ScientificKnowledgeCollection_id" TEXT, 
	has_members_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", has_members_id), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id), 
	FOREIGN KEY(has_members_id) REFERENCES "ScientificKnowledgeExpression" (id)
);
CREATE TABLE "ScientificKnowledgeCollection_provenance" (
	"ScientificKnowledgeCollection_id" TEXT, 
	provenance TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", provenance), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id)
);
CREATE TABLE "ScientificKnowledgeCollection_xref" (
	"ScientificKnowledgeCollection_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", xref), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id)
);
CREATE TABLE "ScientificKnowledgeCollection_has_notes" (
	"ScientificKnowledgeCollection_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", has_notes_id), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "ScientificKnowledgeCollection_iri" (
	"ScientificKnowledgeCollection_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", iri), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id)
);
CREATE TABLE "ScientificKnowledgeExpression_member_of" (
	"ScientificKnowledgeExpression_id" TEXT, 
	member_of_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", member_of_id), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY(member_of_id) REFERENCES "ScientificKnowledgeCollection" (id)
);
CREATE TABLE "ScientificKnowledgeExpression_provenance" (
	"ScientificKnowledgeExpression_id" TEXT, 
	provenance TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", provenance), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id)
);
CREATE TABLE "ScientificKnowledgeExpression_xref" (
	"ScientificKnowledgeExpression_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", xref), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id)
);
CREATE TABLE "ScientificKnowledgeExpression_has_notes" (
	"ScientificKnowledgeExpression_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", has_notes_id), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "ScientificKnowledgeExpression_iri" (
	"ScientificKnowledgeExpression_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", iri), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id)
);
CREATE TABLE "Note_is_about" (
	"Note_id" TEXT, 
	is_about_id TEXT, 
	PRIMARY KEY ("Note_id", is_about_id), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id), 
	FOREIGN KEY(is_about_id) REFERENCES "InformationContentEntity" (id)
);
CREATE TABLE "Note_provenance" (
	"Note_id" TEXT, 
	provenance TEXT, 
	PRIMARY KEY ("Note_id", provenance), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id)
);
CREATE TABLE "Note_xref" (
	"Note_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("Note_id", xref), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id)
);
CREATE TABLE "Note_has_notes" (
	"Note_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("Note_id", has_notes_id), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "Note_iri" (
	"Note_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("Note_id", iri), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id)
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
CREATE TABLE "Organization_iri" (
	"Organization_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("Organization_id", iri), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE TABLE "City_iri" (
	"City_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("City_id", iri), 
	FOREIGN KEY("City_id") REFERENCES "City" (id)
);
CREATE TABLE "Country_iri" (
	"Country_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("Country_id", iri), 
	FOREIGN KEY("Country_id") REFERENCES "Country" (id)
);
CREATE TABLE "ScientificKnowledgeFragment" (
	part_of TEXT, 
	"offset" INTEGER, 
	length INTEGER, 
	creation_date DATE, 
	content TEXT, 
	format TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(part_of) REFERENCES "ScientificKnowledgeItem" (id)
);
CREATE TABLE "ScientificKnowledgeExpression_has_representation" (
	"ScientificKnowledgeExpression_id" TEXT, 
	has_representation_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", has_representation_id), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY(has_representation_id) REFERENCES "ScientificKnowledgeItem" (id)
);
CREATE TABLE "ScientificKnowledgeItem_provenance" (
	"ScientificKnowledgeItem_id" TEXT, 
	provenance TEXT, 
	PRIMARY KEY ("ScientificKnowledgeItem_id", provenance), 
	FOREIGN KEY("ScientificKnowledgeItem_id") REFERENCES "ScientificKnowledgeItem" (id)
);
CREATE TABLE "ScientificKnowledgeItem_xref" (
	"ScientificKnowledgeItem_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificKnowledgeItem_id", xref), 
	FOREIGN KEY("ScientificKnowledgeItem_id") REFERENCES "ScientificKnowledgeItem" (id)
);
CREATE TABLE "ScientificKnowledgeItem_has_notes" (
	"ScientificKnowledgeItem_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeItem_id", has_notes_id), 
	FOREIGN KEY("ScientificKnowledgeItem_id") REFERENCES "ScientificKnowledgeItem" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "ScientificKnowledgeItem_iri" (
	"ScientificKnowledgeItem_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("ScientificKnowledgeItem_id", iri), 
	FOREIGN KEY("ScientificKnowledgeItem_id") REFERENCES "ScientificKnowledgeItem" (id)
);
CREATE TABLE "Author" (
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	"InformationContentEntity_id" TEXT, 
	"InformationResource_id" TEXT, 
	"ScientificKnowledgeCollection_id" TEXT, 
	"ScientificKnowledgeExpression_id" TEXT, 
	"ScientificKnowledgeItem_id" TEXT, 
	"ScientificKnowledgeFragment_id" TEXT, 
	"Note_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("InformationContentEntity_id") REFERENCES "InformationContentEntity" (id), 
	FOREIGN KEY("InformationResource_id") REFERENCES "InformationResource" (id), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY("ScientificKnowledgeItem_id") REFERENCES "ScientificKnowledgeItem" (id), 
	FOREIGN KEY("ScientificKnowledgeFragment_id") REFERENCES "ScientificKnowledgeFragment" (id), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id)
);
CREATE TABLE "ScientificKnowledgeItem_has_part" (
	"ScientificKnowledgeItem_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeItem_id", has_part_id), 
	FOREIGN KEY("ScientificKnowledgeItem_id") REFERENCES "ScientificKnowledgeItem" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "ScientificKnowledgeFragment_provenance" (
	"ScientificKnowledgeFragment_id" TEXT, 
	provenance TEXT, 
	PRIMARY KEY ("ScientificKnowledgeFragment_id", provenance), 
	FOREIGN KEY("ScientificKnowledgeFragment_id") REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "ScientificKnowledgeFragment_xref" (
	"ScientificKnowledgeFragment_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificKnowledgeFragment_id", xref), 
	FOREIGN KEY("ScientificKnowledgeFragment_id") REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "ScientificKnowledgeFragment_has_notes" (
	"ScientificKnowledgeFragment_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeFragment_id", has_notes_id), 
	FOREIGN KEY("ScientificKnowledgeFragment_id") REFERENCES "ScientificKnowledgeFragment" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);
CREATE TABLE "ScientificKnowledgeFragment_iri" (
	"ScientificKnowledgeFragment_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("ScientificKnowledgeFragment_id", iri), 
	FOREIGN KEY("ScientificKnowledgeFragment_id") REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "Author_affiliations" (
	"Author_id" TEXT, 
	affiliations_id TEXT, 
	PRIMARY KEY ("Author_id", affiliations_id), 
	FOREIGN KEY("Author_id") REFERENCES "Author" (id), 
	FOREIGN KEY(affiliations_id) REFERENCES "Organization" (id)
);
CREATE TABLE "Author_iri" (
	"Author_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("Author_id", iri), 
	FOREIGN KEY("Author_id") REFERENCES "Author" (id)
);
