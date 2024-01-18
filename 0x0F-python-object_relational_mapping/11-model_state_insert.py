#!/usr/bin/python3
"""
script that adds the
State object “Louisiana” to the database hbtn_0e_6_usa
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
    Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
    session = Session()
    state = State(name='Louisiana')

    session.add(state)

    session.commit()
    session.close()
    added_state = session.quey(State).filter(State.name == 'Louisiana').first()
    print(f"{added_state.id}")
