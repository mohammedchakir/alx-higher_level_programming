#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the hbtn_0e_6_usa database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.contains('a'))

    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()
