# big-o/test_big_o.py
import math
import pytest

from algorithms import (
    first_element,
    is_even,
    binary_search_steps,
    linear_sum,
    merge_sort,
    quadratic_pairs,
    fib_exp,
)


# ----------------- O(1) ----------------- #

def test_first_element_basic():
    arr = [10, 20, 30]
    assert first_element(arr) == 10


def test_first_element_empty():
    assert first_element([]) is None


def test_is_even_true_false():
    assert is_even(4) is True
    assert is_even(7) is False


# ----------------- O(log n) ----------------- #
def test_binary_search_steps_log_growth():
    s1 = binary_search_steps(8)  # log2(8) = 3
    s2 = binary_search_steps(16)  # log2(16) = 4
    s3 = binary_search_steps(32)  # log2(32) = 5
    assert s1 <= s2 <= s3
    assert s2 - s1 == 1
    assert s3 - s2 == 1


# ----------------- O(n) ----------------- #
def test_linear_sum_matches_formula():
    for n in range(0, 10):
        assert linear_sum(n) == n * (n - 1) // 2


# ----------------- O(n log n) ----------------- #
def test_merge_sort_sorted_output():
    data = [5, 1, 4, 2, 8, 0, 2]
    assert merge_sort(data) == sorted(data)


def test_merge_sort_empty_and_single():
    assert merge_sort([]) == []
    assert merge_sort([42]) == [42]


# ----------------- O(n^2) ----------------- #
def test_quadratic_pairs_count_only():
    for n in range(6):
        assert quadratic_pairs(n) == n * (n - 1) // 2


def test_quadratic_pairs_with_pairs():
    count, pairs = quadratic_pairs(4, return_pairs=True)
    assert count == 6
    assert pairs == [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


# ----------------- O(2^n) ----------------- #
def test_fib_exp_small_values():
    vals = [fib_exp(i) for i in range(10)]
    assert vals == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fib_exp_base_cases():
    assert fib_exp(0) == 0
    assert fib_exp(1) == 1
