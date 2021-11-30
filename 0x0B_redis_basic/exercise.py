#!/usr/bin/env python3
""" 0. Writing strings to Redis """
from typing import Union, Callable
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

    def get(self, key: str, fn: Callable=None):
        """ Custom redis get method. """
        value = self._redis.get(key)
        if fn and value:
            value = fn(value)
        return(value)

    def get_str(self, key: str):
        """ Custom get str method. """
        return(self.get(key, str))

    def get_int(self):
        """ Custom get int method. """
        return(self.get(key, int))
