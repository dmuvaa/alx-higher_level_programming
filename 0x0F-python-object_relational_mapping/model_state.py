#!/usr/bin/python3

"""Imports a Module"""


from sqlalchemy import Column, String, Integer
from sqlachemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class that inherits from Base"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
