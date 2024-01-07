#!/usr/bin/python3
"""
This script changes the name of a State object with id = 2 to 'New Mexico'
in the database hbtn_0e_6_usa. It takes three arguments: MySQL username,
MySQL password, and database name.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def change_state_name(username, password, db_name):
    """
    Changes the name of the State object with id = 2 to 'New Mexico'.
    """
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        change_state_name(sys.argv[1], sys.argv[2], sys.argv[3])
