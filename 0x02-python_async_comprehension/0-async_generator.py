#!/usr/bin/env python3
""" Module for storing the async_generator coroutine. """
import asyncio
from random import uniform
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """ Waits for a second and tields a random number """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
