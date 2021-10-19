#!/usr/bin/env python3
""" Module to store the definition of the method to be annotated. """
from typing import Mapping, Any, Union, TypeVar
a_type = TypeVar("T")


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[a_type, None] = None
                     ) -> Union[Any, a_type]:
    """ Given method to annotate. """
    if key in dct:
        return dct[key]
    else:
        return default
