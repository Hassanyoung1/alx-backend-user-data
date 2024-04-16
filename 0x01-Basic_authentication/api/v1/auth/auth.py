#!/usr/bin/env python3

"""
Authentication helper class for handling
authorization headers and user authentication.
"""


from typing import List, TypeVar
from flask import request


class Auth:
    """
    Authentication helper class for handling authorization
    headers and user authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for a given path.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path[-1] != '/':
                excluded_path += '/'

            if path == excluded_path:
                return False

            if '*' in excluded_path:
                wildcard_index = excluded_path.index('*')
                if path.startswith(excluded_path[:wildcard_index]):
                    return False

            elif path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the Flask request.
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the
        Authorization header in the Flask request.
        """
        if request is None or 'Authorization' not in request.headers:
            return None

        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None
        return None
