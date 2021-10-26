#!/usr/bin/python3
'''LFU Caching'''

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''LFU caching'''

    def __init__(self):
        '''Constructor'''
        super().__init__()
        self.queue = []
        self.counter = {}

    def put(self, key, item):
        '''Puts item in cache'''
        if key is None or item is None:
            return

        self.cache_data[key] = item

        item_count = self.counter.get(key, None)

        if item_count is not None:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_first_list(self.queue)
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
                del self.counter[first]
                print("DISCARD: {}".format(first))

        if key not in self.queue:
            self.queue.insert(0, key)
        self.mv_right_list(key)

    def get(self, key):
        '''Gets item from cache'''
        item = self.cache_data.get(key, None)
        if item is not None:
            self.counter[key] += 1
            self.mv_right_list(key)
        return item

    def mv_right_list(self, item):
        '''Moves element to the right, taking into account LFU'''
        length = len(self.queue)

        idx = self.queue.index(item)
        item_count = self.counter[item]

        for i in range(idx, length):
            if i != (length - 1):
                nxt = self.queue[i + 1]
                nxt_count = self.counter[nxt]

                if nxt_count > item_count:
                    break

        self.queue.insert(i + 1, item)
        self.queue.remove(item)

    @staticmethod
    def get_first_list(array):
        '''Get first element of list or None'''
        return array[0] if array else None
# """ LFU Cache module. """
# BaseCaching = __import__('base_caching').BaseCaching


# class LFUCache(BaseCaching):
#     """ Inherits from BaseCaching class and is a LFU Cache system. """
#     order = 0
#     better_dictionary = {} # better but expensive in memory.

#     def __init__(self):
#         """ Constructor of the class. """
#         super().__init__()

#     def put(self, key, item):
#         """ Assigns the item and key to the dictionary cache. """
#         if key and item:

#             if key in self.better_dictionary.keys():
#                 self.cache_data[str(key)] = item
#                 self.better_dictionary[str(key)]["hits"] += 1
#             else:
#                 self.cache_data[str(key)] = item
#                 self.better_dictionary[str(key)] = {
#                     "value": item,
#                     "order": self.order,
#                     "hits": self.order - self.order
#                 }

#             # Increase order of request in cache
#             self.order += 1

#             if len(self.better_dictionary) > self.MAX_ITEMS:

#                 # Obtain least accessed value with order. ━━━━━━━━━━━━━━━━━━━
#                 min_value = min([
#                     dictionary["order"]
#                     for dictionary
#                     in list(self.better_dictionary.values())
#                 ])

#                 # Obtain the least frequently accessed value with "hits". ━━━
#                 least_frequent = min(
#                     dictionary["hits"]
#                     for dictionary
#                     in list(self.better_dictionary.values())
#                 )

#                 # Pop the extra key from the dictionary. ━━━━━━━━━━━━━━━━━━━
#                 for key, value in self.better_dictionary.items():
#                     if value["order"] == min_value:
#                         key_to_pop = key

#                 # Print and pop. ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#                 print("DISCARD: {}".format(key_to_pop))
#                 self.better_dictionary.pop(key_to_pop)
#                 self.cache_data.pop(key_to_pop)

#     def get(self, key):
#         """ Returns the value of the cache_data dictionary given its key. """
#         if key and key in self.cache_data.keys():
#             self.better_dictionary[str(key)]["hits"] += 1
#             self.order += 1
#             return(self.cache_data[key])
#         return(None)
