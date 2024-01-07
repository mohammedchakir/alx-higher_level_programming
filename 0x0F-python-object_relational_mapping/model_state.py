#!/usr/bin/python3
"""
This module defines the State class which inherits from Base,
and an instance Base using declarative_base from SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class:
    - Inherits from Base.
    - Links to MySQL table states.
    - Has id and name attributes.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Your code to connect to the database, for example:
    engine = create_engine('mysql+mysqldb://<username>:<password>@localhost:3306/<dbname>')
    Base.metadata.create_all(engine)
