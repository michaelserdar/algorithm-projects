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

FAST = os.environ.get("FAST", "") != ""
SIZES_LINEAR = [10_000, 50_000, 100_000] if not FAST else [5_000, 20_000]
SIZES_NLOGN = [5_000, 20_000, 50_000] if not FAST else [2_000, 10_000]
SIZES_quad = [600, 1_000, 1_400] if not FAST else [300, 600]
SIZES_EXP = [28, 30] if not FAST else [24, 26]


def time_call(fn: Callable, *args, repeats: int = 1) -> float:
    start = time.perf_counter()
    for _ in range(repeats):
        fn(*args)
    end = time.perf_counter()
    return (end - start) / repeats


# function left aligns output rows for readability and converts seconds to ms
def format_row(name: str, n: int, secs: float) -> str:
    return f"{name:<18} | n={n:<8} | {secs*1000:8.4f} ms"


# prints the title of the algorithm and underlines it with * matching the len of title
def section(title: str):
    print("\n" + title)
    print("\n" * len(title))



if __name__ == "__main__":
    main()
