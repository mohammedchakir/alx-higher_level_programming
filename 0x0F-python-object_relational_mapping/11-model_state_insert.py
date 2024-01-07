#!/usr/bin/python3
"""
This script adds the State object "Louisiana" to the database hbtn_0e_6_usa.
It takes three arguments: MySQL username, MySQL password, and database name.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def add_louisiana_state(username, password, db_name):
    """
    Adds the State object "Louisiana" to the database and prints its id.
    """
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        add_louisiana_state(sys.argv[1], sys.argv[2], sys.argv[3])
