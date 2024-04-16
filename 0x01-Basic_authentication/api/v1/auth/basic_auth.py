#!/usr/bin/env python3

"""
This module contains the basic authentication class.
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic authentication class."""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts the base64 part of the authorization header."""
        if (authorization_header is None or
            not isinstance(authorization_header, str) or
            not authorization_header.startswith('Basic ')):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decodes the base64 part of the authorization header."""
        if (base64_authorization_header is None or
            not isinstance(base64_authorization_header, str)):
            return None
        try:
            return base64.b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None
