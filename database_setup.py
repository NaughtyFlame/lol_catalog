from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Region(Base):
    __tablename__ = 'region'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    slug = Column(String(250))
    description = Column(String(500))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name'          : self.name,
            'id'            : self.id,
            'slug'          : self.slug,
            'description'   : self.description
        }

class Champion(Base):
    __tablename__ = 'champion'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    slug = Column(String(250))
    description = Column(String(500))
    role = Column(String(16))
    pic_url = Column(String(250))
    info_url = Column(String(250))
    region_id = Column(Integer, ForeignKey('region.id'))
    region = relationship(Region)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id'            : self.id,
            'name'          : self.name,
            'slug'          : self.slug,
            'description'   : self.description,
            'role'          : self.role,
            'pic_url'       : self.pic_url,
            'info_url'      : self.info_url
        }

engine = create_engine('sqlite:///regionchampion.db')


Base.metadata.create_all(engine)
