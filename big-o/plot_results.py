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

