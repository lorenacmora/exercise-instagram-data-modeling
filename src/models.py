import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    usuario = Column(String(25), nullable=False)
    nombre = Column(String(25), nullable=False)
    apellido = Column(String(25), nullable=False)
    correo = Column(String(25), unique=True)

class Seguidor(Base):
    __tablename__ = 'seguidor'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class Comentarios(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    comentario_text = Column(String(25))
    autor_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))


    def to_dict(self):
        return {}




render_er(Base, 'diagram.png')