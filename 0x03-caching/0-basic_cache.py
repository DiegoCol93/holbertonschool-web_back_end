#!/usr/bin/env python3
""" BasicCaching module. """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from BaseCaching class and is a basic Cache system. """

    def __init__(self):
        """ Constructor of the class. """
        super().__init__()

    def put(self, key, item):
        """ Assigns the item and key to the dictionary cache. """
        if key and item:
            self.cache_data[str(key)] = item

    def get(self, key):
        """ Returns the value of the cache_data dictionary given its key. """
        if key:
            if key in self.cache_data.keys():
                return(self.cache_data[str(key)])
        return(None)
