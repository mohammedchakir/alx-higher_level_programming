#!/usr/bin/python3
"""
Creates the State 'California' with the City 'San Francisco'
in the database hbtn_0e_100_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


def create_california_with_sf(username, password, db_name):
    """
    Creates 'California' state with 'San Francisco' city.
    """
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_state)
    session.add(new_city)
    session.commit()

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        create_california_with_sf(sys.argv[1], sys.argv[2], sys.argv[3])
