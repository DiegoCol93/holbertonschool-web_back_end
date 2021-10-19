#!/usr/bin/env python3
""" Module for storing the sum_mixed_list() method definition."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sums a mixed list of integers and float numbers returning a float. """
    a: float = 0.0
    for num in mxd_lst:
        a += num
    return(a)
