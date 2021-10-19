#!/usr/bin/env python3
""" Module for storing the sum_list() method definition. """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns the adition of the given list of float numbers.  """
    a: float = 0.0
    for num in input_list:
        a += num
    return (a)
