#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
in the hbtn_0e_100_usa database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    new_state = State(name='California')
    new_city = City(name='San Francisco')

    session.add(new_state)
    session.add(new_city)
    session.commit()

    session.close()
