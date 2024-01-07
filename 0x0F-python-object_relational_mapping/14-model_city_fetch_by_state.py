#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


def list_cities_by_state(username, password, db_name):
    """
    Prints all City objects, sorted by city id, along with their state names.
    """
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).join(State).order_by(City.id).all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
