#!/usr/bin/env python3
""" LIFO caching module """
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
        retrieving items from a dictionary with a LIFO
        removal mechanism when the limit is reached.
    """
    def __init__(self):
        """ initializing caching """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, last_item = self.cache_data.popitem(last=True)
                print(f"DISCARD: {last_key}")
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ access an item """
        return self.cache_data.get(key, None)
