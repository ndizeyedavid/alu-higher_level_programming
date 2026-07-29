#!/usr/bin/python3
"""Module that defines the State class and an instance of declarative_base."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class that links to the MySQL table states.

    Attributes:
        id: Auto-generated unique integer, primary key, can't be null.
        name: String with max 128 characters, can't be null.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
