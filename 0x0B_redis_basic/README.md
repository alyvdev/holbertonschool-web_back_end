# Redis Basic

This project covers basic Redis operations using Python. It demonstrates how to use Redis for caching and basic data storage operations.

## Learning Objectives

- Learn how to use Redis for basic operations
- Learn how to use Redis as a simple cache
- Understand basic Redis commands and their Python implementation

## Requirements

- All files interpreted/compiled on Ubuntu 18.04 LTS using Python3 (version 3.7)
- All files should end with a new line
- First line of all files should be exactly `#!/usr/bin/env python3`
- Code should use the `pycodestyle` style (version 2.5)
- All modules should have documentation
- All classes should have documentation
- All functions should have documentation
- Type annotations must be added for all functions

## Installation

```bash
pip install redis
```

## Files

- `exercise.py`: Contains the implementation of Cache class for Redis operations

## Usage

```python
cache = Cache()
data = "hello"
key = cache.set(data)
```

## Author
[Your Name]
