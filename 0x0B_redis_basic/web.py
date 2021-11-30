#!/usr/bin/env python3
""" 5. Implementing an expiring web cache and tracker module. """
from requests import get as GET
import redis


def get_page(url: str) -> str:
    """ Obtains the HTML content of a URL and returns it. """
    cache = redis.Redis()
    r = GET(url)
    cache.setex(f"count:{url}", 10, r.text)
    return r.text
