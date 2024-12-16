#!/usr/bin/env python3
"""
Module to redact sensitive data from logs.

This module contains a formatter and logger setup for securely
obfuscating Personally Identifiable Information (PII) in logs.
"""

from typing import List
import re
import logging

# Define PII_FIELDS constant
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class.

    This formatter obfuscates specific fields in log messages to
    protect sensitive data.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor method."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Redacting Formatter method."""
        original_message = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, original_message, self.SEPARATOR
        )


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Obfuscates fields in a log message.

    Args:
        fields (List[str]): Fields to redact.
        redaction (str): Redaction string to use.
        message (str): Log message to process.
        separator (str): Separator for fields.

    Returns:
        str: Obfuscated log message.
    """
    pattern = f"({'|'.join(fields)})=.*?{separator}"
    return re.sub(
        pattern,
        lambda m: f"{m.group(1)}={redaction}{separator}",
        message
    )


def get_logger() -> logging.Logger:
    """
    Configures and returns a logger for user data.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create a handler with RedactingFormatter
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger
