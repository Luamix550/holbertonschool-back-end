#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_random(n: int, max_delay: int) -> List[float]:
    data = [task_wait_random(max_delay) for _ in range(n)]
    data = await asyncio.gather(*data)
    return sorted(data)
