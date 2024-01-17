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
    """Fucntion should not execute if imported
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]))

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
state = session.query(State).order_by(State.id).first()
if state:
    for instance in state:
        print(f"{state.id}: {state.name}")
    else:
        print('Nothing')