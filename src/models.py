import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(),nullable=False)
    photo = Column(String)
    telephone = Column(Integer,primary_key=True)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    photo = Column (String())
    date = Column(String())
    numero_likes = Column(Integer)
    numero_comentarios = Column(Integer)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Story(Base):
    __tablename__="story"
    id = Column(Integer,primary_key=True)
    story_video= Column(String())
    date= Column(String())
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)    

class Comentarios(Base):
    __tablename__="comentarios"
    id = Column(Integer,primary_key=True)
    content = Column(String)
    person_id = Column(Integer, ForeignKey('person.id'))
    date= Column(String())
    person = relationship(Person) 
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post) 

class Like(Base):
    __tablename__="like"
    id = Column(Integer,primary_key=True)
    like = Column(String)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person) 
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post) 
    comentarios_id = Column(Integer, ForeignKey('comentarios.id'))
    comentarios = relationship(Comentarios) 

class Chat(Base):
    __tablename__="chat"
    id = Column(Integer,primary_key=True)
    mensajes = Column(Integer)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Mensajes(Base):
    __tablename__="mensajes"
    id = Column(Integer,primary_key=True)
    content = Column(String)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    chat_id = Column(Integer, ForeignKey('chat.id'))
    chat = relationship(Chat)

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e