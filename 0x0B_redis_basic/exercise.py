#!/usr/bin/env python3
""" 0. Writing strings to Redis """
from typing import Union
from uuid import uuid4
import redis


class Cache:
    """ Basic cache redis class. """

    def __init__(self):
        """ Constructor method. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a UUID, and stores the data in Redis. """
        key = str(uuid4())
        self._redis.set(key, data)
        return(key)
