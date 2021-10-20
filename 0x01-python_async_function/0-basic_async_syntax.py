#!/usr/bin/env python3
""" Module for storing a basic asyncio sample. """
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random delay between 0 and max_delay and returns it. """
    time = uniform(0, max_delay)
    await asyncio.sleep(time)
    return time