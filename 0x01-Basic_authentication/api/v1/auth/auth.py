#!/usr/bin/env python

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

        Args:
            path (str): The path to check for authentication.
            excluded_paths (List[str]): List of paths to exclude
            from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
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

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the Flask request.

        Args:
            request (flask.Request, optional): The Flask
            request object. Defaults to None.

        Returns:
            str: The Authorization header value if present, otherwise None.
        """
        if request is None or 'Authorization' not in request.headers:
            return None

        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None

        return authorization_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the
        Authorization header in the Flask request.

        Args:
            request (flask.Request, optional):
            The Flask request object. Defaults to None.

        Returns:
            TypeVar('User'):
            The current user object if authenticated, otherwise None.
        """
        if request is None or 'Authorization' not in request.headers:
            return None

        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None
        return None
