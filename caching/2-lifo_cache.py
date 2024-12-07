#!/usr/bin/python3
""" LIFO caching """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO CACHE"""

    def __init__(self):
        super().__init__()
        self.keys = []
    
    def put(self, key, item):
        if key and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last = self.keys.pop()
                del self.cache_data[last]
                print("DISCARD: {}".format(last))
    
    def get(self, key):
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
