# Recursive version of Euclid's algorithm
import sys


def gcd_recursive(a: int, b: int, depth: int = 1) -> int:
    """Computer GCD using the recursive Euclidean algorithm, printing each call."""
    print(f"Call {depth}: gcd_recursive{a}, {b}")

    if b == 0:
        print(f"Bae case reached at depth {depth}: GCD = {abs(a)}")
        return abs(a)

    return gcd_recursive(b, a % b, depth + 1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python euclid_recursive.py <a> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    result = gcd_recursive(a, b)
    print("Result: ", result)
