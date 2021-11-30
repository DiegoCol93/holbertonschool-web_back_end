#!/usr/bin/env python3
""" 0. Writing strings to Redis """
from typing import Union, Callable
from functools import wraps
from uuid import uuid4
import redis


def count_calls(method: Callable) -> Callable:
    """ Decorator method to count calls to the Cache calss methods. """
    @wraps(method)
    def counter(self, data):
        """
        Increments the number of calls to the given method having
        __qualname__ as the keyname.
        """
        self._redis.incr(method.__qualname__, 1)
        return method(self, data)
    return counter


def call_history(method: Callable) -> Callable:
    """ Stores history of inputs and outputs for the given method. """
    @wraps(method)
    def history(self, data):
        """ Stores history of inputs and outputs for the given method. """
        self._redis.rpush(method.__qualname__ + ":inputs",
                          str("('" + data + "',)"))
        out = method(self, data)
        self._redis.rpush(method.__qualname__ + ":outputs", out)
        return out
    return history


class Cache:
    """ Basic cache redis class. """

    def __init__(self):
        """ Constructor method. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a UUID, and stores the data in Redis. """
        key = str(uuid4())
        self._redis.set(key, data)
        return(key)

    def get(self, key: str, fn: Callable = None):
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
