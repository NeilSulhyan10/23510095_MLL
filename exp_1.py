import numpy as np
import matplotlib.pyplot as plt
from statistics import mean, median
from scipy.stats import gmean

def exp1(k=100, N=100):
    change_counts = []

    for _ in range(k):
        arr = np.random.rand(N)
        temp_min = float('inf')
        change_count = 0
        i = 0

        while i < N:
            if arr[i] < temp_min:
                temp_min = arr[i]
                change_count += 1
            i += 1

        change_counts.append(change_count)

    # Plot histogram after collecting all counts
    # plt.hist(change_counts, bins='auto', alpha=0.7, color='skyblue', edgecolor='black')
    # plt.title(f'Histogram of change_counts for N={N}')
    # plt.xlabel('change_counts')
    # plt.ylabel('Frequency')
    # plt.grid(True)
    # plt.show()

    # Calculate statistics
    mean_count = mean(change_counts)
    median_count = median(change_counts)
    geo_mean_count = gmean(change_counts)

    print(f'N = {N}')
    print(f'Mean: {mean_count:.2f}')
    print(f'Median: {median_count:.2f}')
    print(f'Geometric Mean: {geo_mean_count:.2f}')
    print('---------------------------------------')

    return mean_count

# List of N values
N_values = [10, 20, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]

mean_counts = []

# Run analysis for each N
for N in N_values:
    mean_val = exp1(k=100, N=N)
    mean_counts.append(mean_val)

# Plot N vs mean_var_change_count
plt.figure(figsize=(12, 6))
plt.plot(N_values, mean_counts, marker='o', linestyle='-')
plt.xscale('log')
plt.xlabel('Array Size N (log scale)')
plt.ylabel('Mean change_count')
plt.title('N vs Mean change_count')
plt.grid(True)
plt.show()
