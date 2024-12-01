#!/usr/bin/env python3
"""Basic async syntax"""
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay"""

    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for n random delays"""
    tasks = [wait_random() for _ in range(n)]
    return await asyncio.gather(*tasks)
