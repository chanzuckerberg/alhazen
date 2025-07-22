
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
    type = Column(Text(), nullable=False )
    
    
    iri_rel = relationship( "EntityIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: EntityIri(iri=x_))
    

    def __repr__(self):
        return f"Entity(id={self.id},type={self.type},)"



    


class EntityIri(Base):
    """
    
    """
    __tablename__ = 'Entity_iri'

    Entity_id = Column(Text(), ForeignKey('Entity.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Entity_iri(Entity_id={self.Entity_id},iri={self.iri},)"



    


class NamedThingIri(Base):
    """
    
    """
    __tablename__ = 'NamedThing_iri'

    NamedThing_id = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"NamedThing_iri(NamedThing_id={self.NamedThing_id},iri={self.iri},)"



    


class InformationContentEntityXref(Base):
    """
    
    """
    __tablename__ = 'InformationContentEntity_xref'

    InformationContentEntity_id = Column(Text(), ForeignKey('InformationContentEntity.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationContentEntity_xref(InformationContentEntity_id={self.InformationContentEntity_id},xref={self.xref},)"



    


class InformationContentEntityHasNotes(Base):
    """
    
    """
    __tablename__ = 'InformationContentEntity_has_notes'

    InformationContentEntity_id = Column(Text(), ForeignKey('InformationContentEntity.id'), primary_key=True)
    has_notes_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationContentEntity_has_notes(InformationContentEntity_id={self.InformationContentEntity_id},has_notes_id={self.has_notes_id},)"



    


class InformationContentEntityIri(Base):
    """
    
    """
    __tablename__ = 'InformationContentEntity_iri'

    InformationContentEntity_id = Column(Text(), ForeignKey('InformationContentEntity.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationContentEntity_iri(InformationContentEntity_id={self.InformationContentEntity_id},iri={self.iri},)"



    


class UserQuestionXref(Base):
    """
    
    """
    __tablename__ = 'UserQuestion_xref'

    UserQuestion_id = Column(Text(), ForeignKey('UserQuestion.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"UserQuestion_xref(UserQuestion_id={self.UserQuestion_id},xref={self.xref},)"



    


class UserQuestionHasNotes(Base):
    """
    
    """
    __tablename__ = 'UserQuestion_has_notes'

    UserQuestion_id = Column(Text(), ForeignKey('UserQuestion.id'), primary_key=True)
    has_notes_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    

    def __repr__(self):
        return f"UserQuestion_has_notes(UserQuestion_id={self.UserQuestion_id},has_notes_id={self.has_notes_id},)"



    


class UserQuestionIri(Base):
    """
    
    """
    __tablename__ = 'UserQuestion_iri'

    UserQuestion_id = Column(Text(), ForeignKey('UserQuestion.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"UserQuestion_iri(UserQuestion_id={self.UserQuestion_id},iri={self.iri},)"



    


class InformationResourceXref(Base):
    """
    
    """
    __tablename__ = 'InformationResource_xref'

    InformationResource_id = Column(Text(), ForeignKey('InformationResource.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationResource_xref(InformationResource_id={self.InformationResource_id},xref={self.xref},)"



    


class InformationResourceHasNotes(Base):
    """
    
    """
    __tablename__ = 'InformationResource_has_notes'

    InformationResource_id = Column(Text(), ForeignKey('InformationResource.id'), primary_key=True)
    has_notes_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationResource_has_notes(InformationResource_id={self.InformationResource_id},has_notes_id={self.has_notes_id},)"



    


class InformationResourceIri(Base):
    """
    
    """
    __tablename__ = 'InformationResource_iri'

    InformationResource_id = Column(Text(), ForeignKey('InformationResource.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationResource_iri(InformationResource_id={self.InformationResource_id},iri={self.iri},)"



    


class ScientificKnowledgeCollectionHasMembers(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeCollection_has_members'

    ScientificKnowledgeCollection_id = Column(Text(), ForeignKey('ScientificKnowledgeCollection.id'), primary_key=True)
    has_members_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeCollection_has_members(ScientificKnowledgeCollection_id={self.ScientificKnowledgeCollection_id},has_members_id={self.has_members_id},)"



    


class ScientificKnowledgeCollectionXref(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeCollection_xref'

    ScientificKnowledgeCollection_id = Column(Text(), ForeignKey('ScientificKnowledgeCollection.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeCollection_xref(ScientificKnowledgeCollection_id={self.ScientificKnowledgeCollection_id},xref={self.xref},)"



    


class ScientificKnowledgeCollectionHasNotes(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeCollection_has_notes'

    ScientificKnowledgeCollection_id = Column(Text(), ForeignKey('ScientificKnowledgeCollection.id'), primary_key=True)
    has_notes_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeCollection_has_notes(ScientificKnowledgeCollection_id={self.ScientificKnowledgeCollection_id},has_notes_id={self.has_notes_id},)"



    


class ScientificKnowledgeCollectionIri(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeCollection_iri'

    ScientificKnowledgeCollection_id = Column(Text(), ForeignKey('ScientificKnowledgeCollection.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeCollection_iri(ScientificKnowledgeCollection_id={self.ScientificKnowledgeCollection_id},iri={self.iri},)"



    


class ScientificKnowledgeExpressionHasRepresentation(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeExpression_has_representation'

    ScientificKnowledgeExpression_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'), primary_key=True)
    has_representation_id = Column(Text(), ForeignKey('ScientificKnowledgeItem.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeExpression_has_representation(ScientificKnowledgeExpression_id={self.ScientificKnowledgeExpression_id},has_representation_id={self.has_representation_id},)"



    


class ScientificKnowledgeExpressionMemberOf(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeExpression_member_of'

    ScientificKnowledgeExpression_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'), primary_key=True)
    member_of_id = Column(Text(), ForeignKey('ScientificKnowledgeCollection.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeExpression_member_of(ScientificKnowledgeExpression_id={self.ScientificKnowledgeExpression_id},member_of_id={self.member_of_id},)"



    


class ScientificKnowledgeExpressionHasAuthors(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeExpression_has_authors'

    ScientificKnowledgeExpression_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'), primary_key=True)
    has_authors_id = Column(Text(), ForeignKey('Author.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeExpression_has_authors(ScientificKnowledgeExpression_id={self.ScientificKnowledgeExpression_id},has_authors_id={self.has_authors_id},)"



    


class ScientificKnowledgeExpressionXref(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeExpression_xref'

    ScientificKnowledgeExpression_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeExpression_xref(ScientificKnowledgeExpression_id={self.ScientificKnowledgeExpression_id},xref={self.xref},)"



    


class ScientificKnowledgeExpressionHasNotes(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeExpression_has_notes'

    ScientificKnowledgeExpression_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'), primary_key=True)
    has_notes_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeExpression_has_notes(ScientificKnowledgeExpression_id={self.ScientificKnowledgeExpression_id},has_notes_id={self.has_notes_id},)"



    


class ScientificKnowledgeExpressionIri(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeExpression_iri'

    ScientificKnowledgeExpression_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeExpression_iri(ScientificKnowledgeExpression_id={self.ScientificKnowledgeExpression_id},iri={self.iri},)"



    


class ScientificKnowledgeItemHasPart(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeItem_has_part'

    ScientificKnowledgeItem_id = Column(Text(), ForeignKey('ScientificKnowledgeItem.id'), primary_key=True)
    has_part_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeItem_has_part(ScientificKnowledgeItem_id={self.ScientificKnowledgeItem_id},has_part_id={self.has_part_id},)"



    


class ScientificKnowledgeItemXref(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeItem_xref'

    ScientificKnowledgeItem_id = Column(Text(), ForeignKey('ScientificKnowledgeItem.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeItem_xref(ScientificKnowledgeItem_id={self.ScientificKnowledgeItem_id},xref={self.xref},)"



    


class ScientificKnowledgeItemHasNotes(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeItem_has_notes'

    ScientificKnowledgeItem_id = Column(Text(), ForeignKey('ScientificKnowledgeItem.id'), primary_key=True)
    has_notes_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeItem_has_notes(ScientificKnowledgeItem_id={self.ScientificKnowledgeItem_id},has_notes_id={self.has_notes_id},)"



    


class ScientificKnowledgeItemIri(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeItem_iri'

    ScientificKnowledgeItem_id = Column(Text(), ForeignKey('ScientificKnowledgeItem.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeItem_iri(ScientificKnowledgeItem_id={self.ScientificKnowledgeItem_id},iri={self.iri},)"



    


class ScientificKnowledgeFragmentXref(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeFragment_xref'

    ScientificKnowledgeFragment_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeFragment_xref(ScientificKnowledgeFragment_id={self.ScientificKnowledgeFragment_id},xref={self.xref},)"



    


class ScientificKnowledgeFragmentHasNotes(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeFragment_has_notes'

    ScientificKnowledgeFragment_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    has_notes_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeFragment_has_notes(ScientificKnowledgeFragment_id={self.ScientificKnowledgeFragment_id},has_notes_id={self.has_notes_id},)"



    


class ScientificKnowledgeFragmentIri(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeFragment_iri'

    ScientificKnowledgeFragment_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeFragment_iri(ScientificKnowledgeFragment_id={self.ScientificKnowledgeFragment_id},iri={self.iri},)"



    


class NoteIsAbout(Base):
    """
    
    """
    __tablename__ = 'Note_is_about'

    Note_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    is_about_id = Column(Text(), ForeignKey('InformationContentEntity.id'), primary_key=True)
    

    def __repr__(self):
        return f"Note_is_about(Note_id={self.Note_id},is_about_id={self.is_about_id},)"



    


class NoteXref(Base):
    """
    
    """
    __tablename__ = 'Note_xref'

    Note_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Note_xref(Note_id={self.Note_id},xref={self.xref},)"



    


class NoteHasNotes(Base):
    """
    
    """
    __tablename__ = 'Note_has_notes'

    Note_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    has_notes_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    

    def __repr__(self):
        return f"Note_has_notes(Note_id={self.Note_id},has_notes_id={self.has_notes_id},)"



    


class NoteIri(Base):
    """
    
    """
    __tablename__ = 'Note_iri'

    Note_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Note_iri(Note_id={self.Note_id},iri={self.iri},)"



    


class AuthorAffiliations(Base):
    """
    
    """
    __tablename__ = 'Author_affiliations'

    Author_id = Column(Text(), ForeignKey('Author.id'), primary_key=True)
    affiliations_id = Column(Text(), ForeignKey('Organization.id'), primary_key=True)
    

    def __repr__(self):
        return f"Author_affiliations(Author_id={self.Author_id},affiliations_id={self.affiliations_id},)"



    


class AuthorIsAuthorOf(Base):
    """
    
    """
    __tablename__ = 'Author_is_author_of'

    Author_id = Column(Text(), ForeignKey('Author.id'), primary_key=True)
    is_author_of_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'), primary_key=True)
    

    def __repr__(self):
        return f"Author_is_author_of(Author_id={self.Author_id},is_author_of_id={self.is_author_of_id},)"



    


class AuthorXref(Base):
    """
    
    """
    __tablename__ = 'Author_xref'

    Author_id = Column(Text(), ForeignKey('Author.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Author_xref(Author_id={self.Author_id},xref={self.xref},)"



    


class AuthorHasNotes(Base):
    """
    
    """
    __tablename__ = 'Author_has_notes'

    Author_id = Column(Text(), ForeignKey('Author.id'), primary_key=True)
    has_notes_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    

    def __repr__(self):
        return f"Author_has_notes(Author_id={self.Author_id},has_notes_id={self.has_notes_id},)"



    


class AuthorIri(Base):
    """
    
    """
    __tablename__ = 'Author_iri'

    Author_id = Column(Text(), ForeignKey('Author.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Author_iri(Author_id={self.Author_id},iri={self.iri},)"



    


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



    


class OrganizationHasNotes(Base):
    """
    
    """
    __tablename__ = 'Organization_has_notes'

    Organization_id = Column(Text(), ForeignKey('Organization.id'), primary_key=True)
    has_notes_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    

    def __repr__(self):
        return f"Organization_has_notes(Organization_id={self.Organization_id},has_notes_id={self.has_notes_id},)"



    


class OrganizationIri(Base):
    """
    
    """
    __tablename__ = 'Organization_iri'

    Organization_id = Column(Text(), ForeignKey('Organization.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Organization_iri(Organization_id={self.Organization_id},iri={self.iri},)"



    


class CityIri(Base):
    """
    
    """
    __tablename__ = 'City_iri'

    City_id = Column(Text(), ForeignKey('City.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"City_iri(City_id={self.City_id},iri={self.iri},)"



    


class CountryIri(Base):
    """
    
    """
    __tablename__ = 'Country_iri'

    Country_id = Column(Text(), ForeignKey('Country.id'), primary_key=True)
    iri = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Country_iri(Country_id={self.Country_id},iri={self.iri},)"



    


class NamedThing(Entity):
    """
    an entity or concept/class described by a name
    """
    __tablename__ = 'NamedThing'

    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    
    
    iri_rel = relationship( "NamedThingIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: NamedThingIri(iri=x_))
    

    def __repr__(self):
        return f"NamedThing(name={self.name},id={self.id},type={self.type},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InformationContentEntity(NamedThing):
    """
    A piece of information that is represented in the typically describes some topic of discourse or is used as support.

    """
    __tablename__ = 'InformationContentEntity'

    creation_date = Column(Date())
    content = Column(Text())
    token_count = Column(Integer())
    format = Column(Text())
    provenance = Column(Text())
    license = Column(Text())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    
    
    xref_rel = relationship( "InformationContentEntityXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: InformationContentEntityXref(xref=x_))
    
    
    # ManyToMany
    has_notes = relationship( "Note", secondary="InformationContentEntity_has_notes", back_populates="is_about")
    
    
    iri_rel = relationship( "InformationContentEntityIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: InformationContentEntityIri(iri=x_))
    

    def __repr__(self):
        return f"InformationContentEntity(creation_date={self.creation_date},content={self.content},token_count={self.token_count},format={self.format},provenance={self.provenance},license={self.license},name={self.name},id={self.id},type={self.type},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True,
        'polymorphic_on': type,
        "polymorphic_identity": "InformationContentEntity",
    }    


class City(NamedThing):
    """
    
    """
    __tablename__ = 'City'

    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    
    
    iri_rel = relationship( "CityIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: CityIri(iri=x_))
    

    def __repr__(self):
        return f"City(name={self.name},id={self.id},type={self.type},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Country(NamedThing):
    """
    
    """
    __tablename__ = 'Country'

    code2 = Column(Text())
    code3 = Column(Text())
    region = Column(Text())
    income = Column(Text())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    
    
    iri_rel = relationship( "CountryIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: CountryIri(iri=x_))
    

    def __repr__(self):
        return f"Country(code2={self.code2},code3={self.code3},region={self.region},income={self.income},name={self.name},id={self.id},type={self.type},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class UserQuestion(InformationContentEntity):
    """
    A question, inquiry, or instruction from an user of the Alhazen system.

    """
    __tablename__ = 'UserQuestion'

    creation_date = Column(Date())
    content = Column(Text())
    token_count = Column(Integer())
    format = Column(Text())
    provenance = Column(Text())
    license = Column(Text())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    
    
    xref_rel = relationship( "UserQuestionXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: UserQuestionXref(xref=x_))
    
    
    # ManyToMany
    has_notes = relationship( "Note", secondary="UserQuestion_has_notes")
    
    
    iri_rel = relationship( "UserQuestionIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: UserQuestionIri(iri=x_))
    

    def __repr__(self):
        return f"UserQuestion(creation_date={self.creation_date},content={self.content},token_count={self.token_count},format={self.format},provenance={self.provenance},license={self.license},name={self.name},id={self.id},type={self.type},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InformationResource(InformationContentEntity):
    """
    A database or knowledgebase and its supporting ecosystem of interfaces and services that deliver content to consumers (e.g. web portals, APIs, query endpoints, streaming services, data downloads, etc.). A single Information Resource by this definition may span many different datasets or databases, and include many access endpoints and user interfaces. Information Resources include project-specific resources such as a Translator Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb.
    """
    __tablename__ = 'InformationResource'

    creation_date = Column(Date())
    content = Column(Text())
    token_count = Column(Integer())
    format = Column(Text())
    provenance = Column(Text())
    license = Column(Text())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    
    
    xref_rel = relationship( "InformationResourceXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: InformationResourceXref(xref=x_))
    
    
    # ManyToMany
    has_notes = relationship( "Note", secondary="InformationResource_has_notes")
    
    
    iri_rel = relationship( "InformationResourceIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: InformationResourceIri(iri=x_))
    

    def __repr__(self):
        return f"InformationResource(creation_date={self.creation_date},content={self.content},token_count={self.token_count},format={self.format},provenance={self.provenance},license={self.license},name={self.name},id={self.id},type={self.type},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ScientificKnowledgeCollection(InformationContentEntity):
    """
    A collection of expressions of scientific knowledge.
    """
    __tablename__ = 'ScientificKnowledgeCollection'

    creation_date = Column(Date())
    content = Column(Text())
    token_count = Column(Integer())
    format = Column(Text())
    provenance = Column(Text())
    license = Column(Text())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    
    
    # ManyToMany
    has_members = relationship( "ScientificKnowledgeExpression", secondary="ScientificKnowledgeCollection_has_members")
    
    
    xref_rel = relationship( "ScientificKnowledgeCollectionXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificKnowledgeCollectionXref(xref=x_))
    
    
    # ManyToMany
    has_notes = relationship( "Note", secondary="ScientificKnowledgeCollection_has_notes", back_populates="is_about")
    
    
    iri_rel = relationship( "ScientificKnowledgeCollectionIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: ScientificKnowledgeCollectionIri(iri=x_))
    

    def __repr__(self):
        return f"ScientificKnowledgeCollection(creation_date={self.creation_date},content={self.content},token_count={self.token_count},format={self.format},provenance={self.provenance},license={self.license},name={self.name},id={self.id},type={self.type},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True,
        "polymorphic_identity": "ScientificKnowledgeCollection",
    }    


class ScientificKnowledgeExpression(InformationContentEntity):
    """
    Any expression of scientific knowledge.   
    """
    __tablename__ = 'ScientificKnowledgeExpression'

    publication_date = Column(Date())
    type = Column(Text(), nullable=False )
    creation_date = Column(Date())
    content = Column(Text())
    token_count = Column(Integer())
    format = Column(Text())
    provenance = Column(Text())
    license = Column(Text())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    
    
    # ManyToMany
    has_representation = relationship( "ScientificKnowledgeItem", secondary="ScientificKnowledgeExpression_has_representation")
    
    
    # ManyToMany
    member_of = relationship( "ScientificKnowledgeCollection", secondary="ScientificKnowledgeExpression_member_of")
    
    
    # ManyToMany
    has_authors = relationship( "Author", secondary="ScientificKnowledgeExpression_has_authors")
    
    
    xref_rel = relationship( "ScientificKnowledgeExpressionXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificKnowledgeExpressionXref(xref=x_))
    
    
    # ManyToMany
    has_notes = relationship( "Note", secondary="ScientificKnowledgeExpression_has_notes", back_populates="is_about")
    
    
    iri_rel = relationship( "ScientificKnowledgeExpressionIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: ScientificKnowledgeExpressionIri(iri=x_))
    

    def __repr__(self):
        return f"ScientificKnowledgeExpression(publication_date={self.publication_date},type={self.type},creation_date={self.creation_date},content={self.content},token_count={self.token_count},format={self.format},provenance={self.provenance},license={self.license},name={self.name},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True,
        "polymorphic_identity": "ScientificKnowledgeExpression",
    }    


class ScientificKnowledgeItem(InformationContentEntity):
    """
    A specific instance of a ScientificKnowledgeExpression:- our internal representation of an EPMC citation record, a local copy of a full-text article. This is the substrate that forms the basis for a ScientificKnowledgeFragment.
    """
    __tablename__ = 'ScientificKnowledgeItem'

    representation_of = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'))
    creation_date = Column(Date())
    content = Column(Text())
    token_count = Column(Integer())
    format = Column(Text())
    provenance = Column(Text())
    license = Column(Text())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    
    
    # ManyToMany
    has_part = relationship( "ScientificKnowledgeFragment", secondary="ScientificKnowledgeItem_has_part")
    
    
    xref_rel = relationship( "ScientificKnowledgeItemXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificKnowledgeItemXref(xref=x_))
    
    
    # ManyToMany
    has_notes = relationship( "Note", secondary="ScientificKnowledgeItem_has_notes", back_populates="is_about")
    
    
    iri_rel = relationship( "ScientificKnowledgeItemIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: ScientificKnowledgeItemIri(iri=x_))
    

    def __repr__(self):
        return f"ScientificKnowledgeItem(representation_of={self.representation_of},creation_date={self.creation_date},content={self.content},token_count={self.token_count},format={self.format},provenance={self.provenance},license={self.license},name={self.name},id={self.id},type={self.type},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True,
        "polymorphic_identity": "ScientificKnowledgeItem",
    }    


class ScientificKnowledgeFragment(InformationContentEntity):
    """
    A selected subportion of the contents of a ScientificKnowledgeExpression, described by an selector.
    """
    __tablename__ = 'ScientificKnowledgeFragment'

    part_of = Column(Text(), ForeignKey('ScientificKnowledgeItem.id'))
    offset = Column(Integer())
    length = Column(Integer())
    creation_date = Column(Date())
    content = Column(Text())
    token_count = Column(Integer())
    format = Column(Text())
    provenance = Column(Text())
    license = Column(Text())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    
    
    xref_rel = relationship( "ScientificKnowledgeFragmentXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificKnowledgeFragmentXref(xref=x_))
    
    
    # ManyToMany
    has_notes = relationship( "Note", secondary="ScientificKnowledgeFragment_has_notes", back_populates="is_about")
    
    
    iri_rel = relationship( "ScientificKnowledgeFragmentIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: ScientificKnowledgeFragmentIri(iri=x_))
    

    def __repr__(self):
        return f"ScientificKnowledgeFragment(part_of={self.part_of},offset={self.offset},length={self.length},creation_date={self.creation_date},content={self.content},token_count={self.token_count},format={self.format},provenance={self.provenance},license={self.license},name={self.name},id={self.id},type={self.type},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True,
        "polymorphic_identity": "ScientificKnowledgeFragment",
    }    


class Note(InformationContentEntity):
    """
    A structured piece of information with an author that is about another InformationContentEntity.
    """
    __tablename__ = 'Note'

    format = Column(Text())
    type = Column(Text(), nullable=False )
    creation_date = Column(Date())
    content = Column(Text())
    token_count = Column(Integer())
    provenance = Column(Text())
    license = Column(Text())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    
    
    # ManyToMany
    is_about = relationship( "InformationContentEntity", secondary="Note_is_about", back_populates="has_notes")
    
    
    xref_rel = relationship( "NoteXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: NoteXref(xref=x_))
    
    
    # ManyToMany
    has_notes = relationship( "Note", 
                             secondary="Note_has_notes", 
                             primaryjoin="Note.id==Note_has_notes.c.Note_id",
                             secondaryjoin="Note.id==Note_has_notes.c.has_notes_id",
                             back_populates="is_about")
    
    
    iri_rel = relationship( "NoteIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: NoteIri(iri=x_))
    

    def __repr__(self):
        return f"Note(format={self.format},type={self.type},creation_date={self.creation_date},content={self.content},token_count={self.token_count},provenance={self.provenance},license={self.license},name={self.name},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True,
        "polymorphic_identity": "Note",
    }    


class Author(InformationContentEntity):
    """
    
    """
    __tablename__ = 'Author'

    creation_date = Column(Date())
    content = Column(Text())
    token_count = Column(Integer())
    format = Column(Text())
    provenance = Column(Text())
    license = Column(Text())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    
    
    # ManyToMany
    affiliations = relationship( "Organization", secondary="Author_affiliations")
    
    
    # ManyToMany
    is_author_of = relationship( "ScientificKnowledgeExpression", secondary="Author_is_author_of")
    
    
    xref_rel = relationship( "AuthorXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: AuthorXref(xref=x_))
    
    
    # ManyToMany
    has_notes = relationship( "Note", secondary="Author_has_notes", back_populates="is_about")
    
    
    iri_rel = relationship( "AuthorIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: AuthorIri(iri=x_))
    

    def __repr__(self):
        return f"Author(creation_date={self.creation_date},content={self.content},token_count={self.token_count},format={self.format},provenance={self.provenance},license={self.license},name={self.name},id={self.id},type={self.type},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True,
        "polymorphic_identity": "Author",
    }    


class Organization(InformationContentEntity):
    """
    
    """
    __tablename__ = 'Organization'

    creation_date = Column(Date())
    content = Column(Text())
    token_count = Column(Integer())
    format = Column(Text())
    provenance = Column(Text())
    license = Column(Text())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    
    
    # ManyToMany
    city = relationship( "City", secondary="Organization_city")
    
    
    # ManyToMany
    country = relationship( "Country", secondary="Organization_country")
    
    
    xref_rel = relationship( "OrganizationXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: OrganizationXref(xref=x_))
    
    
    # ManyToMany
    has_notes = relationship( "Note", secondary="Organization_has_notes", back_populates="is_about")
    
    
    iri_rel = relationship( "OrganizationIri" )
    iri = association_proxy("iri_rel", "iri",
                                  creator=lambda x_: OrganizationIri(iri=x_))
    

    def __repr__(self):
        return f"Organization(creation_date={self.creation_date},content={self.content},token_count={self.token_count},format={self.format},provenance={self.provenance},license={self.license},name={self.name},id={self.id},type={self.type},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True,
        "polymorphic_identity": "Organization",
    }    


