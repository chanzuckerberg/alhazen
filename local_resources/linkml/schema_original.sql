
CREATE TABLE "Entity" (
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Entity" IS 'Root Model class for all things and informational relationships, real or imagined.';COMMENT ON COLUMN "Entity".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';COMMENT ON COLUMN "Entity".type IS 'The type of an Entity expressed as curi.';
CREATE TABLE "NamedThing" (
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "NamedThing" IS 'an entity or concept/class described by a name';COMMENT ON COLUMN "NamedThing".name IS 'A human-readable name for an attribute or entity.';COMMENT ON COLUMN "NamedThing".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';COMMENT ON COLUMN "NamedThing".type IS 'The type of an Entity expressed as curi.';
CREATE TABLE "InformationContentEntity" (
	creation_date DATE, 
	content TEXT, 
	token_count INTEGER, 
	format TEXT, 
	provenance TEXT, 
	license TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "InformationContentEntity" IS 'A piece of information that is represented in the typically describes some topic of discourse or is used as support.
';COMMENT ON COLUMN "InformationContentEntity".creation_date IS 'date on which an entity was created. This can be applied to nodes or edges';COMMENT ON COLUMN "InformationContentEntity".content IS 'The content of an InformationContentEntity expressed as a string.';COMMENT ON COLUMN "InformationContentEntity".token_count IS 'The number of tokens in the content of an InformationContentEntity.';COMMENT ON COLUMN "InformationContentEntity".format IS 'The format (JSON, XML, BINARY) of the content of an InformationContentEntity.';COMMENT ON COLUMN "InformationContentEntity".provenance IS 'A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.  ';COMMENT ON COLUMN "InformationContentEntity".license IS 'A license under which an information content entity is provided.';COMMENT ON COLUMN "InformationContentEntity".name IS 'A human-readable name for an attribute or entity.';COMMENT ON COLUMN "InformationContentEntity".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';COMMENT ON COLUMN "InformationContentEntity".type IS 'The type of an Entity expressed as curi.';
CREATE TABLE "UserQuestion" (
	creation_date DATE, 
	content TEXT, 
	token_count INTEGER, 
	format TEXT, 
	provenance TEXT, 
	license TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "UserQuestion" IS 'A question, inquiry, or instruction from an user of the Alhazen system.
';COMMENT ON COLUMN "UserQuestion".creation_date IS 'date on which an entity was created. This can be applied to nodes or edges';COMMENT ON COLUMN "UserQuestion".content IS 'The content of an InformationContentEntity expressed as a string.';COMMENT ON COLUMN "UserQuestion".token_count IS 'The number of tokens in the content of an InformationContentEntity.';COMMENT ON COLUMN "UserQuestion".format IS 'The format (JSON, XML, BINARY) of the content of an InformationContentEntity.';COMMENT ON COLUMN "UserQuestion".provenance IS 'A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.  ';COMMENT ON COLUMN "UserQuestion".license IS 'A license under which an information content entity is provided.';COMMENT ON COLUMN "UserQuestion".name IS 'A human-readable name for an attribute or entity.';COMMENT ON COLUMN "UserQuestion".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';COMMENT ON COLUMN "UserQuestion".type IS 'The type of an Entity expressed as curi.';
CREATE TABLE "InformationResource" (
	creation_date DATE, 
	content TEXT, 
	token_count INTEGER, 
	format TEXT, 
	provenance TEXT, 
	license TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "InformationResource" IS 'A database or knowledgebase and its supporting ecosystem of interfaces and services that deliver content to consumers (e.g. web portals, APIs, query endpoints, streaming services, data downloads, etc.). A single Information Resource by this definition may span many different datasets or databases, and include many access endpoints and user interfaces. Information Resources include project-specific resources such as a Translator Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb.';COMMENT ON COLUMN "InformationResource".creation_date IS 'date on which an entity was created. This can be applied to nodes or edges';COMMENT ON COLUMN "InformationResource".content IS 'The content of an InformationContentEntity expressed as a string.';COMMENT ON COLUMN "InformationResource".token_count IS 'The number of tokens in the content of an InformationContentEntity.';COMMENT ON COLUMN "InformationResource".format IS 'The format (JSON, XML, BINARY) of the content of an InformationContentEntity.';COMMENT ON COLUMN "InformationResource".provenance IS 'A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.  ';COMMENT ON COLUMN "InformationResource".license IS 'A license under which an information content entity is provided.';COMMENT ON COLUMN "InformationResource".name IS 'A human-readable name for an attribute or entity.';COMMENT ON COLUMN "InformationResource".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';COMMENT ON COLUMN "InformationResource".type IS 'The type of an Entity expressed as curi.';
CREATE TABLE "ScientificKnowledgeCollection" (
	creation_date DATE, 
	content TEXT, 
	token_count INTEGER, 
	format TEXT, 
	provenance TEXT, 
	license TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "ScientificKnowledgeCollection" IS 'A collection of expressions of scientific knowledge.';COMMENT ON COLUMN "ScientificKnowledgeCollection".creation_date IS 'date on which an entity was created. This can be applied to nodes or edges';COMMENT ON COLUMN "ScientificKnowledgeCollection".content IS 'The content of an InformationContentEntity expressed as a string.';COMMENT ON COLUMN "ScientificKnowledgeCollection".token_count IS 'The number of tokens in the content of an InformationContentEntity.';COMMENT ON COLUMN "ScientificKnowledgeCollection".format IS 'The format (JSON, XML, BINARY) of the content of an InformationContentEntity.';COMMENT ON COLUMN "ScientificKnowledgeCollection".provenance IS 'A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.  ';COMMENT ON COLUMN "ScientificKnowledgeCollection".license IS 'A license under which an information content entity is provided.';COMMENT ON COLUMN "ScientificKnowledgeCollection".name IS 'A human-readable name for an attribute or entity.';COMMENT ON COLUMN "ScientificKnowledgeCollection".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';COMMENT ON COLUMN "ScientificKnowledgeCollection".type IS 'The type of an Entity expressed as curi.';
CREATE TABLE "ScientificKnowledgeExpression" (
	publication_date DATE, 
	type TEXT NOT NULL, 
	creation_date DATE, 
	content TEXT, 
	token_count INTEGER, 
	format TEXT, 
	provenance TEXT, 
	license TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "ScientificKnowledgeExpression" IS 'Any expression of scientific knowledge.   ';COMMENT ON COLUMN "ScientificKnowledgeExpression".publication_date IS 'date on which an entity was published (i.e., made available to the public).';COMMENT ON COLUMN "ScientificKnowledgeExpression".type IS 'The type of an Entity expressed as curi.';COMMENT ON COLUMN "ScientificKnowledgeExpression".creation_date IS 'date on which an entity was created. This can be applied to nodes or edges';COMMENT ON COLUMN "ScientificKnowledgeExpression".content IS 'The content of an InformationContentEntity expressed as a string.';COMMENT ON COLUMN "ScientificKnowledgeExpression".token_count IS 'The number of tokens in the content of an InformationContentEntity.';COMMENT ON COLUMN "ScientificKnowledgeExpression".format IS 'The format (JSON, XML, BINARY) of the content of an InformationContentEntity.';COMMENT ON COLUMN "ScientificKnowledgeExpression".provenance IS 'A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.  ';COMMENT ON COLUMN "ScientificKnowledgeExpression".license IS 'A license under which an information content entity is provided.';COMMENT ON COLUMN "ScientificKnowledgeExpression".name IS 'A human-readable name for an attribute or entity.';COMMENT ON COLUMN "ScientificKnowledgeExpression".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';
CREATE TABLE "Note" (
	format TEXT, 
	type TEXT NOT NULL, 
	creation_date DATE, 
	content TEXT, 
	token_count INTEGER, 
	provenance TEXT, 
	license TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Note" IS 'A structured piece of information with an author that is about another InformationContentEntity.';COMMENT ON COLUMN "Note".format IS 'The format (JSON, XML, BINARY) of the content of an InformationContentEntity.';COMMENT ON COLUMN "Note".type IS 'The type of an Entity expressed as curi.';COMMENT ON COLUMN "Note".creation_date IS 'date on which an entity was created. This can be applied to nodes or edges';COMMENT ON COLUMN "Note".content IS 'The content of an InformationContentEntity expressed as a string.';COMMENT ON COLUMN "Note".token_count IS 'The number of tokens in the content of an InformationContentEntity.';COMMENT ON COLUMN "Note".provenance IS 'A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.  ';COMMENT ON COLUMN "Note".license IS 'A license under which an information content entity is provided.';COMMENT ON COLUMN "Note".name IS 'A human-readable name for an attribute or entity.';COMMENT ON COLUMN "Note".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';
CREATE TABLE "Author" (
	creation_date DATE, 
	content TEXT, 
	token_count INTEGER, 
	format TEXT, 
	provenance TEXT, 
	license TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Author" IS 'None';COMMENT ON COLUMN "Author".creation_date IS 'date on which an entity was created. This can be applied to nodes or edges';COMMENT ON COLUMN "Author".content IS 'The content of an InformationContentEntity expressed as a string.';COMMENT ON COLUMN "Author".token_count IS 'The number of tokens in the content of an InformationContentEntity.';COMMENT ON COLUMN "Author".format IS 'The format (JSON, XML, BINARY) of the content of an InformationContentEntity.';COMMENT ON COLUMN "Author".provenance IS 'A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.  ';COMMENT ON COLUMN "Author".license IS 'A license under which an information content entity is provided.';COMMENT ON COLUMN "Author".name IS 'A human-readable name for an attribute or entity.';COMMENT ON COLUMN "Author".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';COMMENT ON COLUMN "Author".type IS 'The type of an Entity expressed as curi.';
CREATE TABLE "Organization" (
	creation_date DATE, 
	content TEXT, 
	token_count INTEGER, 
	format TEXT, 
	provenance TEXT, 
	license TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Organization" IS 'None';COMMENT ON COLUMN "Organization".creation_date IS 'date on which an entity was created. This can be applied to nodes or edges';COMMENT ON COLUMN "Organization".content IS 'The content of an InformationContentEntity expressed as a string.';COMMENT ON COLUMN "Organization".token_count IS 'The number of tokens in the content of an InformationContentEntity.';COMMENT ON COLUMN "Organization".format IS 'The format (JSON, XML, BINARY) of the content of an InformationContentEntity.';COMMENT ON COLUMN "Organization".provenance IS 'A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.  ';COMMENT ON COLUMN "Organization".license IS 'A license under which an information content entity is provided.';COMMENT ON COLUMN "Organization".name IS 'A human-readable name for an attribute or entity.';COMMENT ON COLUMN "Organization".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';COMMENT ON COLUMN "Organization".type IS 'The type of an Entity expressed as curi.';
CREATE TABLE "City" (
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "City" IS 'None';COMMENT ON COLUMN "City".name IS 'A human-readable name for an attribute or entity.';COMMENT ON COLUMN "City".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';COMMENT ON COLUMN "City".type IS 'The type of an Entity expressed as curi.';
CREATE TABLE "Country" (
	code2 TEXT, 
	code3 TEXT, 
	region TEXT, 
	income TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);COMMENT ON TABLE "Country" IS 'None';COMMENT ON COLUMN "Country".name IS 'A human-readable name for an attribute or entity.';COMMENT ON COLUMN "Country".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';COMMENT ON COLUMN "Country".type IS 'The type of an Entity expressed as curi.';
CREATE TABLE "ScientificKnowledgeItem" (
	representation_of TEXT, 
	creation_date DATE, 
	content TEXT, 
	token_count INTEGER, 
	format TEXT, 
	provenance TEXT, 
	license TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(representation_of) REFERENCES "ScientificKnowledgeExpression" (id)
);COMMENT ON TABLE "ScientificKnowledgeItem" IS 'A specific instance of a ScientificKnowledgeExpression:- our internal representation of an EPMC citation record, a local copy of a full-text article. This is the substrate that forms the basis for a ScientificKnowledgeFragment.';COMMENT ON COLUMN "ScientificKnowledgeItem".representation_of IS 'The ScientificKnowledgeExpression that this ScientificKnowledgeItem  is a representation of.';COMMENT ON COLUMN "ScientificKnowledgeItem".creation_date IS 'date on which an entity was created. This can be applied to nodes or edges';COMMENT ON COLUMN "ScientificKnowledgeItem".content IS 'The content of an InformationContentEntity expressed as a string.';COMMENT ON COLUMN "ScientificKnowledgeItem".token_count IS 'The number of tokens in the content of an InformationContentEntity.';COMMENT ON COLUMN "ScientificKnowledgeItem".format IS 'The format (JSON, XML, BINARY) of the content of an InformationContentEntity.';COMMENT ON COLUMN "ScientificKnowledgeItem".provenance IS 'A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.  ';COMMENT ON COLUMN "ScientificKnowledgeItem".license IS 'A license under which an information content entity is provided.';COMMENT ON COLUMN "ScientificKnowledgeItem".name IS 'A human-readable name for an attribute or entity.';COMMENT ON COLUMN "ScientificKnowledgeItem".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';COMMENT ON COLUMN "ScientificKnowledgeItem".type IS 'The type of an Entity expressed as curi.';
CREATE TABLE "Entity_iri" (
	"Entity_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("Entity_id", iri), 
	FOREIGN KEY("Entity_id") REFERENCES "Entity" (id)
);COMMENT ON TABLE "Entity_iri" IS 'None';COMMENT ON COLUMN "Entity_iri"."Entity_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Entity_iri".iri IS 'An IRI for an entity. ';
CREATE TABLE "NamedThing_iri" (
	"NamedThing_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("NamedThing_id", iri), 
	FOREIGN KEY("NamedThing_id") REFERENCES "NamedThing" (id)
);COMMENT ON TABLE "NamedThing_iri" IS 'None';COMMENT ON COLUMN "NamedThing_iri"."NamedThing_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "NamedThing_iri".iri IS 'An IRI for an entity. ';
CREATE TABLE "InformationContentEntity_xref" (
	"InformationContentEntity_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("InformationContentEntity_id", xref), 
	FOREIGN KEY("InformationContentEntity_id") REFERENCES "InformationContentEntity" (id)
);COMMENT ON TABLE "InformationContentEntity_xref" IS 'None';COMMENT ON COLUMN "InformationContentEntity_xref"."InformationContentEntity_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "InformationContentEntity_xref".xref IS 'A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. ';
CREATE TABLE "InformationContentEntity_has_notes" (
	"InformationContentEntity_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("InformationContentEntity_id", has_notes_id), 
	FOREIGN KEY("InformationContentEntity_id") REFERENCES "InformationContentEntity" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);COMMENT ON TABLE "InformationContentEntity_has_notes" IS 'None';COMMENT ON COLUMN "InformationContentEntity_has_notes"."InformationContentEntity_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "InformationContentEntity_has_notes".has_notes_id IS 'Points to notes that are about a given entity.';
CREATE TABLE "InformationContentEntity_iri" (
	"InformationContentEntity_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("InformationContentEntity_id", iri), 
	FOREIGN KEY("InformationContentEntity_id") REFERENCES "InformationContentEntity" (id)
);COMMENT ON TABLE "InformationContentEntity_iri" IS 'None';COMMENT ON COLUMN "InformationContentEntity_iri"."InformationContentEntity_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "InformationContentEntity_iri".iri IS 'An IRI for an entity. ';
CREATE TABLE "UserQuestion_xref" (
	"UserQuestion_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("UserQuestion_id", xref), 
	FOREIGN KEY("UserQuestion_id") REFERENCES "UserQuestion" (id)
);COMMENT ON TABLE "UserQuestion_xref" IS 'None';COMMENT ON COLUMN "UserQuestion_xref"."UserQuestion_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "UserQuestion_xref".xref IS 'A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. ';
CREATE TABLE "UserQuestion_has_notes" (
	"UserQuestion_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("UserQuestion_id", has_notes_id), 
	FOREIGN KEY("UserQuestion_id") REFERENCES "UserQuestion" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);COMMENT ON TABLE "UserQuestion_has_notes" IS 'None';COMMENT ON COLUMN "UserQuestion_has_notes"."UserQuestion_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "UserQuestion_has_notes".has_notes_id IS 'Points to notes that are about a given entity.';
CREATE TABLE "UserQuestion_iri" (
	"UserQuestion_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("UserQuestion_id", iri), 
	FOREIGN KEY("UserQuestion_id") REFERENCES "UserQuestion" (id)
);COMMENT ON TABLE "UserQuestion_iri" IS 'None';COMMENT ON COLUMN "UserQuestion_iri"."UserQuestion_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "UserQuestion_iri".iri IS 'An IRI for an entity. ';
CREATE TABLE "InformationResource_xref" (
	"InformationResource_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("InformationResource_id", xref), 
	FOREIGN KEY("InformationResource_id") REFERENCES "InformationResource" (id)
);COMMENT ON TABLE "InformationResource_xref" IS 'None';COMMENT ON COLUMN "InformationResource_xref"."InformationResource_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "InformationResource_xref".xref IS 'A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. ';
CREATE TABLE "InformationResource_has_notes" (
	"InformationResource_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("InformationResource_id", has_notes_id), 
	FOREIGN KEY("InformationResource_id") REFERENCES "InformationResource" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);COMMENT ON TABLE "InformationResource_has_notes" IS 'None';COMMENT ON COLUMN "InformationResource_has_notes"."InformationResource_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "InformationResource_has_notes".has_notes_id IS 'Points to notes that are about a given entity.';
CREATE TABLE "InformationResource_iri" (
	"InformationResource_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("InformationResource_id", iri), 
	FOREIGN KEY("InformationResource_id") REFERENCES "InformationResource" (id)
);COMMENT ON TABLE "InformationResource_iri" IS 'None';COMMENT ON COLUMN "InformationResource_iri"."InformationResource_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "InformationResource_iri".iri IS 'An IRI for an entity. ';
CREATE TABLE "ScientificKnowledgeCollection_has_members" (
	"ScientificKnowledgeCollection_id" TEXT, 
	has_members_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", has_members_id), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id), 
	FOREIGN KEY(has_members_id) REFERENCES "ScientificKnowledgeExpression" (id)
);COMMENT ON TABLE "ScientificKnowledgeCollection_has_members" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeCollection_has_members"."ScientificKnowledgeCollection_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeCollection_has_members".has_members_id IS 'holds between collections and their members';
CREATE TABLE "ScientificKnowledgeCollection_xref" (
	"ScientificKnowledgeCollection_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", xref), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id)
);COMMENT ON TABLE "ScientificKnowledgeCollection_xref" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeCollection_xref"."ScientificKnowledgeCollection_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeCollection_xref".xref IS 'A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. ';
CREATE TABLE "ScientificKnowledgeCollection_has_notes" (
	"ScientificKnowledgeCollection_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", has_notes_id), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);COMMENT ON TABLE "ScientificKnowledgeCollection_has_notes" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeCollection_has_notes"."ScientificKnowledgeCollection_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeCollection_has_notes".has_notes_id IS 'Points to notes that are about a given entity.';
CREATE TABLE "ScientificKnowledgeCollection_iri" (
	"ScientificKnowledgeCollection_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", iri), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id)
);COMMENT ON TABLE "ScientificKnowledgeCollection_iri" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeCollection_iri"."ScientificKnowledgeCollection_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeCollection_iri".iri IS 'An IRI for an entity. ';
CREATE TABLE "ScientificKnowledgeExpression_member_of" (
	"ScientificKnowledgeExpression_id" TEXT, 
	member_of_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", member_of_id), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY(member_of_id) REFERENCES "ScientificKnowledgeCollection" (id)
);COMMENT ON TABLE "ScientificKnowledgeExpression_member_of" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeExpression_member_of"."ScientificKnowledgeExpression_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeExpression_member_of".member_of_id IS 'holds between individuals and collections that they are members of';
CREATE TABLE "ScientificKnowledgeExpression_has_authors" (
	"ScientificKnowledgeExpression_id" TEXT, 
	has_authors_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", has_authors_id), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY(has_authors_id) REFERENCES "Author" (id)
);COMMENT ON TABLE "ScientificKnowledgeExpression_has_authors" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeExpression_has_authors"."ScientificKnowledgeExpression_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeExpression_has_authors".has_authors_id IS 'The named entity that authored an ScientificKnowledgeExpression. ';
CREATE TABLE "ScientificKnowledgeExpression_xref" (
	"ScientificKnowledgeExpression_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", xref), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id)
);COMMENT ON TABLE "ScientificKnowledgeExpression_xref" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeExpression_xref"."ScientificKnowledgeExpression_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeExpression_xref".xref IS 'A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. ';
CREATE TABLE "ScientificKnowledgeExpression_has_notes" (
	"ScientificKnowledgeExpression_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", has_notes_id), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);COMMENT ON TABLE "ScientificKnowledgeExpression_has_notes" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeExpression_has_notes"."ScientificKnowledgeExpression_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeExpression_has_notes".has_notes_id IS 'Points to notes that are about a given entity.';
CREATE TABLE "ScientificKnowledgeExpression_iri" (
	"ScientificKnowledgeExpression_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", iri), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id)
);COMMENT ON TABLE "ScientificKnowledgeExpression_iri" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeExpression_iri"."ScientificKnowledgeExpression_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeExpression_iri".iri IS 'An IRI for an entity. ';
CREATE TABLE "Note_is_about" (
	"Note_id" TEXT, 
	is_about_id TEXT, 
	PRIMARY KEY ("Note_id", is_about_id), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id), 
	FOREIGN KEY(is_about_id) REFERENCES "InformationContentEntity" (id)
);COMMENT ON TABLE "Note_is_about" IS 'None';COMMENT ON COLUMN "Note_is_about"."Note_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Note_is_about".is_about_id IS 'A (currently) primitive relation that relates an information artifact to an entity. ';
CREATE TABLE "Note_xref" (
	"Note_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("Note_id", xref), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id)
);COMMENT ON TABLE "Note_xref" IS 'None';COMMENT ON COLUMN "Note_xref"."Note_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Note_xref".xref IS 'A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. ';
CREATE TABLE "Note_has_notes" (
	"Note_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("Note_id", has_notes_id), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);COMMENT ON TABLE "Note_has_notes" IS 'None';COMMENT ON COLUMN "Note_has_notes"."Note_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Note_has_notes".has_notes_id IS 'Points to notes that are about a given entity.';
CREATE TABLE "Note_iri" (
	"Note_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("Note_id", iri), 
	FOREIGN KEY("Note_id") REFERENCES "Note" (id)
);COMMENT ON TABLE "Note_iri" IS 'None';COMMENT ON COLUMN "Note_iri"."Note_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Note_iri".iri IS 'An IRI for an entity. ';
CREATE TABLE "Author_affiliations" (
	"Author_id" TEXT, 
	affiliations_id TEXT, 
	PRIMARY KEY ("Author_id", affiliations_id), 
	FOREIGN KEY("Author_id") REFERENCES "Author" (id), 
	FOREIGN KEY(affiliations_id) REFERENCES "Organization" (id)
);COMMENT ON TABLE "Author_affiliations" IS 'None';COMMENT ON COLUMN "Author_affiliations"."Author_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Author_affiliations".affiliations_id IS 'The affiliations of an author. ';
CREATE TABLE "Author_is_author_of" (
	"Author_id" TEXT, 
	is_author_of_id TEXT, 
	PRIMARY KEY ("Author_id", is_author_of_id), 
	FOREIGN KEY("Author_id") REFERENCES "Author" (id), 
	FOREIGN KEY(is_author_of_id) REFERENCES "ScientificKnowledgeExpression" (id)
);COMMENT ON TABLE "Author_is_author_of" IS 'None';COMMENT ON COLUMN "Author_is_author_of"."Author_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Author_is_author_of".is_author_of_id IS 'The ScientificKnowledgeExpression that an Author is the author of. ';
CREATE TABLE "Author_xref" (
	"Author_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("Author_id", xref), 
	FOREIGN KEY("Author_id") REFERENCES "Author" (id)
);COMMENT ON TABLE "Author_xref" IS 'None';COMMENT ON COLUMN "Author_xref"."Author_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Author_xref".xref IS 'A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. ';
CREATE TABLE "Author_has_notes" (
	"Author_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("Author_id", has_notes_id), 
	FOREIGN KEY("Author_id") REFERENCES "Author" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);COMMENT ON TABLE "Author_has_notes" IS 'None';COMMENT ON COLUMN "Author_has_notes"."Author_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Author_has_notes".has_notes_id IS 'Points to notes that are about a given entity.';
CREATE TABLE "Author_iri" (
	"Author_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("Author_id", iri), 
	FOREIGN KEY("Author_id") REFERENCES "Author" (id)
);COMMENT ON TABLE "Author_iri" IS 'None';COMMENT ON COLUMN "Author_iri"."Author_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Author_iri".iri IS 'An IRI for an entity. ';
CREATE TABLE "Organization_city" (
	"Organization_id" TEXT, 
	city_id TEXT, 
	PRIMARY KEY ("Organization_id", city_id), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id), 
	FOREIGN KEY(city_id) REFERENCES "City" (id)
);COMMENT ON TABLE "Organization_city" IS 'None';COMMENT ON COLUMN "Organization_city"."Organization_id" IS 'Autocreated FK slot';
CREATE TABLE "Organization_country" (
	"Organization_id" TEXT, 
	country_id TEXT, 
	PRIMARY KEY ("Organization_id", country_id), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id), 
	FOREIGN KEY(country_id) REFERENCES "Country" (id)
);COMMENT ON TABLE "Organization_country" IS 'None';COMMENT ON COLUMN "Organization_country"."Organization_id" IS 'Autocreated FK slot';
CREATE TABLE "Organization_xref" (
	"Organization_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("Organization_id", xref), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);COMMENT ON TABLE "Organization_xref" IS 'None';COMMENT ON COLUMN "Organization_xref"."Organization_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Organization_xref".xref IS 'A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. ';
CREATE TABLE "Organization_has_notes" (
	"Organization_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("Organization_id", has_notes_id), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);COMMENT ON TABLE "Organization_has_notes" IS 'None';COMMENT ON COLUMN "Organization_has_notes"."Organization_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Organization_has_notes".has_notes_id IS 'Points to notes that are about a given entity.';
CREATE TABLE "Organization_iri" (
	"Organization_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("Organization_id", iri), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);COMMENT ON TABLE "Organization_iri" IS 'None';COMMENT ON COLUMN "Organization_iri"."Organization_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Organization_iri".iri IS 'An IRI for an entity. ';
CREATE TABLE "City_iri" (
	"City_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("City_id", iri), 
	FOREIGN KEY("City_id") REFERENCES "City" (id)
);COMMENT ON TABLE "City_iri" IS 'None';COMMENT ON COLUMN "City_iri"."City_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "City_iri".iri IS 'An IRI for an entity. ';
CREATE TABLE "Country_iri" (
	"Country_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("Country_id", iri), 
	FOREIGN KEY("Country_id") REFERENCES "Country" (id)
);COMMENT ON TABLE "Country_iri" IS 'None';COMMENT ON COLUMN "Country_iri"."Country_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "Country_iri".iri IS 'An IRI for an entity. ';
CREATE TABLE "ScientificKnowledgeFragment" (
	part_of TEXT, 
	"offset" INTEGER, 
	length INTEGER, 
	creation_date DATE, 
	content TEXT, 
	token_count INTEGER, 
	format TEXT, 
	provenance TEXT, 
	license TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(part_of) REFERENCES "ScientificKnowledgeItem" (id)
);COMMENT ON TABLE "ScientificKnowledgeFragment" IS 'A selected subportion of the contents of a ScientificKnowledgeExpression, described by an selector.';COMMENT ON COLUMN "ScientificKnowledgeFragment".part_of IS 'holds between parts and wholes (material entities or processes)';COMMENT ON COLUMN "ScientificKnowledgeFragment"."offset" IS 'The offset of the start of the fragment from the start of the text.';COMMENT ON COLUMN "ScientificKnowledgeFragment".length IS 'The length of the fragment.';COMMENT ON COLUMN "ScientificKnowledgeFragment".creation_date IS 'date on which an entity was created. This can be applied to nodes or edges';COMMENT ON COLUMN "ScientificKnowledgeFragment".content IS 'The content of an InformationContentEntity expressed as a string.';COMMENT ON COLUMN "ScientificKnowledgeFragment".token_count IS 'The number of tokens in the content of an InformationContentEntity.';COMMENT ON COLUMN "ScientificKnowledgeFragment".format IS 'The format (JSON, XML, BINARY) of the content of an InformationContentEntity.';COMMENT ON COLUMN "ScientificKnowledgeFragment".provenance IS 'A description of the provenance of an information content entity. Expressed as a list of commands describing how the collection was built. This should involve describing the operation to generate the collection in  sufficient detail that that could be replicated by an LLM agent with  the appropriate tooling.  ';COMMENT ON COLUMN "ScientificKnowledgeFragment".license IS 'A license under which an information content entity is provided.';COMMENT ON COLUMN "ScientificKnowledgeFragment".name IS 'A human-readable name for an attribute or entity.';COMMENT ON COLUMN "ScientificKnowledgeFragment".id IS 'A simple, locally-generated unique identifier specific with different heuristic formatting for each application.';COMMENT ON COLUMN "ScientificKnowledgeFragment".type IS 'The type of an Entity expressed as curi.';
CREATE TABLE "ScientificKnowledgeExpression_has_representation" (
	"ScientificKnowledgeExpression_id" TEXT, 
	has_representation_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeExpression_id", has_representation_id), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY(has_representation_id) REFERENCES "ScientificKnowledgeItem" (id)
);COMMENT ON TABLE "ScientificKnowledgeExpression_has_representation" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeExpression_has_representation"."ScientificKnowledgeExpression_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeExpression_has_representation".has_representation_id IS 'holds between wholes and their parts (material entities or processes)';
CREATE TABLE "ScientificKnowledgeItem_xref" (
	"ScientificKnowledgeItem_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificKnowledgeItem_id", xref), 
	FOREIGN KEY("ScientificKnowledgeItem_id") REFERENCES "ScientificKnowledgeItem" (id)
);COMMENT ON TABLE "ScientificKnowledgeItem_xref" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeItem_xref"."ScientificKnowledgeItem_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeItem_xref".xref IS 'A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. ';
CREATE TABLE "ScientificKnowledgeItem_has_notes" (
	"ScientificKnowledgeItem_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeItem_id", has_notes_id), 
	FOREIGN KEY("ScientificKnowledgeItem_id") REFERENCES "ScientificKnowledgeItem" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);COMMENT ON TABLE "ScientificKnowledgeItem_has_notes" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeItem_has_notes"."ScientificKnowledgeItem_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeItem_has_notes".has_notes_id IS 'Points to notes that are about a given entity.';
CREATE TABLE "ScientificKnowledgeItem_iri" (
	"ScientificKnowledgeItem_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("ScientificKnowledgeItem_id", iri), 
	FOREIGN KEY("ScientificKnowledgeItem_id") REFERENCES "ScientificKnowledgeItem" (id)
);COMMENT ON TABLE "ScientificKnowledgeItem_iri" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeItem_iri"."ScientificKnowledgeItem_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeItem_iri".iri IS 'An IRI for an entity. ';
CREATE TABLE "ScientificKnowledgeItem_has_part" (
	"ScientificKnowledgeItem_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeItem_id", has_part_id), 
	FOREIGN KEY("ScientificKnowledgeItem_id") REFERENCES "ScientificKnowledgeItem" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ScientificKnowledgeFragment" (id)
);COMMENT ON TABLE "ScientificKnowledgeItem_has_part" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeItem_has_part"."ScientificKnowledgeItem_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeItem_has_part".has_part_id IS 'holds between wholes and their parts (material entities or processes)';
CREATE TABLE "ScientificKnowledgeFragment_xref" (
	"ScientificKnowledgeFragment_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificKnowledgeFragment_id", xref), 
	FOREIGN KEY("ScientificKnowledgeFragment_id") REFERENCES "ScientificKnowledgeFragment" (id)
);COMMENT ON TABLE "ScientificKnowledgeFragment_xref" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeFragment_xref"."ScientificKnowledgeFragment_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeFragment_xref".xref IS 'A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.   This property should point to a database record or webpage that  defines the definition of the NamedThing. ';
CREATE TABLE "ScientificKnowledgeFragment_has_notes" (
	"ScientificKnowledgeFragment_id" TEXT, 
	has_notes_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeFragment_id", has_notes_id), 
	FOREIGN KEY("ScientificKnowledgeFragment_id") REFERENCES "ScientificKnowledgeFragment" (id), 
	FOREIGN KEY(has_notes_id) REFERENCES "Note" (id)
);COMMENT ON TABLE "ScientificKnowledgeFragment_has_notes" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeFragment_has_notes"."ScientificKnowledgeFragment_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeFragment_has_notes".has_notes_id IS 'Points to notes that are about a given entity.';
CREATE TABLE "ScientificKnowledgeFragment_iri" (
	"ScientificKnowledgeFragment_id" TEXT, 
	iri TEXT, 
	PRIMARY KEY ("ScientificKnowledgeFragment_id", iri), 
	FOREIGN KEY("ScientificKnowledgeFragment_id") REFERENCES "ScientificKnowledgeFragment" (id)
);COMMENT ON TABLE "ScientificKnowledgeFragment_iri" IS 'None';COMMENT ON COLUMN "ScientificKnowledgeFragment_iri"."ScientificKnowledgeFragment_id" IS 'Autocreated FK slot';COMMENT ON COLUMN "ScientificKnowledgeFragment_iri".iri IS 'An IRI for an entity. ';
