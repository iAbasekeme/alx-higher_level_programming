#!/usr/bin/python3
"""
A python script to build a  city class from a Base class
"""
from model_state import Base
from sqlalchemy import *


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, Primary_Key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(states.id), nullable=False)
