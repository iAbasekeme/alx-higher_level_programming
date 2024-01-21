"""
A script that at prints all City
objects from the database hbtn_0e_14_usa
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
    query = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()

    for state, city in query:
        print("{}: {}{}".format(state.name, city.id, city.name))
    session.close()
