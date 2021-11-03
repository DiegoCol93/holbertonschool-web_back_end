#!/usr/bin/env python3
""" Basic Authentication module. """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Basic Authentication Template Class. """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False ¯\_(ツ)_/¯. """
        return False

    def authorization_header(self, request=None) -> str:
        """ Returns None ¯\_(ツ)_/¯.  """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None ¯\_(ツ)_/¯.  """
        return None
