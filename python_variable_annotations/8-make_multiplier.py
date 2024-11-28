#!/usr/bin/env python3
"""
This module demonstrates the use of type annotations in Python.
"""


def make_multipler(multiplier: float) -> callable:
    """
    This function returns a function that multiplies a float by multiplier.
    """
    def f(n: float) -> float:
        return n * multiplier
    return f
