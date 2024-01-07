#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa.
It takes three arguments: MySQL username, MySQL password, and database name.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def list_states(username, password, db_name):
    """
    Lists all State objects from the database in ascending order by states.id.
    """
    engine = create_engine(f'mysql+mysqldb://
            {username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
