import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    dateSign = Column(String(250), nullable=False)

    favorites_id = Column(Integer, ForeignKey('favorites.id'), nullable=False)
    comment_id = Column(Integer, ForeignKey('comment.id'), nullable=False)

    def sign():
        return {}
    def updateProfile():
        return {}
    def likePost():
        return {}
    def addFavorite():
        return {}
    def quitFavorite():
        return {}
    def comment():
        return {}
    def logOut():
        return {}
    def notLikePost():
        return {}

# class Admin(Base):
#     __tablename__ = 'admin'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     password = Column(String(250), nullable=False)
#     email = Column(String(250), nullable=False)
#     dateSign = Column(String(250), nullable=False)
#     def mod():
#         return {}

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    listFavorites = Column(String(250), nullable=False)
    
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    films_id = Column(Integer, ForeignKey('films.id'), nullable=False)
    species_id = Column(Integer, ForeignKey('species.id'), nullable=False)
    starships_id = Column(Integer, ForeignKey('starships.id'), nullable=False)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True) 
    comment = Column(String(250), nullable=False)
    ofUser = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    species = Column(String, nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    homeWorld = Column(String(250), nullable=False)
    related_films = Column(String(250), nullable=False)
    related_vehicles = Column(String(250), nullable=False)
    related_starships = Column(String(250), nullable=False)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True) 
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    class_ = Column(String(250), nullable=False)
    cost = Column(String(250), nullable=False)
    speed = Column(String(250), nullable=False)
    hyperdrive_rating = Column(String(250), nullable=False)
    mglt = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    mimimum = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    related_films = Column(String(250), nullable=False)
    related_pilots = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True) 
    name = Column(String(250), nullable=False)
    populaton = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    terrain_grasslands = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')