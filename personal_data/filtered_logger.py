#!/usr/bin/env python3
"""Filter log messages based on severity level."""

from typing import List
from re import sub


def filter_datum(fields: List, redaction: str,
                 message: str, separator: str):
    """ Filter datum"""
    for field in fields:
        message = sub(f'{field}=.+?{separator}',
                      f'{field}={redaction}{separator}', message)
        
    return message
    pattern = f"({'|'.join(fields)})=.+?{separator}"
    return sub(pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message)
