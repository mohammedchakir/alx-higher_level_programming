#!/usr/bin/python3
"""
This script lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State  # Ensure these are the updated versions with relationships
import sys

def list_states_and_cities(username, password, db_name):
    """
    Lists all State objects and their corresponding City objects from the database.
    """
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id, State.cities).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states_and_cities(sys.argv[1], sys.argv[2], sys.argv[3])
