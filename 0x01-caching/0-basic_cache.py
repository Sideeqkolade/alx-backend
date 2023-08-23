#!/usr/bin/env python3
""" Script that creates a class BasicCache """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ add an item in the cache """
    def put(self, key, item):
        """ add an item into the dictionary """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
