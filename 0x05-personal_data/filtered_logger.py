#!/usr/bin/env python3
""" 0. Regex-ing module. """
from typing import List
import logging
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns an obfuscated message given the fields to obfuscate. """
    for field in fields:
        message = re.sub(r'({}=)(.+?){}'.format(field, separator),
                         r'\1{}{}'.format(redaction, separator), message)
    return(message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """ Constructor of class RedactingFormatter. """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.FIELDS = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Formatting method. """
        logging.basicConfig(format=self.FORMAT)
        return(filter_datum(
            self.FIELDS, self.REDACTION, super().format(record), self.SEPARATOR))
