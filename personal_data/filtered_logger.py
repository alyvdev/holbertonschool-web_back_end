#!/usr/bin/env python3
"""Filter log messages based on severity level."""

from typing import List
from re import sub


def filter_datum(fields: List, redaction: str,
                 message: str, separator: str) -> str:
    """
        Filter and obfuscated the string

        Args:
            fields: a list of strings representing all fields to obfuscate
                    ["password", "date_of_birth"]
            redaction: a string representing by what the
                       field will be obfuscated
                       "XXXXX"
            message: a string representing the log line
                    ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;"]
                    ["name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]
            separator: a string representing by which character is
                    separating all fields in the log line (message)
                    ";"
        Return:
            String with string ofuscated
    """
    for field in fields:
        message = sub(f'{field}=.+?{separator}',
                      f'{field}={redaction}{separator}', message)

    return message
