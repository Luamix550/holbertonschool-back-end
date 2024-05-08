#!/usr/bin/env python3
from typing import  Iterable, Sequence, Any
"""
The types of the elements of the input are not known
"""
def safe_first_element(lst: Iterable[Sequence]) -> Any:
    if lst:
        return lst[0]
    else:
        return None