#!/usr/bin/python3
""" LIFO caching """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    ''' A LIFO Cache.
        Inherits all behaviors from BaseCaching except, upon any attempt to
        add an entry to the cache when it is at max capacity (as specified by
        BaseCaching.MAX_ITEMS), it discards the newest entry to accommodate for
        the new one.
        Attributes:
          __init__ - method that initializes class instance
          put - method that adds a key/value pair to cache
          get - method that retrieves a key/value pair from cache '''
    def __init__(self):
        ''' Initialize class instance. '''
        super().__init__()
        self.keys = []
    
    def put(self, key, item):
        """ Add an item in the cache """
        if key and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last = self.keys.pop()
                del self.cache_data[last]
                print("DISCARD: {}".format(last))
    
    def get(self, key):
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
