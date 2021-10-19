#!/usr/bin/env python3
""" Module to store the definition of the method to be annotated. """
from typing import Tuple, List, Any, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Given method to annotate and check with mypy """
    zoomed_in: Tuple = tuple([
        item for item in lst
        for i in range(int(factor))
    ])
    return list(zoomed_in)


# array: Tuple = [12, 72, 91]

# zoom_2x = zoom_array(array)
# print(zoom_2x)

# zoom_3x = zoom_array(array, 3.0)
# print(zoom_3x)
