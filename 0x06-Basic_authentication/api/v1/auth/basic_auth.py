#!/usr/bin/env python3
""" Basic Authentication module """
from models.user import User
from base64 import b64decode
from typing import TypeVar
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

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on his email and password. """
        if user_email and type(user_email) == str \
           and user_pwd and type(user_pwd) == str:
            try:
                users_list = User.search({"email": user_email})
            except Exception as e:
                return None
            for user in users_list:
                if user.is_valid_password(user_pwd):
                    return user
        return None
