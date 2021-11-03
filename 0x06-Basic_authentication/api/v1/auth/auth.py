#!/usr/bin/env python3
""" Basic Authentication module. """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Basic Authentication Template Class. """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Tells if a given path is authorized or not. """
        if path is None \
           or excluded_paths is None \
           or bool(excluded_paths) is False:
            return True

        if path[-1] != '/':
            path = path + '/'

        if path in excluded_paths:
            return False
        else:
            return True


    def authorization_header(self, request=None) -> str:
        """ Returns None ¯\_(ツ)_/¯.  """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None ¯\_(ツ)_/¯.  """
        return None
