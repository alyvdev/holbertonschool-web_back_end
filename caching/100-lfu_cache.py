#!/usr/bin/python3
""" LFU caching """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache"""
    def __init__(self):
        ''' Initialize class instance. '''
        super().__init__()
        self.keys = []
        self.count = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if key in self.count:
                self.count[key] += 1
            else:
                self.count[key] = 1
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = min(self.count, key=self.count.get)
                self.count.pop(discard)
                self.keys.pop(self.keys.index(discard))
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """ Return value stored in `key` key of cache.
            If key is None or does not exist in cache, return None."""
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            self.count[key] += 1
            return self.cache_data[key]
        return None
