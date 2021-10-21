#!/usr/bin/env python3
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Uses the async_generator with an async comprehension. """
    result = [random_number async for random_number in async_generator()]
    return(result)
