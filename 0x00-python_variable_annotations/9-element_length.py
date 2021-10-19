#!/usr/bin/env python3
""" Module to store the definition of the method to be annotated. """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Given method to annotate. """
    return [(i, len(i)) for i in lst]
