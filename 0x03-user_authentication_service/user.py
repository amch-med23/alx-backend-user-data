#!/usr/bin/env python3
""" a sql alchemy model """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import logging

Base = declarative_base()

logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)


class User(Base):
    """ the User class """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
