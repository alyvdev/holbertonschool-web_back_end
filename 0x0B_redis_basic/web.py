#!/usr/bin/env python3
""" redis module
"""

import redis


def get_page(url: str) -> str:
    """get page"""
    r = redis.Redis()
    key = f"count:{url}"
    r.incr(key)
    return r.get(url).decode('utf-8')
