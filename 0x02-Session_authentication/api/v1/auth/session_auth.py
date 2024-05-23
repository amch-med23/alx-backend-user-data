#!/usr/bin/env python3
""" the session authentication module """


from .auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """ session authenticatioin class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ a method to create the session """
        if user_id is None or not isinstance(user_id, str):
            return None

        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ creting a user id for a session id """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ retreives the current authenticated user """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """ this delets the session / means a logout event """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookie]
        return True
