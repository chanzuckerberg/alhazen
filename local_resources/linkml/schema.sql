-- # Class: "Entity" Description: "Root Model class for all things and informational relationships, real or imagined."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "NamedThing" Description: "an entity or concept/class described by a name"
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "InformationContentEntity" Description: "a piece of information that typically describes some topic of discourse or is used as support."
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "ScientificKnowledgeExpression" Description: "Any expression of scientific knowledge.   "
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: title Description: The title of a ScientificKnowledgeExpression.
--     * Slot: abstract Description: The written abstract of a ScientificKnowledgeExpression.  This is typically a paragraph of text providing  a summary of the expression.
--     * Slot: full_text Description: The full textual content of a ScientificKnowledgeExpression, expressed as a string  (usually with an associated specified encoding / schema / format).
--     * Slot: publication_date Description: date on which an entity was published (i.e., made available to the public).
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "ScientificPublication" Description: "A published expression of scientific knowledge,  such as a paper, book, thesis, conference proceedings, etc.   "
--     * Slot: doi Description: A digital object identifier (see http://doi.org/).
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: title Description: The title of a ScientificKnowledgeExpression.
--     * Slot: abstract Description: The written abstract of a ScientificKnowledgeExpression.  This is typically a paragraph of text providing  a summary of the expression.
--     * Slot: full_text Description: The full textual content of a ScientificKnowledgeExpression, expressed as a string  (usually with an associated specified encoding / schema / format).
--     * Slot: publication_date Description: date on which an entity was published (i.e., made available to the public).
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "ScientificPrimaryResearchArticle" Description: "A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion). These articles will have undergone  peer review. "
--     * Slot: doi Description: A digital object identifier (see http://doi.org/).
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: title Description: The title of a ScientificKnowledgeExpression.
--     * Slot: abstract Description: The written abstract of a ScientificKnowledgeExpression.  This is typically a paragraph of text providing  a summary of the expression.
--     * Slot: full_text Description: The full textual content of a ScientificKnowledgeExpression, expressed as a string  (usually with an associated specified encoding / schema / format).
--     * Slot: publication_date Description: date on which an entity was published (i.e., made available to the public).
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "ScientificPrimaryResearchPreprint" Description: "A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion). These articles have been published as preprints and have NOT undergone peer review. "
--     * Slot: doi Description: A digital object identifier (see http://doi.org/).
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: title Description: The title of a ScientificKnowledgeExpression.
--     * Slot: abstract Description: The written abstract of a ScientificKnowledgeExpression.  This is typically a paragraph of text providing  a summary of the expression.
--     * Slot: full_text Description: The full textual content of a ScientificKnowledgeExpression, expressed as a string  (usually with an associated specified encoding / schema / format).
--     * Slot: publication_date Description: date on which an entity was published (i.e., made available to the public).
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "ScientificReviewArticle" Description: "A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion).   "
--     * Slot: doi Description: A digital object identifier (see http://doi.org/).
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: title Description: The title of a ScientificKnowledgeExpression.
--     * Slot: abstract Description: The written abstract of a ScientificKnowledgeExpression.  This is typically a paragraph of text providing  a summary of the expression.
--     * Slot: full_text Description: The full textual content of a ScientificKnowledgeExpression, expressed as a string  (usually with an associated specified encoding / schema / format).
--     * Slot: publication_date Description: date on which an entity was published (i.e., made available to the public).
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "ScientificBook" Description: "A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion).   "
--     * Slot: doi Description: A digital object identifier (see http://doi.org/).
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: title Description: The title of a ScientificKnowledgeExpression.
--     * Slot: abstract Description: The written abstract of a ScientificKnowledgeExpression.  This is typically a paragraph of text providing  a summary of the expression.
--     * Slot: full_text Description: The full textual content of a ScientificKnowledgeExpression, expressed as a string  (usually with an associated specified encoding / schema / format).
--     * Slot: publication_date Description: date on which an entity was published (i.e., made available to the public).
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "ScientificBookChapter" Description: "A scientific publication describing original research typically formatted in an IMRaD structure (introduction, methods, resulst, and discussion).   "
--     * Slot: part_of Description: The book that this chapter is a part of
--     * Slot: doi Description: A digital object identifier (see http://doi.org/).
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: title Description: The title of a ScientificKnowledgeExpression.
--     * Slot: abstract Description: The written abstract of a ScientificKnowledgeExpression.  This is typically a paragraph of text providing  a summary of the expression.
--     * Slot: full_text Description: The full textual content of a ScientificKnowledgeExpression, expressed as a string  (usually with an associated specified encoding / schema / format).
--     * Slot: publication_date Description: date on which an entity was published (i.e., made available to the public).
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "ScientificConferenceArticle" Description: "A scientific publication describing original research that was presented at a conference.   "
--     * Slot: part_of Description: The book that this chapter is a part of
--     * Slot: doi Description: A digital object identifier (see http://doi.org/).
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: title Description: The title of a ScientificKnowledgeExpression.
--     * Slot: abstract Description: The written abstract of a ScientificKnowledgeExpression.  This is typically a paragraph of text providing  a summary of the expression.
--     * Slot: full_text Description: The full textual content of a ScientificKnowledgeExpression, expressed as a string  (usually with an associated specified encoding / schema / format).
--     * Slot: publication_date Description: date on which an entity was published (i.e., made available to the public).
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "ScientificDissertation" Description: "A thesis or dissertation submitted by a researcher as  part of their work to qualify for an advanced degree - usually a  doctorate.   "
--     * Slot: doi Description: A digital object identifier (see http://doi.org/).
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: title Description: The title of a ScientificKnowledgeExpression.
--     * Slot: abstract Description: The written abstract of a ScientificKnowledgeExpression.  This is typically a paragraph of text providing  a summary of the expression.
--     * Slot: full_text Description: The full textual content of a ScientificKnowledgeExpression, expressed as a string  (usually with an associated specified encoding / schema / format).
--     * Slot: publication_date Description: date on which an entity was published (i.e., made available to the public).
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "InformationResource" Description: "A database or knowledgebase and its supporting ecosystem of interfaces  and services that deliver content to consumers (e.g. web portals, APIs,  query endpoints, streaming services, data downloads, etc.). A single Information Resource by this definition may span many different datasets or databases, and include many access endpoints and user interfaces. Information Resources include project-specific resources such as a Translator Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "ScientificKnowledgeCollection" Description: "A collection of expressions of scientific knowledge."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: logical_query Description: A logical query that can be used to retrieve a set of entities from a  knowledgebase. Typically expressed as a boolean logic expression over  terms to be searched for.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "ScientificPublicationCollection" Description: "A collection of scientific publications."
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: logical_query Description: A logical query that can be used to retrieve a set of entities from a  knowledgebase. Typically expressed as a boolean logic expression over  terms to be searched for.
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "ScientificKnowledgeFragment" Description: "A selected subportion of the contents of a ScientificKnowledgeExpression, described by an selector."
--     * Slot: part_of Description: The SKE that this fragment is a part of
--     * Slot: selector Description: A way of specifying a location within a ScientificKnowledgeExpression that describes where a ScientificKnowledgeFragment comes from
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "Selector" Description: "A way of localizing and describing a ScientificKnowledgeFragment within a ScientificKnowledgeExpression."
--     * Slot: license Description: A license under which an information content entity is provided.
--     * Slot: rights Description: 
--     * Slot: format Description: 
--     * Slot: creation_date Description: date on which an entity was created. This can be applied to nodes or edges
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
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
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "Person" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "Author" Description: ""
--     * Slot: orcid Description: An ORCID for an entity. 
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: ScientificPublication_id Description: Autocreated FK slot
--     * Slot: ScientificPrimaryResearchArticle_id Description: Autocreated FK slot
--     * Slot: ScientificPrimaryResearchPreprint_id Description: Autocreated FK slot
--     * Slot: ScientificReviewArticle_id Description: Autocreated FK slot
--     * Slot: ScientificBook_id Description: Autocreated FK slot
--     * Slot: ScientificBookChapter_id Description: Autocreated FK slot
--     * Slot: ScientificConferenceArticle_id Description: Autocreated FK slot
--     * Slot: ScientificDissertation_id Description: Autocreated FK slot
-- # Class: "Organization" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "City" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
-- # Class: "Country" Description: ""
--     * Slot: name Description: A human-readable name for an attribute or entity.
--     * Slot: id Description: A unique identifier for an entity.
--     * Slot: iri Description: An IRI for an entity.  This is determined by the id using expansion rules.
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
-- # Class: "ScientificKnowledgeExpression_has_part" Description: ""
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: Fragments that have been highlighted as as part of this SKE.
-- # Class: "ScientificKnowledgeExpression_xref" Description: ""
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificKnowledgeExpression_type" Description: ""
--     * Slot: ScientificKnowledgeExpression_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificPublication_has_part" Description: ""
--     * Slot: ScientificPublication_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: Fragments that have been highlighted as as part of this SKE.
-- # Class: "ScientificPublication_xref" Description: ""
--     * Slot: ScientificPublication_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificPublication_type" Description: ""
--     * Slot: ScientificPublication_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificPrimaryResearchArticle_has_part" Description: ""
--     * Slot: ScientificPrimaryResearchArticle_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: Fragments that have been highlighted as as part of this SKE.
-- # Class: "ScientificPrimaryResearchArticle_xref" Description: ""
--     * Slot: ScientificPrimaryResearchArticle_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificPrimaryResearchArticle_type" Description: ""
--     * Slot: ScientificPrimaryResearchArticle_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificPrimaryResearchPreprint_has_part" Description: ""
--     * Slot: ScientificPrimaryResearchPreprint_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: Fragments that have been highlighted as as part of this SKE.
-- # Class: "ScientificPrimaryResearchPreprint_xref" Description: ""
--     * Slot: ScientificPrimaryResearchPreprint_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificPrimaryResearchPreprint_type" Description: ""
--     * Slot: ScientificPrimaryResearchPreprint_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificReviewArticle_has_part" Description: ""
--     * Slot: ScientificReviewArticle_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: Fragments that have been highlighted as as part of this SKE.
-- # Class: "ScientificReviewArticle_xref" Description: ""
--     * Slot: ScientificReviewArticle_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificReviewArticle_type" Description: ""
--     * Slot: ScientificReviewArticle_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificBook_has_part" Description: ""
--     * Slot: ScientificBook_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: Fragments that have been highlighted as as part of this SKE.
-- # Class: "ScientificBook_xref" Description: ""
--     * Slot: ScientificBook_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificBook_type" Description: ""
--     * Slot: ScientificBook_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificBookChapter_has_part" Description: ""
--     * Slot: ScientificBookChapter_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: Fragments that have been highlighted as as part of this SKE.
-- # Class: "ScientificBookChapter_xref" Description: ""
--     * Slot: ScientificBookChapter_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificBookChapter_type" Description: ""
--     * Slot: ScientificBookChapter_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificConferenceArticle_has_part" Description: ""
--     * Slot: ScientificConferenceArticle_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: Fragments that have been highlighted as as part of this SKE.
-- # Class: "ScientificConferenceArticle_xref" Description: ""
--     * Slot: ScientificConferenceArticle_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificConferenceArticle_type" Description: ""
--     * Slot: ScientificConferenceArticle_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificDissertation_has_part" Description: ""
--     * Slot: ScientificDissertation_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: Fragments that have been highlighted as as part of this SKE.
-- # Class: "ScientificDissertation_xref" Description: ""
--     * Slot: ScientificDissertation_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificDissertation_type" Description: ""
--     * Slot: ScientificDissertation_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "InformationResource_xref" Description: ""
--     * Slot: InformationResource_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "InformationResource_type" Description: ""
--     * Slot: InformationResource_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificKnowledgeCollection_information_sources" Description: ""
--     * Slot: ScientificKnowledgeCollection_id Description: Autocreated FK slot
--     * Slot: information_sources_id Description: The InformationResources that are queried to build a  ScientificKnowledgeCollection.
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
--     * Slot: information_sources_id Description: The InformationResources that are queried to build a  ScientificKnowledgeCollection.
-- # Class: "ScientificPublicationCollection_xref" Description: ""
--     * Slot: ScientificPublicationCollection_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificPublicationCollection_type" Description: ""
--     * Slot: ScientificPublicationCollection_id Description: Autocreated FK slot
--     * Slot: type Description: 
-- # Class: "ScientificKnowledgeFragment_xref" Description: ""
--     * Slot: ScientificKnowledgeFragment_id Description: Autocreated FK slot
--     * Slot: xref Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
-- # Class: "ScientificKnowledgeFragment_type" Description: ""
--     * Slot: ScientificKnowledgeFragment_id Description: Autocreated FK slot
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
CREATE TABLE "ScientificKnowledgeExpression" (
	id TEXT NOT NULL, 
	title TEXT, 
	abstract TEXT, 
	full_text TEXT, 
	publication_date DATE, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificPublication" (
	doi TEXT, 
	id TEXT NOT NULL, 
	title TEXT, 
	abstract TEXT, 
	full_text TEXT, 
	publication_date DATE, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificPrimaryResearchArticle" (
	doi TEXT, 
	id TEXT NOT NULL, 
	title TEXT, 
	abstract TEXT, 
	full_text TEXT, 
	publication_date DATE, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificPrimaryResearchPreprint" (
	doi TEXT, 
	id TEXT NOT NULL, 
	title TEXT, 
	abstract TEXT, 
	full_text TEXT, 
	publication_date DATE, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificReviewArticle" (
	doi TEXT, 
	id TEXT NOT NULL, 
	title TEXT, 
	abstract TEXT, 
	full_text TEXT, 
	publication_date DATE, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificBook" (
	doi TEXT, 
	id TEXT NOT NULL, 
	title TEXT, 
	abstract TEXT, 
	full_text TEXT, 
	publication_date DATE, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ScientificDissertation" (
	doi TEXT, 
	id TEXT NOT NULL, 
	title TEXT, 
	abstract TEXT, 
	full_text TEXT, 
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
CREATE TABLE "ScientificBookChapter" (
	part_of TEXT, 
	doi TEXT, 
	id TEXT NOT NULL, 
	title TEXT, 
	abstract TEXT, 
	full_text TEXT, 
	publication_date DATE, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(part_of) REFERENCES "ScientificBook" (id)
);
CREATE TABLE "ScientificConferenceArticle" (
	part_of TEXT, 
	doi TEXT, 
	id TEXT NOT NULL, 
	title TEXT, 
	abstract TEXT, 
	full_text TEXT, 
	publication_date DATE, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(part_of) REFERENCES "ScientificBook" (id)
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
	PRIMARY KEY (id), 
	FOREIGN KEY(part_of) REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY(selector) REFERENCES "Selector" (id)
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
CREATE TABLE "ScientificPrimaryResearchArticle_xref" (
	"ScientificPrimaryResearchArticle_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificPrimaryResearchArticle_id", xref), 
	FOREIGN KEY("ScientificPrimaryResearchArticle_id") REFERENCES "ScientificPrimaryResearchArticle" (id)
);
CREATE TABLE "ScientificPrimaryResearchArticle_type" (
	"ScientificPrimaryResearchArticle_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("ScientificPrimaryResearchArticle_id", type), 
	FOREIGN KEY("ScientificPrimaryResearchArticle_id") REFERENCES "ScientificPrimaryResearchArticle" (id)
);
CREATE TABLE "ScientificPrimaryResearchPreprint_xref" (
	"ScientificPrimaryResearchPreprint_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificPrimaryResearchPreprint_id", xref), 
	FOREIGN KEY("ScientificPrimaryResearchPreprint_id") REFERENCES "ScientificPrimaryResearchPreprint" (id)
);
CREATE TABLE "ScientificPrimaryResearchPreprint_type" (
	"ScientificPrimaryResearchPreprint_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("ScientificPrimaryResearchPreprint_id", type), 
	FOREIGN KEY("ScientificPrimaryResearchPreprint_id") REFERENCES "ScientificPrimaryResearchPreprint" (id)
);
CREATE TABLE "ScientificReviewArticle_xref" (
	"ScientificReviewArticle_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificReviewArticle_id", xref), 
	FOREIGN KEY("ScientificReviewArticle_id") REFERENCES "ScientificReviewArticle" (id)
);
CREATE TABLE "ScientificReviewArticle_type" (
	"ScientificReviewArticle_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("ScientificReviewArticle_id", type), 
	FOREIGN KEY("ScientificReviewArticle_id") REFERENCES "ScientificReviewArticle" (id)
);
CREATE TABLE "ScientificBook_xref" (
	"ScientificBook_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificBook_id", xref), 
	FOREIGN KEY("ScientificBook_id") REFERENCES "ScientificBook" (id)
);
CREATE TABLE "ScientificBook_type" (
	"ScientificBook_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("ScientificBook_id", type), 
	FOREIGN KEY("ScientificBook_id") REFERENCES "ScientificBook" (id)
);
CREATE TABLE "ScientificDissertation_xref" (
	"ScientificDissertation_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificDissertation_id", xref), 
	FOREIGN KEY("ScientificDissertation_id") REFERENCES "ScientificDissertation" (id)
);
CREATE TABLE "ScientificDissertation_type" (
	"ScientificDissertation_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("ScientificDissertation_id", type), 
	FOREIGN KEY("ScientificDissertation_id") REFERENCES "ScientificDissertation" (id)
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
CREATE TABLE "ScientificKnowledgeCollection_information_sources" (
	"ScientificKnowledgeCollection_id" TEXT, 
	information_sources_id TEXT, 
	PRIMARY KEY ("ScientificKnowledgeCollection_id", information_sources_id), 
	FOREIGN KEY("ScientificKnowledgeCollection_id") REFERENCES "ScientificKnowledgeCollection" (id), 
	FOREIGN KEY(information_sources_id) REFERENCES "InformationResource" (id)
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
CREATE TABLE "Author" (
	orcid TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	"ScientificKnowledgeExpression_id" TEXT, 
	"ScientificPublication_id" TEXT, 
	"ScientificPrimaryResearchArticle_id" TEXT, 
	"ScientificPrimaryResearchPreprint_id" TEXT, 
	"ScientificReviewArticle_id" TEXT, 
	"ScientificBook_id" TEXT, 
	"ScientificBookChapter_id" TEXT, 
	"ScientificConferenceArticle_id" TEXT, 
	"ScientificDissertation_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ScientificKnowledgeExpression_id") REFERENCES "ScientificKnowledgeExpression" (id), 
	FOREIGN KEY("ScientificPublication_id") REFERENCES "ScientificPublication" (id), 
	FOREIGN KEY("ScientificPrimaryResearchArticle_id") REFERENCES "ScientificPrimaryResearchArticle" (id), 
	FOREIGN KEY("ScientificPrimaryResearchPreprint_id") REFERENCES "ScientificPrimaryResearchPreprint" (id), 
	FOREIGN KEY("ScientificReviewArticle_id") REFERENCES "ScientificReviewArticle" (id), 
	FOREIGN KEY("ScientificBook_id") REFERENCES "ScientificBook" (id), 
	FOREIGN KEY("ScientificBookChapter_id") REFERENCES "ScientificBookChapter" (id), 
	FOREIGN KEY("ScientificConferenceArticle_id") REFERENCES "ScientificConferenceArticle" (id), 
	FOREIGN KEY("ScientificDissertation_id") REFERENCES "ScientificDissertation" (id)
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
CREATE TABLE "ScientificPrimaryResearchArticle_has_part" (
	"ScientificPrimaryResearchArticle_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("ScientificPrimaryResearchArticle_id", has_part_id), 
	FOREIGN KEY("ScientificPrimaryResearchArticle_id") REFERENCES "ScientificPrimaryResearchArticle" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "ScientificPrimaryResearchPreprint_has_part" (
	"ScientificPrimaryResearchPreprint_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("ScientificPrimaryResearchPreprint_id", has_part_id), 
	FOREIGN KEY("ScientificPrimaryResearchPreprint_id") REFERENCES "ScientificPrimaryResearchPreprint" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "ScientificReviewArticle_has_part" (
	"ScientificReviewArticle_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("ScientificReviewArticle_id", has_part_id), 
	FOREIGN KEY("ScientificReviewArticle_id") REFERENCES "ScientificReviewArticle" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "ScientificBook_has_part" (
	"ScientificBook_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("ScientificBook_id", has_part_id), 
	FOREIGN KEY("ScientificBook_id") REFERENCES "ScientificBook" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "ScientificBookChapter_has_part" (
	"ScientificBookChapter_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("ScientificBookChapter_id", has_part_id), 
	FOREIGN KEY("ScientificBookChapter_id") REFERENCES "ScientificBookChapter" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "ScientificBookChapter_xref" (
	"ScientificBookChapter_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificBookChapter_id", xref), 
	FOREIGN KEY("ScientificBookChapter_id") REFERENCES "ScientificBookChapter" (id)
);
CREATE TABLE "ScientificBookChapter_type" (
	"ScientificBookChapter_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("ScientificBookChapter_id", type), 
	FOREIGN KEY("ScientificBookChapter_id") REFERENCES "ScientificBookChapter" (id)
);
CREATE TABLE "ScientificConferenceArticle_has_part" (
	"ScientificConferenceArticle_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("ScientificConferenceArticle_id", has_part_id), 
	FOREIGN KEY("ScientificConferenceArticle_id") REFERENCES "ScientificConferenceArticle" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ScientificKnowledgeFragment" (id)
);
CREATE TABLE "ScientificConferenceArticle_xref" (
	"ScientificConferenceArticle_id" TEXT, 
	xref TEXT, 
	PRIMARY KEY ("ScientificConferenceArticle_id", xref), 
	FOREIGN KEY("ScientificConferenceArticle_id") REFERENCES "ScientificConferenceArticle" (id)
);
CREATE TABLE "ScientificConferenceArticle_type" (
	"ScientificConferenceArticle_id" TEXT, 
	type TEXT, 
	PRIMARY KEY ("ScientificConferenceArticle_id", type), 
	FOREIGN KEY("ScientificConferenceArticle_id") REFERENCES "ScientificConferenceArticle" (id)
);
CREATE TABLE "ScientificDissertation_has_part" (
	"ScientificDissertation_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("ScientificDissertation_id", has_part_id), 
	FOREIGN KEY("ScientificDissertation_id") REFERENCES "ScientificDissertation" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ScientificKnowledgeFragment" (id)
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
