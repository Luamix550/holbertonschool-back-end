#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
"""
function’s parameters and return values with the appropriate types
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, list]]:
    return [(i, len(i)) for i in lst]
