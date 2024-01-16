#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+mysqldb://${argv[1]}:${argv[2]}@localhost:3306/${argv[3]}')

Session = sessionmaker(bind=engine)
session = Session()

for instance in session.query(State).order_by(states.id):
    print(f"{instance.id}: {instance.name}")
