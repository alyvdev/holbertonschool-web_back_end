#!/usr/bin/env python3
""" Module of Auth views
"""
from flask import jsonify, abort, request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for given path"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        
        if not path.endswith('/'):
            path += '/'

        return not any(path.startswith(exc.rstrip('/') + '/') 
                  for exc in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """ authorization_header
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar:
        """ current_user
        """
        return None

    def session_cookie(self, request=None):
        """ session_cookie
        """
        if request is None:
            return None
        return request.cookies.get('_my_session_id')
