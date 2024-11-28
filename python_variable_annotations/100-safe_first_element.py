#!/usr/bin/env python3
"""
Duck typing sequence Any
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Duck typing sequence Any
    """
    if lst:
        return lst[0]
    else:
        return None
