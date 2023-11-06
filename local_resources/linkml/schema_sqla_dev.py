
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
    type_str = Column(Text())
    
    
    type_rel = relationship( "EntityType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: EntityType(type=x_))
    

    def __repr__(self):
        return f"Entity(id={self.id},iri={self.iri},type_str={self.type_str},)"



    


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



    


class InformationContentEntityProvenance(Base):
    """
    
    """
    __tablename__ = 'InformationContentEntity_provenance'

    InformationContentEntity_id = Column(Text(), ForeignKey('InformationContentEntity.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationContentEntity_provenance(InformationContentEntity_id={self.InformationContentEntity_id},provenance_id={self.provenance_id},)"



    


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



    


class ScientificKnowledgeExpressionProvenance(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeExpression_provenance'

    ScientificKnowledgeExpression_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeExpression_provenance(ScientificKnowledgeExpression_id={self.ScientificKnowledgeExpression_id},provenance_id={self.provenance_id},)"



    


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



    


class ScientificPublicationProvenance(Base):
    """
    
    """
    __tablename__ = 'ScientificPublication_provenance'

    ScientificPublication_id = Column(Text(), ForeignKey('ScientificPublication.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPublication_provenance(ScientificPublication_id={self.ScientificPublication_id},provenance_id={self.provenance_id},)"



    


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



    


class InformationResourceXref(Base):
    """
    
    """
    __tablename__ = 'InformationResource_xref'

    InformationResource_id = Column(Text(), ForeignKey('InformationResource.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationResource_xref(InformationResource_id={self.InformationResource_id},xref={self.xref},)"



    


class InformationResourceProvenance(Base):
    """
    
    """
    __tablename__ = 'InformationResource_provenance'

    InformationResource_id = Column(Text(), ForeignKey('InformationResource.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"InformationResource_provenance(InformationResource_id={self.InformationResource_id},provenance_id={self.provenance_id},)"



    


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



    


class ScientificKnowledgeCollectionProvenance(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeCollection_provenance'

    ScientificKnowledgeCollection_id = Column(Text(), ForeignKey('ScientificKnowledgeCollection.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeCollection_provenance(ScientificKnowledgeCollection_id={self.ScientificKnowledgeCollection_id},provenance_id={self.provenance_id},)"



    


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



    


class ScientificPublicationCollectionProvenance(Base):
    """
    
    """
    __tablename__ = 'ScientificPublicationCollection_provenance'

    ScientificPublicationCollection_id = Column(Text(), ForeignKey('ScientificPublicationCollection.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificPublicationCollection_provenance(ScientificPublicationCollection_id={self.ScientificPublicationCollection_id},provenance_id={self.provenance_id},)"



    


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



    


class ScientificKnowledgeFragmentProvenance(Base):
    """
    
    """
    __tablename__ = 'ScientificKnowledgeFragment_provenance'

    ScientificKnowledgeFragment_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"ScientificKnowledgeFragment_provenance(ScientificKnowledgeFragment_id={self.ScientificKnowledgeFragment_id},provenance_id={self.provenance_id},)"



    


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



    


class SelectorProvenance(Base):
    """
    
    """
    __tablename__ = 'Selector_provenance'

    Selector_id = Column(Text(), ForeignKey('Selector.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"Selector_provenance(Selector_id={self.Selector_id},provenance_id={self.provenance_id},)"



    


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



    


class OffsetTextSelectorProvenance(Base):
    """
    
    """
    __tablename__ = 'OffsetTextSelector_provenance'

    OffsetTextSelector_id = Column(Text(), ForeignKey('OffsetTextSelector.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"OffsetTextSelector_provenance(OffsetTextSelector_id={self.OffsetTextSelector_id},provenance_id={self.provenance_id},)"



    


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



    


class NoteIsAbout(Base):
    """
    
    """
    __tablename__ = 'Note_is_about'

    Note_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    is_about_id = Column(Text(), ForeignKey('Entity.id'), primary_key=True)
    

    def __repr__(self):
        return f"Note_is_about(Note_id={self.Note_id},is_about_id={self.is_about_id},)"



    


class NoteProvenance(Base):
    """
    
    """
    __tablename__ = 'Note_provenance'

    Note_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"Note_provenance(Note_id={self.Note_id},provenance_id={self.provenance_id},)"



    


class NoteXref(Base):
    """
    
    """
    __tablename__ = 'Note_xref'

    Note_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Note_xref(Note_id={self.Note_id},xref={self.xref},)"



    


class NoteType(Base):
    """
    
    """
    __tablename__ = 'Note_type'

    Note_id = Column(Text(), ForeignKey('Note.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Note_type(Note_id={self.Note_id},type={self.type},)"



    


class NameValuePairIsAbout(Base):
    """
    
    """
    __tablename__ = 'NameValuePair_is_about'

    NameValuePair_id = Column(Text(), ForeignKey('NameValuePair.id'), primary_key=True)
    is_about_id = Column(Text(), ForeignKey('Entity.id'), primary_key=True)
    

    def __repr__(self):
        return f"NameValuePair_is_about(NameValuePair_id={self.NameValuePair_id},is_about_id={self.is_about_id},)"



    


class NameValuePairProvenance(Base):
    """
    
    """
    __tablename__ = 'NameValuePair_provenance'

    NameValuePair_id = Column(Text(), ForeignKey('NameValuePair.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"NameValuePair_provenance(NameValuePair_id={self.NameValuePair_id},provenance_id={self.provenance_id},)"



    


class NameValuePairXref(Base):
    """
    
    """
    __tablename__ = 'NameValuePair_xref'

    NameValuePair_id = Column(Text(), ForeignKey('NameValuePair.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"NameValuePair_xref(NameValuePair_id={self.NameValuePair_id},xref={self.xref},)"



    


class NameValuePairType(Base):
    """
    
    """
    __tablename__ = 'NameValuePair_type'

    NameValuePair_id = Column(Text(), ForeignKey('NameValuePair.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"NameValuePair_type(NameValuePair_id={self.NameValuePair_id},type={self.type},)"



    


class NoteAboutProvenanceIsAbout(Base):
    """
    
    """
    __tablename__ = 'NoteAboutProvenance_is_about'

    NoteAboutProvenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    is_about_id = Column(Text(), ForeignKey('InformationContentEntity.id'), primary_key=True)
    

    def __repr__(self):
        return f"NoteAboutProvenance_is_about(NoteAboutProvenance_id={self.NoteAboutProvenance_id},is_about_id={self.is_about_id},)"



    


class NoteAboutProvenanceProvenance(Base):
    """
    
    """
    __tablename__ = 'NoteAboutProvenance_provenance'

    NoteAboutProvenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"NoteAboutProvenance_provenance(NoteAboutProvenance_id={self.NoteAboutProvenance_id},provenance_id={self.provenance_id},)"



    


class NoteAboutProvenanceXref(Base):
    """
    
    """
    __tablename__ = 'NoteAboutProvenance_xref'

    NoteAboutProvenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"NoteAboutProvenance_xref(NoteAboutProvenance_id={self.NoteAboutProvenance_id},xref={self.xref},)"



    


class NoteAboutProvenanceType(Base):
    """
    
    """
    __tablename__ = 'NoteAboutProvenance_type'

    NoteAboutProvenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"NoteAboutProvenance_type(NoteAboutProvenance_id={self.NoteAboutProvenance_id},type={self.type},)"



    


class NoteAboutPublicationIsAbout(Base):
    """
    
    """
    __tablename__ = 'NoteAboutPublication_is_about'

    NoteAboutPublication_id = Column(Text(), ForeignKey('NoteAboutPublication.id'), primary_key=True)
    is_about_id = Column(Text(), ForeignKey('ScientificPublication.id'), primary_key=True)
    

    def __repr__(self):
        return f"NoteAboutPublication_is_about(NoteAboutPublication_id={self.NoteAboutPublication_id},is_about_id={self.is_about_id},)"



    


class NoteAboutPublicationProvenance(Base):
    """
    
    """
    __tablename__ = 'NoteAboutPublication_provenance'

    NoteAboutPublication_id = Column(Text(), ForeignKey('NoteAboutPublication.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"NoteAboutPublication_provenance(NoteAboutPublication_id={self.NoteAboutPublication_id},provenance_id={self.provenance_id},)"



    


class NoteAboutPublicationXref(Base):
    """
    
    """
    __tablename__ = 'NoteAboutPublication_xref'

    NoteAboutPublication_id = Column(Text(), ForeignKey('NoteAboutPublication.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"NoteAboutPublication_xref(NoteAboutPublication_id={self.NoteAboutPublication_id},xref={self.xref},)"



    


class NoteAboutPublicationType(Base):
    """
    
    """
    __tablename__ = 'NoteAboutPublication_type'

    NoteAboutPublication_id = Column(Text(), ForeignKey('NoteAboutPublication.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"NoteAboutPublication_type(NoteAboutPublication_id={self.NoteAboutPublication_id},type={self.type},)"



    


class NoteAboutFragmentIsAbout(Base):
    """
    
    """
    __tablename__ = 'NoteAboutFragment_is_about'

    NoteAboutFragment_id = Column(Text(), ForeignKey('NoteAboutFragment.id'), primary_key=True)
    is_about_id = Column(Text(), ForeignKey('ScientificKnowledgeFragment.id'), primary_key=True)
    

    def __repr__(self):
        return f"NoteAboutFragment_is_about(NoteAboutFragment_id={self.NoteAboutFragment_id},is_about_id={self.is_about_id},)"



    


class NoteAboutFragmentProvenance(Base):
    """
    
    """
    __tablename__ = 'NoteAboutFragment_provenance'

    NoteAboutFragment_id = Column(Text(), ForeignKey('NoteAboutFragment.id'), primary_key=True)
    provenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'), primary_key=True)
    

    def __repr__(self):
        return f"NoteAboutFragment_provenance(NoteAboutFragment_id={self.NoteAboutFragment_id},provenance_id={self.provenance_id},)"



    


class NoteAboutFragmentXref(Base):
    """
    
    """
    __tablename__ = 'NoteAboutFragment_xref'

    NoteAboutFragment_id = Column(Text(), ForeignKey('NoteAboutFragment.id'), primary_key=True)
    xref = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"NoteAboutFragment_xref(NoteAboutFragment_id={self.NoteAboutFragment_id},xref={self.xref},)"



    


class NoteAboutFragmentType(Base):
    """
    
    """
    __tablename__ = 'NoteAboutFragment_type'

    NoteAboutFragment_id = Column(Text(), ForeignKey('NoteAboutFragment.id'), primary_key=True)
    type = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"NoteAboutFragment_type(NoteAboutFragment_id={self.NoteAboutFragment_id},type={self.type},)"



    


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
    type_str = Column(Text())
    
    
    xref_rel = relationship( "NamedThingXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: NamedThingXref(xref=x_))
    
    
    type_rel = relationship( "NamedThingType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: NamedThingType(type=x_))
    

    def __repr__(self):
        return f"NamedThing(name={self.name},id={self.id},iri={self.iri},type_str={self.type_str},)"



    
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
    type_str = Column(Text())
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="InformationContentEntity_provenance")
    
    
    xref_rel = relationship( "InformationContentEntityXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: InformationContentEntityXref(xref=x_))
    
    
    type_rel = relationship( "InformationContentEntityType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: InformationContentEntityType(type=x_))
    

    def __repr__(self):
        return f"InformationContentEntity(license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},id={self.id},iri={self.iri},type_str={self.type_str},)"



    
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
    type_str = Column(Text())
    
    
    xref_rel = relationship( "PersonXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: PersonXref(xref=x_))
    
    
    type_rel = relationship( "PersonType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: PersonType(type=x_))
    

    def __repr__(self):
        return f"Person(name={self.name},id={self.id},iri={self.iri},type_str={self.type_str},)"



    
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
    type_str = Column(Text())
    
    
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
        return f"Organization(name={self.name},id={self.id},iri={self.iri},type_str={self.type_str},)"



    
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
    type_str = Column(Text())
    
    
    xref_rel = relationship( "CityXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: CityXref(xref=x_))
    
    
    type_rel = relationship( "CityType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: CityType(type=x_))
    

    def __repr__(self):
        return f"City(name={self.name},id={self.id},iri={self.iri},type_str={self.type_str},)"



    
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
    type_str = Column(Text())
    
    
    xref_rel = relationship( "CountryXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: CountryXref(xref=x_))
    
    
    type_rel = relationship( "CountryType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: CountryType(type=x_))
    

    def __repr__(self):
        return f"Country(name={self.name},id={self.id},iri={self.iri},type_str={self.type_str},)"



    
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
    publication_date = Column(Date())
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    iri = Column(Text())
    type_str = Column(Text())
    
    
    # ManyToMany
    has_part = relationship( "ScientificKnowledgeFragment", secondary="ScientificKnowledgeExpression_has_part")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ScientificKnowledgeExpression', source_slot='authors', mapping_type=None, target_class='Author', target_slot='ScientificKnowledgeExpression_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.ScientificKnowledgeExpression_id]")
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="ScientificKnowledgeExpression_provenance")
    
    
    xref_rel = relationship( "ScientificKnowledgeExpressionXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificKnowledgeExpressionXref(xref=x_))
    
    
    type_rel = relationship( "ScientificKnowledgeExpressionType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificKnowledgeExpressionType(type=x_))
    

    def __repr__(self):
        return f"ScientificKnowledgeExpression(id={self.id},title={self.title},abstract={self.abstract},publication_date={self.publication_date},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},iri={self.iri},type_str={self.type_str},)"



    
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
    type_str = Column(Text())
    
    
    xref_rel = relationship( "InformationResourceXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: InformationResourceXref(xref=x_))
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="InformationResource_provenance")
    
    
    type_rel = relationship( "InformationResourceType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: InformationResourceType(type=x_))
    

    def __repr__(self):
        return f"InformationResource(id={self.id},name={self.name},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},iri={self.iri},type_str={self.type_str},)"



    
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
    type_str = Column(Text())
    
    
    # ManyToMany
    information_sources = relationship( "InformationResource", secondary="ScientificKnowledgeCollection_information_sources")
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="ScientificKnowledgeCollection_provenance")
    
    
    xref_rel = relationship( "ScientificKnowledgeCollectionXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificKnowledgeCollectionXref(xref=x_))
    
    
    type_rel = relationship( "ScientificKnowledgeCollectionType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificKnowledgeCollectionType(type=x_))
    

    def __repr__(self):
        return f"ScientificKnowledgeCollection(id={self.id},name={self.name},logical_query={self.logical_query},creation_date={self.creation_date},license={self.license},rights={self.rights},format={self.format},iri={self.iri},type_str={self.type_str},)"



    
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
    type_str = Column(Text())
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="ScientificKnowledgeFragment_provenance")
    
    
    xref_rel = relationship( "ScientificKnowledgeFragmentXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificKnowledgeFragmentXref(xref=x_))
    
    
    type_rel = relationship( "ScientificKnowledgeFragmentType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificKnowledgeFragmentType(type=x_))
    

    def __repr__(self):
        return f"ScientificKnowledgeFragment(part_of={self.part_of},selector={self.selector},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},id={self.id},iri={self.iri},type_str={self.type_str},)"



    
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
    type_str = Column(Text())
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="Selector_provenance")
    
    
    xref_rel = relationship( "SelectorXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: SelectorXref(xref=x_))
    
    
    type_rel = relationship( "SelectorType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: SelectorType(type=x_))
    

    def __repr__(self):
        return f"Selector(license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},id={self.id},iri={self.iri},type_str={self.type_str},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Note(InformationContentEntity):
    """
    A structured piece of information with an author that is about another InformationContentEntity.
    """
    __tablename__ = 'Note'

    format = Column(Text())
    type_str = Column(Enum('NoteAboutProvenance', 'NoteAboutPublication', 'NoteAboutFragment', name='NoteType'))
    license = Column(Text())
    rights = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    # ManyToMany
    is_about = relationship( "Entity", secondary="Note_is_about")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Note', source_slot='authors', mapping_type=None, target_class='Author', target_slot='Note_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.Note_id]")
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="Note_provenance")
    
    
    xref_rel = relationship( "NoteXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: NoteXref(xref=x_))
    
    
    type_rel = relationship( "NoteType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: NoteType(type=x_))
    

    def __repr__(self):
        return f"Note(format={self.format},type_str={self.type_str},license={self.license},rights={self.rights},creation_date={self.creation_date},name={self.name},id={self.id},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class NameValuePair(InformationContentEntity):
    """
    A single map {string :- string} to track structured data in a note.
    """
    __tablename__ = 'NameValuePair'

    format = Column(Text())
    license = Column(Text())
    rights = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    type_str = Column(Text())
    
    
    # ManyToMany
    is_about = relationship( "Entity", secondary="NameValuePair_is_about")
    
    
    # One-To-Many: OneToAnyMapping(source_class='NameValuePair', source_slot='authors', mapping_type=None, target_class='Author', target_slot='NameValuePair_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.NameValuePair_id]")
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="NameValuePair_provenance")
    
    
    xref_rel = relationship( "NameValuePairXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: NameValuePairXref(xref=x_))
    
    
    type_rel = relationship( "NameValuePairType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: NameValuePairType(type=x_))
    

    def __repr__(self):
        return f"NameValuePair(format={self.format},license={self.license},rights={self.rights},creation_date={self.creation_date},name={self.name},id={self.id},iri={self.iri},type_str={self.type_str},)"



    
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
    type_str = Column(Text())
    ScientificKnowledgeExpression_id = Column(Text(), ForeignKey('ScientificKnowledgeExpression.id'))
    ScientificPublication_id = Column(Text(), ForeignKey('ScientificPublication.id'))
    Note_id = Column(Text(), ForeignKey('Note.id'))
    NameValuePair_id = Column(Text(), ForeignKey('NameValuePair.id'))
    NoteAboutProvenance_id = Column(Text(), ForeignKey('NoteAboutProvenance.id'))
    NoteAboutPublication_id = Column(Text(), ForeignKey('NoteAboutPublication.id'))
    NoteAboutFragment_id = Column(Text(), ForeignKey('NoteAboutFragment.id'))
    
    
    # ManyToMany
    affiliations = relationship( "Organization", secondary="Author_affiliations")
    
    
    xref_rel = relationship( "AuthorXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: AuthorXref(xref=x_))
    
    
    type_rel = relationship( "AuthorType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: AuthorType(type=x_))
    

    def __repr__(self):
        return f"Author(orcid={self.orcid},name={self.name},id={self.id},iri={self.iri},type_str={self.type_str},ScientificKnowledgeExpression_id={self.ScientificKnowledgeExpression_id},ScientificPublication_id={self.ScientificPublication_id},Note_id={self.Note_id},NameValuePair_id={self.NameValuePair_id},NoteAboutProvenance_id={self.NoteAboutProvenance_id},NoteAboutPublication_id={self.NoteAboutPublication_id},NoteAboutFragment_id={self.NoteAboutFragment_id},)"



    
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
    type_str = Column(Enum('ScientificPrimaryResearchArticle', 'ScientificPrimaryResearchPreprint', 'ScientificReviewArticle', 'ScientificBook', 'ScientificBookChapter', 'ScientificConferenceArticle', 'ScientificDissertation', name='ScientificPublicationType'))
    id = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text())
    abstract = Column(Text())
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
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="ScientificPublication_provenance")
    
    
    xref_rel = relationship( "ScientificPublicationXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificPublicationXref(xref=x_))
    
    
    type_rel = relationship( "ScientificPublicationType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificPublicationType(type=x_))
    

    def __repr__(self):
        return f"ScientificPublication(doi={self.doi},type_str={self.type_str},id={self.id},title={self.title},abstract={self.abstract},publication_date={self.publication_date},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
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
    type_str = Column(Text())
    
    
    # ManyToMany
    has_part = relationship( "ScientificPublication", secondary="ScientificPublicationCollection_has_part")
    
    
    # ManyToMany
    information_sources = relationship( "InformationResource", secondary="ScientificPublicationCollection_information_sources")
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="ScientificPublicationCollection_provenance")
    
    
    xref_rel = relationship( "ScientificPublicationCollectionXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: ScientificPublicationCollectionXref(xref=x_))
    
    
    type_rel = relationship( "ScientificPublicationCollectionType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: ScientificPublicationCollectionType(type=x_))
    

    def __repr__(self):
        return f"ScientificPublicationCollection(id={self.id},name={self.name},logical_query={self.logical_query},creation_date={self.creation_date},license={self.license},rights={self.rights},format={self.format},iri={self.iri},type_str={self.type_str},)"



    
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
    license = Column(Text())
    rights = Column(Text())
    format = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    type_str = Column(Text())
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="OffsetTextSelector_provenance")
    
    
    xref_rel = relationship( "OffsetTextSelectorXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: OffsetTextSelectorXref(xref=x_))
    
    
    type_rel = relationship( "OffsetTextSelectorType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: OffsetTextSelectorType(type=x_))
    

    def __repr__(self):
        return f"OffsetTextSelector(offset={self.offset},length={self.length},license={self.license},rights={self.rights},format={self.format},creation_date={self.creation_date},name={self.name},id={self.id},iri={self.iri},type_str={self.type_str},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class NoteAboutProvenance(Note):
    """
    A note that describes the provenance of an InformationContentEntity by describing its source, when it was created and any other salient details written in natural language.
    """
    __tablename__ = 'NoteAboutProvenance'

    format = Column(Text())
    type_str = Column(Enum('NoteAboutProvenance', 'NoteAboutPublication', 'NoteAboutFragment', name='NoteType'))
    license = Column(Text())
    rights = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    # ManyToMany
    is_about = relationship( "InformationContentEntity", secondary="NoteAboutProvenance_is_about")
    
    
    # One-To-Many: OneToAnyMapping(source_class='NoteAboutProvenance', source_slot='authors', mapping_type=None, target_class='Author', target_slot='NoteAboutProvenance_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.NoteAboutProvenance_id]")
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="NoteAboutProvenance_provenance")
    
    
    xref_rel = relationship( "NoteAboutProvenanceXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: NoteAboutProvenanceXref(xref=x_))
    
    
    type_rel = relationship( "NoteAboutProvenanceType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: NoteAboutProvenanceType(type=x_))
    

    def __repr__(self):
        return f"NoteAboutProvenance(format={self.format},type_str={self.type_str},license={self.license},rights={self.rights},creation_date={self.creation_date},name={self.name},id={self.id},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class NoteAboutPublication(Note):
    """
    A structured note about an ScientificPublication.
    """
    __tablename__ = 'NoteAboutPublication'

    format = Column(Text())
    type_str = Column(Enum('NoteAboutProvenance', 'NoteAboutPublication', 'NoteAboutFragment', name='NoteType'))
    license = Column(Text())
    rights = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    # ManyToMany
    is_about = relationship( "ScientificPublication", secondary="NoteAboutPublication_is_about")
    
    
    # One-To-Many: OneToAnyMapping(source_class='NoteAboutPublication', source_slot='authors', mapping_type=None, target_class='Author', target_slot='NoteAboutPublication_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.NoteAboutPublication_id]")
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="NoteAboutPublication_provenance")
    
    
    xref_rel = relationship( "NoteAboutPublicationXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: NoteAboutPublicationXref(xref=x_))
    
    
    type_rel = relationship( "NoteAboutPublicationType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: NoteAboutPublicationType(type=x_))
    

    def __repr__(self):
        return f"NoteAboutPublication(format={self.format},type_str={self.type_str},license={self.license},rights={self.rights},creation_date={self.creation_date},name={self.name},id={self.id},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class NoteAboutFragment(Note):
    """
    A structured note about an ScientificKnowledgeFragment.
    """
    __tablename__ = 'NoteAboutFragment'

    format = Column(Text())
    type_str = Column(Enum('NoteAboutProvenance', 'NoteAboutPublication', 'NoteAboutFragment', name='NoteType'))
    license = Column(Text())
    rights = Column(Text())
    creation_date = Column(Date())
    name = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    iri = Column(Text())
    
    
    # ManyToMany
    is_about = relationship( "ScientificKnowledgeFragment", secondary="NoteAboutFragment_is_about")
    
    
    # One-To-Many: OneToAnyMapping(source_class='NoteAboutFragment', source_slot='authors', mapping_type=None, target_class='Author', target_slot='NoteAboutFragment_id', join_class=None, uses_join_table=None, multivalued=False)
    authors = relationship( "Author", foreign_keys="[Author.NoteAboutFragment_id]")
    
    
    # ManyToMany
    provenance = relationship( "NoteAboutProvenance", secondary="NoteAboutFragment_provenance")
    
    
    xref_rel = relationship( "NoteAboutFragmentXref" )
    xref = association_proxy("xref_rel", "xref",
                                  creator=lambda x_: NoteAboutFragmentXref(xref=x_))
    
    
    type_rel = relationship( "NoteAboutFragmentType" )
    type = association_proxy("type_rel", "type",
                                  creator=lambda x_: NoteAboutFragmentType(type=x_))
    

    def __repr__(self):
        return f"NoteAboutFragment(format={self.format},type_str={self.type_str},license={self.license},rights={self.rights},creation_date={self.creation_date},name={self.name},id={self.id},iri={self.iri},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


