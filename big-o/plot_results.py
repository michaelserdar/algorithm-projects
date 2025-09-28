# big-o/plot_results.py
"""
Plot runtime growth curves for the Big-O examples

Usage (from repo root):
    python big-o/plot_results.py
    python big-o/plot_results.py --fast
    python big-o/plot_results.py --only linear_sum,merge_sort
    python big-o/plot_results.py --csv big-o/plots/results.csv
    python big-o/plot_results.py --outdir big-o/plots-fast --fast

Notes:
- one chart per function
- simple charts for readability no color/style - may update in future
"""

import argparse
import csv
import os
import random
import time
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Tuple, Optional

# import functions
from algorithms import (
    first_element,
    is_even,
    binary_search_steps,
    linear_sum,
    merge_sort,
    quadratic_pairs,
    fib_exp
)

# -------------------------------- Configuration -----------------------------------------#


def get_sizes(fast: bool) -> Dict[str, List[int]]:
    """Return input-size schedule per function"""
    return {
        # O(1) examples: list length doesn't effect lookup cost
        "first_element": [1_000_000, 1_000_000, 1_000_000],
        "is_even": [10, 10**8, 10**12],

        # O(log n) example
        "binary_search": [10,10_000,10_000_000],

        # O(n) example
        "linear_sum": [5_000, 20_000] if fast else [10_000, 50_000, 100_000],

        # O(n log n) example
        "merge_sort": [2_000, 10_000] if fast else [5_000, 20_000, 50_000],

        # O(n^2) example
        "quadratic_pairs": [300, 600] if fast else [600, 1_000, 1_400],

        # O(2^n) example
        "fib_exp": [24, 26] if fast else [28, 30]
    }


def get_funcs() -> Dict[str, Callable[[int], object]]:
    """
    Map function names to callables that accept 'n'.
    where needed, wrap to generate inputs (e.g., merge_sort needs a list).
    """
    return {
        "first_element": lambda n: first_element(list(range(n))),
        "is_even": lambda n: is_even(n),
        "binary_search": lambda n: binary_search_steps(n),
        "linear_sum": lambda n: linear_sum(n),
        "merge_sort": lambda n: merge_sort([random.randint(0,1_000_000) for _ in range(n)]),
        "quadratic_pairs": lambda n: quadratic_pairs(n),
        "fib_exp": lambda n: fib_exp(n)
    }


def get_repeats(fast: bool)-> Dict[str, int]:
    """
    Repeat very fast calls to reduce timer noise.
    Slower algorithms run once per n
    """
    return {
        "first_element": 200_000 if fast else 500_000,
        "is_even": 200_000 if fast else 500_000,
        "binary_search": 100_000 if fast else 200_000,
        "linear_sum": 1,
        "merge_sort": 1,
        "quadratic_pairs": 1,
        "fib_exp": 1
    }

# --------------------------------- Timing -------------------------#


def time_call(fn: Callable[[int], object], n: int, repeats: int) -> float:
    """
    Return average seconds over 'repeats' runs.
    """
    start = time.perf_counter()
    for _ in range(repeats):
        fn(n)
    end = time.perf_counter()
    return (end - start) / repeats


def measure_series(name: str, fn: callable[[int], object], ns: Iterable[int],
                   repeats: int) -> Tuple[List[int], List[float]]:
    """Measure seconds for each n; returns (ns, secs)"""
    ns_list: List[int] = []
    secs: List[float] = []
    for n in ns:
        s = time_call(fn, n, repeats=repeats)
        ns_list.append(n)
        secs.append(s)
    return ns_list, secs


# ---------------------------------- Plotting --------------------------------#

def plot_series(name:str, ns: List[int], secs: List[float], outdir: Path) -> Path:
    import matplotlib.pyplot as plt

    outdir.mkdir(parents=True, exist_ok=True)
    outpath = outdir / f"{name}.png"

    plt.figure() # default style
    plt.plot(ns, secs, marker="o")
    plt.xlabel("n")
    plt.ylabel("seconds")
    plt.title(f"Runtime growth: {name}")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(outpath.as_posix(), dpi=150, bbox_inches="tight")
    plt.close()

    print(f"Saved {outpath}")
    return outpath

