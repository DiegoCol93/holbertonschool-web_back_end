#!/usr/bin/env python3
""" 0. Regex-ing module. """

import re
from typing import List

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns an obfiscated message given the fields. """
    
