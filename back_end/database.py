import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from dotenv import load_dotenv

DATABASE_URL = os.environ.get('DATABASE_URL')

# SQL LITE (LOCALMENTE)
if not DATABASE_URL:
    DATABASE_URL = 'sqlite:///solielle.db'

if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

engine = create_engine(DATABASE_URL, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

load_dotenv()

def init_db():
    from back_end import models
    Base.metadata.create_all(bind=engine)