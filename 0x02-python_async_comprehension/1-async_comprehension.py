#!/usr/bin/env python3

import asyncio
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """ Uses the async_generator with an async comprehension. """
    result = [random_number async for random_number in async_generator()]
    return(result)
