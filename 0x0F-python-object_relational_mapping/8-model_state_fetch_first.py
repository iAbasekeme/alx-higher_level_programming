#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
fetch all states from the database before displaying the result
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print('Nothing')
