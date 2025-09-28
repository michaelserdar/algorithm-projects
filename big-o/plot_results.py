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
        "is_even": [10, 10 ** 8, 10 ** 12],

        # O(log n) example
        "binary_search": [10, 10_000, 10_000_000],

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
    We cache large inputs so repeats don't rebuild them.
    """
    arr_cache: Dict[int, list] = {}

    def first_element_wrapped(n: int):
        # Build the array once per n, then reuse it across repeats.
        if n not in arr_cache:
            arr_cache[n] = list(range(n))
        return first_element(arr_cache[n])

    return {
        "first_element": first_element_wrapped,           # uses cache
        "is_even": lambda n: is_even(n),
        "binary_search": lambda n: binary_search_steps(n),
        "linear_sum": lambda n: linear_sum(n),
        "merge_sort": lambda n: merge_sort([random.randint(0, 1_000_000) for _ in range(n)]),
        "quadratic_pairs": lambda n: quadratic_pairs(n),
        "fib_exp": lambda n: fib_exp(n),
    }


def get_repeats(fast: bool) -> Dict[str, int]:
    """
    Repeat very fast calls to reduce timer noise, but keep counts reasonable.
    """
    return {
        "first_element": 50_000 if fast else 100_000,   # reduced (was huge)
        "is_even": 50_000 if fast else 100_000,
        "binary_search": 20_000 if fast else 50_000,
        "linear_sum": 1,
        "merge_sort": 1,
        "quadratic_pairs": 1,
        "fib_exp": 1,
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


def measure_series(name: str, fn: Callable[[int], object], ns: Iterable[int],
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

def plot_series(name: str, ns: List[int], secs: List[float], outdir: Path) -> Path:
    import matplotlib.pyplot as plt

    outdir.mkdir(parents=True, exist_ok=True)
    outpath = outdir / f"{name}.png"

    plt.figure()  # default style
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


# ------------------------------- CSV -----------------------------------------#


def append_csv(csv_path: Path, rows: List[Tuple[str, int, float]]) -> None:
    """Append timing rows to a csv file. Creates a header if one does not exist"""
    csv_path.parent.mkdir(parents=True, exist_of=True)
    new_file = not csv_path.exists()
    with csv_path.open("a", newline="") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["function", "n", "seconds"])
        for row in rows:
            w.writerow(row)


# ---------------------------- CLI -------------------------------------------#


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Plot Big-O runtime growth curves.")
    p.add_argument(
        "--fast", action="store_true", help="Use smaller input sizes"
    )
    p.add_argument(
        "--only", type=str, default="", help="Comma-separated list of function names to include "
                                             "(first_element, is_even, binary_search_steps, linear_sum, merge_sort, "
                                             "quadratic_pairs, fib_exp)"
    )
    p.add_argument(
        "--outdir", type=Path, default=Path(__file__).parent / "plots",
        help="Directory to save PNG plots (defaults to big-o/plots"
    )
    p.add_argument(
        "--csv", type=Path, default=None, help="Optional path to append timing results as CSV."
    )
    return p.parse_args()

# ------------------------------- Main ---------------------------------------#


def main() -> None:
    args = parse_args()

    # look for either --fast of environment FAST from the cli
    fast_env = os.environ.get("Fast", "") != ""
    fast = args.fast or fast_env

    sizes = get_sizes(fast)
    funcs = get_funcs()
    repeats = get_repeats(fast)

    # filter selection if --only is given as flag
    selected = set(n.strip() for n in args.only.split(",") if n.strip()) or set(funcs.keys())
    unknown = selected - set(funcs.keys())
    if unknown:
        raise SystemExit(f"Unknown function: {', '.join(sorted(unknown))}")

    # run, plot, and optionally log csv
    for name in sorted(selected):
        fn = funcs[name]
        ns = sizes[name]
        reps = repeats[name]

        ns_list, secs = measure_series(name, fn, ns, reps)
        plot_series(name, ns_list, secs, args.outdir)

        if args.csv is not None:
            rows = [(name, n, s) for n, s in zip(ns_list, secs)]
            append_csv(args.csv, rows)

if __name__ == "__main__":
    main()
