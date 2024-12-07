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
        ''' Add key/value pair to cache data.
            If cache is at max capacity (specified by BaseCaching.MAX_ITEMS),
            discard least frequently used entry to accommodate new entry. '''

        if key is not None and item is not None:
            if (len(self.keys) == BaseCaching.MAX_ITEMS and
                    key not in self.keys):
                discard = self.keys.pop(self.keys.index(self.findLFU()))
                del self.cache_data[discard]
                del self.uses[discard]
                print('DISCARD: {:s}'.format(discard))
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
                self.uses[key] = 0
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
                self.uses[key] += 1

    def get(self, key):
        ''' Return value stored in `key` key of cache.
            If key is None or does not exist in cache, return None. '''
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            self.uses[key] += 1
            return self.cache_data[key]
        return None
