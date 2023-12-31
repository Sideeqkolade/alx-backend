#!/usr/bin/env python3
""" A FIFOCache module """
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ Represents an object that allows storing and
        retrieving items from a dictionary with a FIFO
        removal mechanism when the limit is reached.
    """
    def __init__(self):
        """ initialize cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """ get an item """
        return self.cache_data.get(key, None)
