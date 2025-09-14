# GCD Algorithms

This folder demonstrates **Euclid’s Algorithm** for finding the Greatest Common Divisor (GCD) of two integers.  
Two versions are provided: **iterative** and **recursive**, each with detailed step-by-step output for teaching and learning.

---

## 📜 Files
- `euclid_iterative.py` – Iterative version of Euclid’s algorithm with step tracing.  
- `euclid_recursive.py` – Recursive version of Euclid’s algorithm with call tracing.   

---

## ▶️ Running the Programs

### Command-line arguments
From the repo root:
```bash
python gcd/euclid_iterative.py 14300 5915
python gcd/euclid_recursive.py 14300 5915
```

## Example Output 

### Iterative
```bash 
Starting iterative GCD for (14300, 5915)
Step 1: a = 14300, b = 5915 → a % b = 2470
Step 2: a = 5915,  b = 2470 → a % b = 975
Step 3: a = 2470,  b = 975  → a % b = 520
Step 4: a = 975,   b = 520  → a % b = 455
Step 5: a = 520,   b = 455  → a % b = 65
Step 6: a = 455,   b = 65   → a % b = 0
Final step: a = 65, b = 0 → GCD = 65
Result: 65
```

### Recursive
```bash
Call 1: gcd_recursive(14300, 5915)
Call 2: gcd_recursive(5915, 2470)
Call 3: gcd_recursive(2470, 975)
Call 4: gcd_recursive(975, 520)
Call 5: gcd_recursive(520, 455)
Call 6: gcd_recursive(455, 65)
Call 7: gcd_recursive(65, 0)
Base case reached at depth 7: GCD = 65
Result: 65
```

