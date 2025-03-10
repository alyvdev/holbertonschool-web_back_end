#!/usr/bin/python3
""" Basic dictionary """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - Caching System """
    def put(self, key, item):
        """ Add an item in the cache """
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """

        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
