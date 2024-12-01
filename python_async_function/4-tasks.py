#!/usr/bin/env python3
"""  alter it into a new function task_wait_n.
The code is nearly identical to wait_n except
task_wait_random is being called """

from typing import List


task_wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns delayed async task"""
    delays = []
    for _ in range(n):
        delays.append(task_wait_n(n, max_delay))
    return delays
