import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

# data array
data = [60, 50, 40, 35, 56, 50, 34, 50, 60, 40, 35, 50, 30, 54, 52, 70, 45, 65, 30, 48, 65, 24, 67, 89, 34, 77, 54, 61, 32, 61, 43, 23, 52, 78, 74, 27, 43, 55, 78, 82, 49, 45, 76, 32, 85, 29, 42, 61, 76, 91]

# untuk menghitung total kelas
count = round(1 + 3.3 * math.log10(len(data)))

# count max interval one class
interval = round((max(data) - min(data)) / count)

# count bins value with arange numpy
bins = np.arange(min(data), 100, interval)

# count for base number
values, base = np.histogram(data, bins=bins)
# Output: [ 8  7 12  9  4  7  3]

# create cumulative number
cumsum = np.cumsum(values)
# Output: [ 8 15 27 36 40 47 50]

# create cumulative for ogive negatif
z = sum(values)
current = z
result = [z]

for value in values:
    current -= value
    if current > 0:
        result.append(current)
# Output: [50, 42, 35, 23, 14, 10, 3]

figure, (ax1, ax2, ax3) = plt.subplots(1, 3)

# histogram graphic
ax1.set_title("Histogram Graphic")
ax1.hist(data, bins=bins)

# Ogive positif
ax2.set_title("Ogive Positif")
ax2.plot(base[1:], cumsum, color='red', marker='o', linestyle='-')

# ogive negatif
ax3.set_title("Ogive Negatif")
ax3.plot(base[1:], result, color='red', marker='o', linestyle='-')

plt.show()