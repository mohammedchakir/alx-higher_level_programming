#!/usr/bin/python3
"""
This script deletes all State objects that have a name containing the letter
'a' from the database hbtn_0e_6_usa. It takes three arguments: MySQL username,
MySQL password, and database name.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def delete_states_with_a(username, password, db_name):
    """
    Deletes all State objects with names containing the letter 'a'.
    """
    engine = create_engine(f'mysql+mysqldb://
            {username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%'))
    for state in states_with_a:
        session.delete(state)
    session.commit()

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
