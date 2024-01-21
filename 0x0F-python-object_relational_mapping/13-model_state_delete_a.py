#!/usr/bin/python3
"""
A script that deletes all State objects with
a name containing the letter a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(autoflush=False, bind=engine)
    session = Session()
    result = delete(State).where(State.name.ilike('%a%'))
    session.commit()
    session.close()
