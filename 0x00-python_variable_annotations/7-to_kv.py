#!/usr/bin/env python3
"""
Atype annotated function that returns a tuple
"""
from typing import List, Union, Tuple



def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple
    """
    return (k, v * v)
