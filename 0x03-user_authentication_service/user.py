#!/usr/bin/env python3
"""User model for SQLAlchemy."""

import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """Data model for a user.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_token = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
