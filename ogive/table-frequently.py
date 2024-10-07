import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

data = [60, 50, 40, 35, 56, 50, 34, 50, 60, 40, 35, 50, 30, 54, 52, 70, 45, 65, 30, 48, 65, 24, 67, 89, 34, 77, 54, 61, 32, 61, 43, 23, 52, 78, 74, 27, 43, 55, 78, 82, 49, 45, 76, 32, 85, 29, 42, 61, 76, 91]

df = pd.DataFrame(data, columns=['Values'])

# untuk menghitung total kelas
count = round(1 + 3.3 * math.log10(len(data)))

# count max interval one class
interval = round((max(data) - min(data)) / count)

# count bins value with arange numpy
bins = np.arange(min(data), 100, interval)

freq_table = pd.cut(df['Values'], bins=bins, right=False).value_counts().sort_index()

# Membuat DataFrame dari tabel frekuensi
freq_df = freq_table.reset_index()
freq_df.columns = ['Interval', 'Frekuensi']

# Memformat kelas menjadi format yang diinginkan
freq_df['Interval'] = freq_df['Interval'].apply(lambda x: f"{int(x.left)}-{int(x.right) - 1}")

# Menampilkan tabel frekuensi
print(freq_df)