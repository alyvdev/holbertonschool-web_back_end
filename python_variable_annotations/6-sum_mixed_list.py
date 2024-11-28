#!/usr/bin/env python3
"""
This module demonstrates the use of type annotations in Python.
"""
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    This function takes a list of numbers as input and
    returns the sum of the numbers.
    """
    return sum(mxd_list)
