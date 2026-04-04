from database import Base
from sqlalchemy import Column, Integer, String, Float, Text

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(50))
    genre = Column(String(100))
    synopsis = Column(Text)
    price = Column(Float)
    cover = Column(String(255))
    link = Column(String(300))

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    avatar = Column(String(255))
    pet = Column(String(255))
    width = Column(Integer)
    emoji = Column(String(10))
    bio = Column(Text)
    account = Column(String(50))
    link = Column(String(100))

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    excerpt = Column(String(255))
    cover = Column(String(255))

class Launch(Base):
    __tablename__ = "launches"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(50))
    genre = Column(String(100))
    cover = Column(String(255))
    bio = Column(Text)

class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    text = Column(Text)

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    img = Column(String(255))
    caption = Column(String(255))