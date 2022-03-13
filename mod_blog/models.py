from sqlalchemy import Column, ForeignKey, Integer, String, Text, Table
from app import db

posts_categories = Table('posts_categories', db.metadata,
    Column('post_id', Integer, ForeignKey('posts.id', ondelete='cascade')),
    Column('category_id', Integer, ForeignKey('categories.id', ondelete='cascade'))
)

class Category(db.Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    description = Column(String(256), nullable=True, unique=False)
    slug = Column(String(128), nullable=False, unique=True)
    posts = db.relationship('Post', secondary=posts_categories, back_populates='categories')


class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False, unique=True)
    summary = Column(String(256), nullable=True, unique=False)
    context = Column(Text, nullable=False, unique=False)
    slug = Column(String(128), nullable=False, unique=True)
    categories = db.relationship('Category', secondary=posts_categories, back_populates='posts')