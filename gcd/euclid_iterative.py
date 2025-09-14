# Iterative version of Euclid's algorithm
import sys

def gcd_iterative(a: int, b: int) -> int:
    """Compute GCD using the iterative Euclidean algorithm, printing each step for clarity"""
    print(f"Finding the GCD for: ({a}, {b}")

    step = 1
    while b != 0:
        print(f"Step: {step}: a = {a}, b = {b} -> a % b = {a % b}")
        temp = a
        a = b
        b = temp % a
        step += 1

    print(f"Final step: a = {a}, b = {b} -> GCD = {abs(a)}")
    return abs(a)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python euclid_iterative.py <a> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    result = gcd_iterative(a,b)
    print("Result: ", result)
