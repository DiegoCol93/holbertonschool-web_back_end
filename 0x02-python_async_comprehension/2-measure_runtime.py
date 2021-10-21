#!/usr/bin/env python3
""" Module for storing the measure_runtime. """
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
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
