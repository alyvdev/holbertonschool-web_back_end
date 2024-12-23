#!/usr/bin/env python3
"""
This is a simple exercise to test your understanding of the Python language.
"""

import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(func: Callable) -> Callable:
    """
    Decorator that counts the number of times a function is called.

    Args:
        func (Callable): The function to decorate.

    Returns:
        Callable: The decorated function.
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that increments the call count and executes the method"""
        self._redis.incr(func.__qualname__)
        return func(self, *args, **kwargs)
    
    return wrapper


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using a random key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The generated random key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis by key and optionally apply a transformation.

        Args:
            key (str): The key to retrieve the data.
            fn (Optional[Callable]): A function to transform the data.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis and decode it as a UTF-8 string.

        Args:
            key (str): The key to retrieve the data.

        Returns:
            Optional[str]: The retrieved data as a string, or None if not found.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis and convert it to an integer.

        Args:
            key (str): The key to retrieve the data.

        Returns:
            Optional[int]: The retrieved data as an integer, or None if not found.
        """
        return self.get(key, fn=int)
