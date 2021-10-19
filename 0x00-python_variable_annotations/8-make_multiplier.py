#!/usr/bin/env python3
""" Module for storing the make_multiplier() method definition."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier. """
    return lambda x: multiplier * x
