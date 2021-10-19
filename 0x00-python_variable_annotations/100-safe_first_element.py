#!/usr/bin/env python3
""" Module to store the definition of the method to be annotated. """
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Given method to annotate. """
    if lst:
        return lst[0]
    else:
        return None
