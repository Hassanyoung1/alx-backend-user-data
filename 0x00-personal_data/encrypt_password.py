#!/usr/bin/env python

"""
Encrypting passwords using bcrypt
"""

import bcrypt
from bcrypt import hashpw


def hash_password(password):
    """
    Hash password using bcrypt
    and return the hashed password
    """
    hashed = hashpw(password.encode(), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    validate password using bcrypt
    args:
    hashed_password: hashed password
    password: password to be validated
    return: True if password is valid
    else False
    """
    password = password.encode('utf-8')
    return bcrypt.checkpw(password, hashed_password)
