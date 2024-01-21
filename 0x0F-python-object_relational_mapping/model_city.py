#!/usr/bin/python3
"""
module city
"""
from model_state import Base
from sqlalchemy import *


class City(Base):
    """
    A city class that will define the cities table
    """
    __tablename__ = 'cities'
    id = Column(Integer, Primary_Key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
