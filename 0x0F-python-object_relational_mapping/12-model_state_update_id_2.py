#!/usr/bin/python3
"""
A script that changes the name
of a State object from the database hbtn_0e_6_usa
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
    Session = sessionmaker(autoflush=False, bind=engine)
    session = Session()
    result = session.query(State).filter(State.id == 2).first()

    result.name = "New Mexico"
    session.commit()
    session.close()
