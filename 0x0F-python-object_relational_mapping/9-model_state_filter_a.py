#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa
    using sqlalchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format
                           (argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).\
        filter(State.name.like("%a%"))
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()
