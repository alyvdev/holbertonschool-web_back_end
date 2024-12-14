#!/usr/bin/env python3
"""Filter log messages based on severity level."""

from typing import List
from re import sub, escape


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Filter sensitive fields in a log message."""
    # Build regex pattern for all fields
    escaped_fields = [escape(field) for field in fields]
    joined_fields = '|'.join(escaped_fields)
    pattern = f"({joined_fields})=.+?(?={escape(separator)}|$)"
    # Replace sensitive field values with redaction
    return sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
