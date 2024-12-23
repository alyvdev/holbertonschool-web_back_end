#!/usr/bin/env python3
"""
This is a simple exercise to test your understanding of the Python language.
"""

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using a random key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The generated random key used to store the data.
        """
        key = str(uuid.uuid4())  # Generate a random UUID key as a string
        self._redis.set(key, data)  # Store the data in Redis with the key
        return key
