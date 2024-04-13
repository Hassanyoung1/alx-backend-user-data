#!/usr/bin/env python3

"""
This is a filtered logger module
"""

import logging
import re


logger = logging.getLogger(__name__)


def filter_datum(fields: list[str], redaction: str, message: str,
                 separator: str = ',') -> str:
    """
    This function filters the data.

    Args:
        fields (list[str]): A list of strings representing the
        fields to obfuscate.
        redaction (str): A string representing how the
        field will be obfuscated.

        message (str): A string representing the log line.

        separator (str, optional): A string

        representing the character that separates all fields
            in the log line. Defaults to ','.

    Returns:
        str: The filtered log message with specified fields obfuscated.
    """
    for field in fields:
        message = re.sub(r'(?<=' + separator + field + '=)([^' +
                         separator + ']+)', redaction, message)
    return message
