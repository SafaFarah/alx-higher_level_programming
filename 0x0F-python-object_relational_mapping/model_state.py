#!/usr/bin/python3

"""
module that contains the class definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """ State class
        Attributes:
            id:(Interger) an auto-generated ,not null and is a primary key
            name:(String) with maximum 128 char and not  null
    """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
