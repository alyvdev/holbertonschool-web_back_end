#!/usr/bin/env python3
"""
This module demonstrates the use of type annotations in Python.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string k and an int or float v as arguments
    and returns a tuple.
    """
    return (k, v ** 2)
