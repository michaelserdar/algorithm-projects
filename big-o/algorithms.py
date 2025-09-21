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



