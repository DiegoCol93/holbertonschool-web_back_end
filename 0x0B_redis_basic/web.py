#!/usr/bin/env python3
""" 5. Implementing an expiring web cache and tracker module. """
from requests import get as GET
from typing import Callable
from functools import wraps
import redis

def set_page(method: Callable) -> Callable:
    """ Decorator method to store the count of hits to a url. """
    @wraps(method)
    def cache_in(url):
        """ Inner decorator method. """
        text = method(url)
        cache = redis.Redis()
        cache.setex(f"count:{url}", 10, text)
    return cache_in


@set_page
def get_page(url: str) -> str:
    """ Obtains the HTML content of a URL and returns it. """
    r = GET(url)
    return r.text

get_page("http://slowwly.robertomurray.co.uk")
