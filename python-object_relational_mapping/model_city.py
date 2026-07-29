#!/usr/bin/python3
"""Module that defines the City class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City class that links to the MySQL table cities.

    Attributes:
        id: Auto-generated unique integer, primary key, can't be null.
        name: String with max 128 characters, can't be null.
        state_id: Foreign key to states.id, can't be null.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
