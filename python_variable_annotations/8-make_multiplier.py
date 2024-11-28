#!/usr/bin/env python3
"""
This module demonstrates the use of type annotations in Python.
"""
from typing import Callable


def make_multipler(multiplier: float) -> Callable[[float], float]:
    """
    This function returns a function that multiplies a float by multiplier.
    """


    def f(n: float) -> float:
        """ Get the second argument somthing like JS """
        return float(f * multiplier)
    return f
