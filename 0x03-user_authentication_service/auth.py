#!/usr/bin/env python3
"""
efine a _hash_password method that takes
in a password string arguments and returns bytes.
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hash a password with salt using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a random UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the given email and password"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))
            return user
        raise ValueError(f'User with email {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Validate a user by email and password"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a new session for a user"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> str:
        """Get a user from a session_id"""
        try:
            if session_id is None:
                return None
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy a session"""
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None
        return None
