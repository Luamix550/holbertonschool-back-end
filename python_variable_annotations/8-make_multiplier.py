#!/usr/bin/env python3
from typing import Callable
"""
function make_multiplier that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def muliplier_function(x: float) -> float:
        return x * multiplier

    return muliplier_function
