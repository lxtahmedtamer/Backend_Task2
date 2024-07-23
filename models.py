"""
This file contains the SQLAlchemy models that define the structure of the database tables, 
where SQLAlchemy model defines the database tables and their columns using SQLAlchemy's ORM features
"""
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
    greeting = Column(String, index=True)
