#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa. It takes four arguments: MySQL username,
MySQL password, database name, and state name to search.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def print_state_by_name(username, password, db_name, state_name):
    """
    Prints the State object with the specified name from the database.
    """
    engine = create_engine(f'mysql+mysqldb://
            {username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        print_state_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
