from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, DateTime

import settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_articles_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

class Articles(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    content = Column('content', String, nullable=True)
    desc = Column('desc', String, nullable=True)
    url = Column('url', String, nullable=True)
    category = Column('category', String, nullable=True)
    avatar = Column('avatar', String, nullable=True)
    published_time = Column('published_time', DateTime, nullable=True)
    modified_time = Column('modified_time', DateTime, nullable=True)
