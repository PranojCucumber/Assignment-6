import time
import numpy as np
import random

# Deterministic algorithm (Median of Medians)
def median_of_medians(arr, k):
    if len(arr) <= 10:
        return sorted(arr)[k]
    medians = [sorted(arr[i:i + 5])[len(arr[i:i + 5]) // 2] for i in range(0, len(arr), 5)]
    pivot = median_of_medians(medians, len(medians) // 2)
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = arr.count(pivot)
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + pivot_count:
        return pivot
    else:
        return median_of_medians(high, k - len(low) - pivot_count)

# Randomized algorithm (Randomized Quickselect)
def randomized_quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = arr.count(pivot)
    if k < len(low):
        return randomized_quickselect(low, k)
    elif k < len(low) + pivot_count:
        return pivot
    else:
        return randomized_quickselect(high, k - len(low) - pivot_count)

# Test setup: generating different types of arrays and measuring execution times
def test_selection_algorithms():
    sizes = [10, 100, 1000, 5000, 10000]  # Different input sizes
    distributions = ["random", "sorted", "reverse_sorted"]
    results = []

    for size in sizes:
        for dist in distributions:
            if dist == "random":
                arr = np.random.randint(0, size * 10, size).tolist()
            elif dist == "sorted":
                arr = sorted(np.random.randint(0, size * 10, size).tolist())
            elif dist == "reverse_sorted":
                arr = sorted(np.random.randint(0, size * 10, size).tolist(), reverse=True)

            k = size // 2  # Median element

            # Measure deterministic algorithm
            start_time = time.time()
            median_of_medians(arr, k)
            deterministic_time = time.time() - start_time

            # Measure randomized algorithm
            start_time = time.time()
            randomized_quickselect(arr, k)
            randomized_time = time.time() - start_time

            results.append((size, dist, deterministic_time, randomized_time))
    
    return results

# Run the test
results = test_selection_algorithms()

# Format and return results for display
import pandas as pd

results_df = pd.DataFrame(results, columns=["Size", "Distribution", "Deterministic Time (s)", "Randomized Time (s)"])
results_df
