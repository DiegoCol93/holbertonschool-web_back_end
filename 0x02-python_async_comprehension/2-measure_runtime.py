#!/usr/bin/env python3

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
    """ Runs async_comprehension 4 times concurrently and measures runtime. """
    start = time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end = time()
    return (end - start)
