# Big-O Growth Exploration

This project demonstrates how different algorithm complexities behave as input size grows.  
It includes **reference implementations**, a **timing harness**, and **plots** so you can see the difference between constant, logarithmic, linear, `n log n`, quadratic, and exponential growth.

---

## Files

- `algorithms.py` — reference implementations:
  - **O(1)** — `first_element`, `is_even`
  - **O(log n)** — `binary_search_steps`
  - **O(n)** — `linear_sum`
  - **O(n log n)** — `merge_sort`
  - **O(n²)** — `quadratic_pairs`
  - **O(2ⁿ)** — `fib_exp` (naive recursion)
- `run_experiments.py` — run timing experiments and print results in a table
- `plot_results.py` — generate one plot per function (`.png` images in `plots/`)
- `test_big_o.py` — sanity tests for correctness

---

## Running the Experiments

From the repo root:

```bash
python big-o/run_experiments.py
```
## Sample Output 
O(1) — first_element
--------------------
first_element       | n=1000000  |     0.0000 ms

O(n) — linear_sum
-----------------
linear_sum          | n=10000    |     0.2100 ms
linear_sum          | n=50000    |     1.0200 ms
linear_sum          | n=100000   |     2.0500 ms

O(n log n) — merge_sort
-----------------------
merge_sort          | n=5000     |   42.0000 ms
merge_sort          | n=20000    |  200.0000 ms
merge_sort          | n=50000    |  580.0000 ms

## Plotting the Curves 
```bash
python big-o/plot_results.py
```
- charts are saved to `big-o/plots` (e.g., `merge_sort.png`, `linear_sum.png`).
- Use `--fast` for smaller sizes 

```bash
  python big-o/plot_results.py --fast
```

- Run only certain algorithms:
```bash
  python big-o/plot_results.py --only linear_sum,merge_sort
```
- Save results to a CSV:
```bash
  python big-o/plot_results.py --csv big-o/plots/results.csv
```

## Testing 
Run basic correctness tests with `pytest`:
```bash
pytest big-o/test_big_o.py -q
```
---

## License
This project is licensed under the **MIT License**.
You are free to use, modify, and distribute this code for educational and non-commercial purposes  
