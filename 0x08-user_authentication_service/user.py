#!/usr/bin/env python3
""" User declarative base alchemy model module. """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
class User(Base):
    """ Declarative Alchemy Base class model. """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

    def __repr__(self):
        """ Representation of the User class model. """
        return "<User(name='{}', fullname='{}', nickname='{}')>".format(
            self.name, self.fullname, self.nickname
        )
