import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    def serialize(self):
        return{
            "email" : self.email,
            "username" : self.username,
            "password" : self.password,
        }

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    description = Column(String(250))

    def serialize(self):
        return {
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "description": self.description,          
        }
    class Characters(Base):
        __tablename__ = 'characters'
    
        id = Column(Integer, primary_key=True)
        average_height = Column(String(250))
        average_lifespan = Column(String(250))
        eye_colors = Column(String(250), nullable=False)
        hair_colors = Column(String(250))
        skin_colors = Column(String(250))
        language = Column(String(250))
        classification = Column(String(250))
        created = Column(String(250))

    def serialize(self):
        return {
            "average_height": self.average_height,
            "average_lifespan": self.average_lifespan,
            "eye_colors": self.eye_colors,
            "hair_colors": self.hair_colors,
            "skin_colors": self.skin_colors,
            "language": self.language,
            "classification": self.classification,
            "created": self.created,  
        }
    class Vehicles(Base):
        __tablename__ = 'vehicles'
    
        id = Column(Integer, primary_key=True)
        name = Column(String(250))
        model = Column(String(250))
        vehicle_class = Column(String(250), nullable=False)
        manufacturer = Column(String(250))
        crew = Column(String(250))
        length  = Column(String(250))
        passengers = Column(String(250))
        max_atmosphering_speed = Column(String(250))

    def serialize(self):
        return {
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "crew": self.crew,
            "length": self.length,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,  
        }
    
    class Favorites(Base):
        __tablename__ = 'favorites'

        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
        characters = Column(Integer, ForeignKey('characters.id'), nullable=True)
        planets = Column(Integer, ForeignKey('planets.id'), nullable=True)
        vehicles = Column(Integer, ForeignKey('vehicles.id'), nullable=True)

        user = relationship(User)
        characters = relationship(characters)
        planets = relationship(planets)
        vehicles = relationship(vehicles)

        def serialize(self):
            return{
                "user_id": self.user_id,
                "character_id": self.character_id,
                "planet_id": self.planet_id,
                "vehicle_id": self.vehicle_id,

            }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
