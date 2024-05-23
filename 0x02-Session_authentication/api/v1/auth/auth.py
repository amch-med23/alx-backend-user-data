#!/usr/bin/env python3
"""" the basic authentication model """


from flask import request
from typing import List, TypeVar
import os

class Auth:
    """ the auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ this is to check the authentication requirements """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_paths[:-1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ the header authorization method """
        if request is None:
            return None

        # retreaives the header from the request
        header = request.headers.get('Authorization')

        if header is None:
            return None

        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """ the current authorized (authenticated) user """
        return None

    def session_cookie(self, request=None):
        """ a session cookie logic """
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
