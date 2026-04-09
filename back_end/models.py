from database import Base
from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from datetime import datetime, timezone
from sqlalchemy.sql import func

def utc_now():
    return datetime.now(timezone.utc)

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
    # created_at = Column(
    # DateTime(timezone=True),
    # server_default=func.now(),
    # nullable=False
    # ) 
    created_at = Column(DateTime(timezone=True), server_default=func.now())

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
    # created_at = Column(
    # DateTime(timezone=True),
    # server_default=func.now(),
    # nullable=False
    # )
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    excerpt = Column(String(255))
    cover = Column(String(255))
    # created_at = Column(
    # DateTime(timezone=True),
    # server_default=func.now(),
    # nullable=False
    # )
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Launch(Base):
    __tablename__ = "launches"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(50))
    genre = Column(String(100))
    cover = Column(String(255))
    bio = Column(Text)
    # created_at = Column(
    # DateTime(timezone=True),
    # server_default=func.now(),
    # nullable=False
    # ) 
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    text = Column(Text)
    # created_at = Column(
    # DateTime(timezone=True),
    # server_default=func.now(),
    # nullable=False
    # )
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    img = Column(String(255))
    caption = Column(String(255))
    # created_at = Column(
    # DateTime(timezone=True),
    # server_default=func.now(),
    # nullable=False
    # )
    created_at = Column(DateTime(timezone=True), server_default=func.now())