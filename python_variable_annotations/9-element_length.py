#!/usr/bin/env python3
"""
    Duck type and iteration
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """
    This function takes a list of sequences and returns a list of tuples.
    Each tuple contains a sequence and an int.
    """
    return [(i, len(i)) for i in lst]
