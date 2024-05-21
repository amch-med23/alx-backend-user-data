#!/usr/bin/env python3
""" basic authentication model """


from api.v1.auth.auth import Auth
from typing import TypeVar
import base64
from models.user import User


class BasicAuth(Auth):
    """ the basic auth class that inherents from the Auth class """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ a method to extract the base64 string from the header """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        token = authorization_header.split(' ')[1:]
        return token

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ a method to decode the base64 string """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            header_to_decode = base64_authorization_header.encode('utf-8')
            decode = base64.base64decode(item_to_decode)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ a method toextract the user credentials from the header """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        email, password = decoded_base64_authorization_header.split(':')
        return (email, password)

    def user_object_from_credentials(self, user_email: str,
                                     user_password: str) -> TypeVar('User'):
        """ a method to return a user object from the supplied credentials """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_password is None or not isinstance(user_password, str):
            return None
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_password):
                    return user

            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ retreives the current authonticated user """
        auth_header = self.authorization_header(request)
        if auth_header is not None:
            token = self.extract_base64_authorization_header(auth_header)
            if token is not None:
                decoded = self.decode_base64_authorization_header(token)
                if decoded is not None:
                    email, password = self.extract_user_credentials(decoded)
                    if email is not None:
                        return self.user_object_from_credentials(email,
                                                                 password)

        return
