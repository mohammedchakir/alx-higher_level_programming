#!/usr/bin/python3
"""
Lists all State objects and their corresponding City objects
from the hbtn_0e_101_usa database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_cities = session.query(State, City).filter(State.id == City.state_id).order_by(State.id, City.id).all()

    for state, city in states_cities:
        print("{}: {}".format(state.id, state.name))
        print("\t{}: {}".format(city.id, city.name))

    session.close()
