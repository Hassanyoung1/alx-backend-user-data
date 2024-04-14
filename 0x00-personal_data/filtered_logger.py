#!/usr/bin/env python3

"""
This is a filtered logger module
"""
import logging
import re
from typing import List
import os
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Redacting Formatter class
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Redacting Formatter class
        """
        message = super().format(record)
        redact = filter_datum(self.fields, self.REDACTION,
                              message, self.SEPARATOR)
        return redact


def get_logger() -> logging.Logger:
    """ Get logger
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(("name", "email", "phone",
                                         "ssn", "password")))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Get database connection
    """
    db_config = {
        'user': os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        'password': os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        'host': os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        'database': os.getenv('PERSONAL_DATA_DB_NAME')
    }
    conn = mysql.connector.connect(**db_config)
    return conn

def main():
    db = get_db()
    logger = get_logger()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    for row in cursor:
        logger.info("name=%s; email=%s; phone=%s; ssn=%s; password=%s; ip=%s; last_login=%s; user_agent=%s",
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    cursor.close()
    db.close()

if __name__ == '__main__':
    main()
