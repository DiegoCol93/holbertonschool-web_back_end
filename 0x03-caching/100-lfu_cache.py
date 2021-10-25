#!/usr/bin/env python3
""" LFU Cache module. """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Inherits from BaseCaching class and is a LFU Cache system. """
    order = 0
    better_dictionary = {} # better but expensive in memory.

    def __init__(self):
        """ Constructor of the class. """
        super().__init__()

    def put(self, key, item):
        """ Assigns the item and key to the dictionary cache. """
        if key and item:

            if key in self.better_dictionary.keys():
                self.cache_data[str(key)] = item
                self.better_dictionary[str(key)]["hits"] += 1
            else:
                self.cache_data[str(key)] = item
                self.better_dictionary[str(key)] = {
                    "value": item,
                    "order": self.order,
                    "hits": self.order - self.order
                }

            # Increase order of request in cache
            self.order += 1

            if len(self.better_dictionary) > self.MAX_ITEMS:

                # Obtain least accessed value with order. ━━━━━━━━━━━━━━━━━━━━━
                min_value = min([
                    dictionary["order"]
                    for dictionary
                    in list(self.better_dictionary.values())
                ])

                # Obtain the least frequently accessed value with "hits". ━━━━━━
                least_frequent = min(
                    dictionary["hits"]
                    for dictionary
                    in list(self.better_dictionary.values())
                )

                # Pop the extra key from the dictionary. ━━━━━━━━━━━━━━━━━━━━━━
                for key, value in self.better_dictionary.items():
                    if value["order"] == min_value:
                        key_to_pop = key

                # Print and pop. ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                print("DISCARD: {}".format(key_to_pop))
                self.better_dictionary.pop(key_to_pop)
                self.cache_data.pop(key_to_pop)

    def get(self, key):
        """ Returns the value of the cache_data dictionary given its key. """
        if key and key in self.cache_data.keys():
            self.better_dictionary[str(key)]["hits"] += 1
            self.order += 1
            return(self.cache_data[key])
        return(None)
