#!/usr/bin/env python3
""" Module for storing the to_kv() method definition."""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple of string k and int or float v """
    return (k, v * v)
