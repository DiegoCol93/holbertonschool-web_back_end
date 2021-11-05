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
            except Exception as e:
                return None
        return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Returns the user email and password from the Base64. """
        if decoded_base64_authorization_header \
           and type(decoded_base64_authorization_header) == str \
           and ":" in decoded_base64_authorization_header:
            index = decoded_base64_authorization_header.index(":")
            mail = decoded_base64_authorization_header[:index]
            psw = decoded_base64_authorization_header[index + 1:]
            return (mail, psw)
        return (None, None)
