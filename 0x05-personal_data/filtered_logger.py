#!/usr/bin/env python3
""" 0. Regex-ing module. """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns an obfuscated message given the fields. """
    for field in fields:
        message = re.sub(r'({}=)(.+?){}'.format(field, separator),
                         r'\1{}{}'.format(redaction, separator), message)
    return(message)
