#!/usr/bin/env python3

"""
This is a filtered logger module
"""

import re


def filter_datum(fields: list[str], redaction: str, message: str,
                 separator: str = str) -> str:
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
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message
