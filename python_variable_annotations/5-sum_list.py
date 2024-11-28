#!/usr/bin/env python3
"""
This module demonstrates the use of type annotations in Python.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of numbers as input and
    returns the sum of the numbers.
    """
    return sum(input_list)
