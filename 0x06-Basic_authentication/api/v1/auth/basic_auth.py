#!/usr/bin/env python3
""" Basic Authentication module """
from .auth import Auth


class BasicAuth(Auth):
    """ Basic Authentication class """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Returns the Base64 part of the Authorization header. """
        if authorization_header and type(authorization_header) == str \
           and authorization_header[:6] == 'Basic ':
            return authorization_header[6:]
        return None
