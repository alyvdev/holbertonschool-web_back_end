#!/usr/bin/node
"""
    Encrypt a string
"""
import bcrypt
from db import DB
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from uuid import uuid4


def _hash_password(password: str = '') -> str:
    """
        Hashed the password

        Args:
            password: string to hashed
        Return:
            hashed password
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'),
                           bcrypt.gensalt(prefix=b"2b"))

    hash_str: str = str(hashed.decode())

    return hash_str


def _generate_uuid() -> str:
    """ Generate uuid
        Return:
            uuid in string
    """
    UUID = uuid4()

    return str(UUID)
