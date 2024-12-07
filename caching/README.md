# Caching System

This repository contains different caching system implementations in Python. Each caching system follows a different caching strategy.

## Files

### `0-basic_cache.py`
This file contains the implementation of a basic caching system using a dictionary.

### `1-fifo_cache.py`
This file contains the implementation of a FIFO (First In First Out) caching system.

### `2-lifo_cache.py`
This file contains the implementation of a LIFO (Last In First Out) caching system.

## Usage

Each caching system is implemented as a class that inherits from `BaseCaching`. The `BaseCaching` class is assumed to be provided in a separate module named `base_caching`.

### BasicCache
```python
from 0-basic_cache import BasicCache

cache = BasicCache()
cache.put("A", "Hello")
print(cache.get("A"))  # Output: Hello
```

### FIFOCache
```python
from 1-fifo_cache import FIFOCache

cache = FIFOCache()
cache.put("A", "Hello")
cache.put("B", "World")
print(cache.get("A"))  # Output: Hello
```

### LIFOCache
```python
from 2-lifo_cache import LIFOCache

cache = LIFOCache()
cache.put("A", "Hello")
cache.put("B", "World")
print(cache.get("B"))  # Output: World
```

## Author
This project is maintained by Holberton School students.