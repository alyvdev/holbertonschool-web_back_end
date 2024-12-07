#!/usr/bin/env python3
"""Async Generator"""
async_generator = __import__('0-async_generator').async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehensing"""
    return [i async for i in async_generator()]
