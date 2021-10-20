#!/usr/bin/env python3
"""module"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """fnunctio 1"""
    queue, array = [], []
    for _ in range(n):
        queue.append(wait_random(max_delay))

    for q in asyncio.as_completed(queue):
        result = await q
        array.append(result)

    return array



# """ Module for storing a basic asyncio sample. """
# import asyncio
# from random import uniform

# wait_random = __import__('0-basic_async_syntax').wait_random

# from typing import List


# async def wait_n(n: int, max_delay: int) -> List[float]:
#     """ Creates n instances of wait_random with the specified max_delay. """
#     queue, delays = [], []
#     while n > 0:
#         queue.append(wait_random(max_delay))
#         n -= 1

#     for delay in asyncio.as_completed(queue):
#         result = await delay
#         delays.append(result)

#     return delays