#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa
    using sqlalchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sys import argv
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format
                           (argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    cities = session.query(City, State).filter(City.state_id == State.id).\
        order_by(City.id).all()

    for city, state in cities:
        print(f"{state.name}: {city.id} {city.name}")

    session.close()
