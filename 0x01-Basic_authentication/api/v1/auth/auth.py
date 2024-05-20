#!/usr/bin/env python3
"""" the basic authentication model """


from flask import requests
from typing import List, TypeVar


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

        for exclude_path in excluded_paths:
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

    def current_user(self, request=None) -> typeVar('User'):
        """ the current authorized (authenticated) user """
        return None