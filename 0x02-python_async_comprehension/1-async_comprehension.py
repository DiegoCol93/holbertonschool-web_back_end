#!/usr/bin/env python3

import asyncio
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Uses the async_generator with an async comprehension. """
    result = []
    async for i in async_generator():
        result.append(i)
    return(result)
