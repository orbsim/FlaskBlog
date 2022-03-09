from sqlalchemy import Column, Integer, String
from app import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, Unique=True)
    description = Column(String(256), nullable=True, Unique=False)
    slug = Column(String(128), nullable=False, Unique=True)

class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False, Unique=True)
    summary = Column(String(256), nullable=True, Unique=False)
    context = Column(Text, nullable=False, Unique=False)
    slug = Column(String(128), nullable=False, Unique=True)