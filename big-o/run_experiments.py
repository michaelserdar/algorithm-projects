"""
time each function for increasing input sizwes and print a simple table.

Usage:
    python run_experiments.py
Options:
    pass environment var FAST=1 to use smaller sizes
"""
import os
import random
import time
from typing import Callable, List, Tuple
from algorithms import (
    first_element,
    is_even,
    binary_search_steps,
    linear_sum,
    merge_sort,
    quadratic_pairs,
    fib_exp
)



