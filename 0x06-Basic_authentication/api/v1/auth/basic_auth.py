#!/usr/bin/env python3
""" Basic Authentication module """
from base64 import b64decode
from .auth import Auth


class BasicAuth(Auth):
    """ Basic Authentication class """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization header. """
        if authorization_header and type(authorization_header) == str \
           and authorization_header[:6] == 'Basic ':
            return authorization_header[6:]
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Returns the decoded value of a Base64 string. """
        if base64_authorization_header \
           and type(base64_authorization_header) == str:
            try:
                return b64decode(base64_authorization_header).decode('utf-8')
            except:
                return None
        return None
