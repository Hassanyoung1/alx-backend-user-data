#!/usr/bin/env python3
"""User model for SQLAlchemy."""

from sqlalchemy.orm  import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """Data model for a user.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_token = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
