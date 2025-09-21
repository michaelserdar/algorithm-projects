"""
reference implementations illustrating time complexity growth.
algorithms are written for teaching purposes
"""
from typing import List


# --0(1)-------------------------------------------------

# example 1
def first_element(arr: list):
    """Return the first element of a list"""
    if not arr:
        return None
    else:
        return arr[0]


# example 2
def is_even(n: int) -> bool:
    """checks if an int is even or odd"""
    return n % 2 == 0


# --O(log n)--------------------------------------------
def binary_search_steps(n: int) -> int:
    """
    Simulates the number of iterations binary search would need on a list of length n.
    not actually building the list as it would add n time complexity to build and mask the
    function of log n
    """
    steps = 0
    lo = 0
    hi = max(1, n-1)
    target = hi  # worst case ends after ~log2(n) effectively halving the steps
    while lo <= hi:
        steps +=1
        mid = (lo + hi) // 2
        if mid == target:
            return steps
        elif mid < target:
            lo = mid + 1
        else:
            hi = mid -1
        return steps


# --O(n)---------------------------------------------------
def linear_sum(n: int) -> int:
    total = 0
    for i in range(n):
        total +=i
    return total


# --O(n log n)--------------------------------------------
def merge_sort(a: List[int]) -> List[int]:
    """
    Merge sort algorithm
    """
    # Base case: if the list is length 0 or 1 it is already sorted
    if len(a) <= 1:
        return a

    # split the list in half
    mid = len(a) // 2
    left = merge_sort(a[:mid])   # recursively sort left half
    right = merge_sort(a[mid:])  # recursively sort right half

    # merge two sorted lists back into one with merge function
    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    """
    merge two sorted lists into a single list
    Key step of merge sort
    """
    i = j = 0  # pointers for the left and right lists
    out = []

    # while both lists have elements left to compare
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1

    # to reach this point at least one list is sorted
    # append any remaining elements from the other list
    out.extend(left[i:])
    out.extend(right[j:])
    return out


# --O(n^2)---------------------------------------------------------
def quadratic_pairs(n: int, return_pairs: bool = False):
    """
    Count how many (i, j) pairs with i < j exist among n elements.
    input: int - number of pairs
    output: count of pairs or list of pairs if return_pairs = True
    """
    count = 0
    pairs = [] if return_pairs else None

    for i in range(n):
        for j in range(i + 1, n):
            count += 1
            if return_pairs:
                pairs.append((i,j))

    return (count, pairs) if return_pairs else count


# --O(2^n)-----------------------------------------------------------
def fib_exp(n: int) -> int:
    """
    naive recursive fibonacci to show explosive growth
    DO NOT CALL WITH LARGE N keep it <= 30
    """

    # Base case
    if n <=1:
        return n
    return fib_exp(n -1) + fib_exp(n -2)
