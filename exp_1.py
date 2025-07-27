import numpy as np
import matplotlib.pyplot as plt
from statistics import mean, median
from scipy.stats import gmean

def exp1(k=100, n=100):
    change_counts = []

    for _ in range(k):
        arr = np.random.rand(n)
        temp_min = float('inf')
        change_count = 0
        i = 0

        while i < n:
            if arr[i] < temp_min:
                temp_min = arr[i]
                change_count += 1
            i += 1
        change_counts.append(change_count)

    mean_count = mean(change_counts)
    median_count = median(change_counts)
    geo_mean_count = gmean(change_counts)

    #Individual Grphs
    plt.hist(change_counts, bins='auto', alpha=0.7, color='skyblue', edgecolor='black')
    plt.axvline(mean_count, color='red', linestyle='dashed', linewidth=1, label='Mean')
    plt.axvline(median_count, color='green', linestyle='dashed', linewidth=1, label='Median')
    plt.title(f'Histogram of change_counts for N={n}')
    plt.xlabel('change_counts')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.legend()
    plt.show()  

    print(f'N = {N}')
    print(f'Mean: {mean_count:.2f}')
    print(f'Median: {median_count:.2f}')
    print(f'Geometric Mean: {geo_mean_count:.2f}')
    print('---------------------------------------')

    return mean_count

N_values = [10, 20, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
mean_counts = []
for N in N_values:
    mean_val = exp1(k=100, n=N)
    mean_counts.append(mean_val)
log_n = np.log(N_values)

# N vs Mean Counts
plt.figure(figsize=(12, 6))
plt.plot(N_values, mean_counts, marker='o', label='N vs Mean', linestyle='-')
plt.plot(N_values, log_n, color = "red", label = "logn", linestyle = "--")
plt.xlabel('N Values')
plt.ylabel('Mean change_count')
plt.title('N vs Mean change_count')
plt.grid(True)
plt.legend()
plt.show()

"""
Observations: 
1. Histogram is in Normal Distribution and 
2. N vs Mean :- Plotting is simliar to that of Log N, i.e mean of number of swaps increases slowly as N ncreases
"""
