import numpy

frequently = [3, 7, 10, 5, 8, 15, 9]
data = [[30, 39], [40, 49], [50, 59], [60, 69], [70, 79], [80, 89], [90, 99]]

# Mendapatan nilai N / Jumlah data
N = round(sum(frequently) / 2)
# Mendapatkan nilai frekuensi table x
fx = [ sum(x) / 2 for x in data ]
# Mendapatkan interval dari sebuah data
interval = max(data[0]) - min(data[0]) + 1
# Mendapatkan cumulative dari data yang tersedia
cumulative = numpy.cumsum(frequently)
# Mendapatkan nilai batas quartil 1
q1 = (sum(frequently) / 4)
# Mendapatkan nilai  batas quartil 2
q2 = (sum(frequently) * 2) / 4
# Mendapatkan nilai  batas quartil 3
q3 = (sum(frequently) * 3) / 4

def get_mean() -> int:
    # Mengkalikan antara frequensi X dengan table Frequensi
    result = numpy.multiply(fx, frequently)

    # Return hasil dari pembagian antar data
    return sum(result) / sum(frequently)

def get_median() -> int:
    # Mendapatkan nilai median frekuensi
    # Ini didapatkan dari nilai cumulative yang lebih besar daripada N
    median_frequently = [ x for x in cumulative if x > N ]

    # Mendapatkan nlai cumulative sebelumnya dari nilai median
    top_cumulative = [x for x in cumulative if x < median_frequently[0]]

    # Mendaaptkan index data cumulative
    index = [x for x in range(len(cumulative)) if cumulative[x] == median_frequently[0]]

    # Mendapatkan nilai terbawah dari nilai cumulative
    get_bottom = [y for x, y in enumerate(data) if x == int("".join(map(str, index)))]
    
    # Return Hasil
    result =  min(get_bottom[0]) - 0.5 + (((N - top_cumulative[-1]) * interval) / frequently[index[0]])
    return result

def get_modus() -> int:
    # Mendapatkan index bedasrkan nilai maximal frekuensi
    index = [ x for x in range(len(frequently)) if frequently[x] == max(frequently)]

    # Mendapatkn nilai tertinggi bedasarkan dari index yang didapat
    get_max = [ data[x] for x in range(len(data)) if index[0] == x]

    # Mendapatkan frekuensi yang lebih kecil dari nilai maximal
    last_index = [ x for x in frequently if x < max(frequently)]

    # Return hasil
    result = min(get_max[0]) - 0.5 + ((max(frequently) - last_index[-1]) * interval) / ((max(frequently) - last_index[-1]) + max(frequently))
    return result

def get_quartil_two() -> int:
    # Get Cumulative dari Batas Quartil
    get_cumulative = [ cumulative[x] for x in range(len(cumulative)) if cumulative[x] > q2 ]

    # Get index by cumulative data
    index = [ x for x in range(len(cumulative)) if cumulative[x] == get_cumulative[0] ]

    # Get data from index
    get_data = [y for x, y in enumerate(data) if x == int("".join(map(str, index)))]

    # Return hasil 
    result = min(get_data[0]) - 0.5 + (abs(q2 - get_cumulative[0]) * interval / frequently[index[0]])

    return result

def get_quartil_three() -> int:
    # Get Cumulative dari Batas Quartil
    get_cumulative = [ cumulative[x] for x in range(len(cumulative)) if cumulative[x] > q3 ]

    # Get index by cumulative data
    index = [ x for x in range(len(cumulative)) if cumulative[x] == get_cumulative[0] ]

    # Get data from index
    get_data = [y for x, y in enumerate(data) if x == int("".join(map(str, index)))]

    # Return hasil 
    result = min(get_data[0]) - 0.5 + (abs(q3 - get_cumulative[0]) * interval / frequently[index[0]])

    return result

def get_quartil_one() -> int:
    # Get Cumulative dari Batas Quartil
    get_cumulative = [ cumulative[x] for x in range(len(cumulative)) if cumulative[x] > q1 ]

    # Get index by cumulative data
    index = [ x for x in range(len(cumulative)) if cumulative[x] == get_cumulative[0] ]

    # Get data from index
    get_data = [y for x, y in enumerate(data) if x == int("".join(map(str, index)))]

    # Return hasil 
    result = min(get_data[0]) - 0.5 + (abs(q1 - get_cumulative[0]) * interval / frequently[index[0]])

    return result

print(f"Mean: {get_mean()}")
print(f"Median: {get_median()}")
print(f"Modus:  {get_modus()}")
print(f"Quartil 1:  {get_quartil_one()}")
print(f"Quartil 2:  {get_quartil_two()}")
print(f"Quartil 3:  {get_quartil_three()}")