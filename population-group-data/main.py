import numpy
from tabulate import tabulate
import math

frequently = [3, 7, 10, 5, 8, 15, 9]
data = [[30, 39], [40, 49], [50, 59], [60, 69], [70, 79], [80, 89], [90, 99]]

# Total data yang ada
Y = sum(frequently)
# Mendapatan nilai N / Jumlah data
N = sum(frequently) / 2
# Mendapatkan nilai frekuensi table x
fx = [ sum(x) / 2 for x in data ]
# Mendapatkan interval dari sebuah data
interval = max(data[0]) - min(data[0]) + 1
# Mendapatkan cumulative dari data yang tersedia
cumulative = numpy.cumsum(frequently)
def get_mean() -> int:
    # Mengkalikan antara frequensi X dengan table Frequensi
    result = numpy.multiply(fx, frequently)
    # Return hasil dari pembagian antar data
    return sum(result) / Y

def get_median() -> int:
    # Mendapatkan nilai median frekuensi
    # Ini didapatkan dari nilai cumulative yang lebih besar daripada N
    median_frequently = [ x for x in cumulative if x > N ]
    # Mendapatkan nlai cumulative sebelumnya dari nilai median
    top_cumulative = [x for x in cumulative if x < median_frequently[0]]
    # Mendaaptkan index data cumulative
    index = [x for x in range(len(cumulative)) if cumulative[x] == median_frequently[0]]
    # Mendapatkan nilai terbawah dari nilai cumulative
    get_bottom = [y for x, y in enumerate(data) if x == index[0]]
    # Return Hasil
    result = min(get_bottom[0]) - 0.5 + (((N - top_cumulative[-1])  * interval) / frequently[index[0]])

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
    # Mendapatkan nilai median frekuensi
    # Ini didapatkan dari nilai cumulative yang lebih besar daripada N
    median_frequently = [ x for x in cumulative if x > N ]
    # Mendapatkan nlai cumulative sebelumnya dari nilai median
    top_cumulative = [x for x in cumulative if x < median_frequently[0]]
    # Mendaaptkan index data cumulative
    index = [x for x in range(len(cumulative)) if cumulative[x] == median_frequently[0]]
    # Mendapatkan nilai terbawah dari nilai cumulative
    get_bottom = [y for x, y in enumerate(data) if x == index[0]]
    # Return Hasil
    result = min(get_bottom[0]) - 0.5 + (((N - top_cumulative[-1])  * interval) / frequently[index[0]])

    return result

def get_quartil_three() -> int:
    # Mendapatkan nilai  batas quartil 3
    q3 = ((Y + 1) * 3) / 4
    # Get Cumulative dari Batas Quartil
    get_cumulative_bottom = [ cumulative[x] for x in range(len(cumulative)) if cumulative[x] < q3 ]
    # Get Cumulative dari Batas Quartil
    get_cumulative = [ cumulative[x] for x in range(len(cumulative)) if cumulative[x] > q3 ]
    # Get index by cumulative data
    index = [ x for x in range(len(cumulative)) if cumulative[x] == get_cumulative[0] ]
    # Get data from index
    get_data = [y for x, y in enumerate(data) if x == int("".join(map(str, index)))]
    # Return hasil 
    result = min(get_data[0]) - 0.5 + ((q3 - get_cumulative_bottom[-1]) * interval / frequently[index[0]])

    return result

def get_quartil_one() -> int:
    # Mendapatkan nilai batas quartil 1
    q1 = ((Y + 1) / 4)
    # Get Cumulative dari Batas Quartil
    get_cumulative_bottom = [ cumulative[x] for x in range(len(cumulative)) if cumulative[x] < q1 ]
    # Get Cumulative dari Batas Quartil
    get_cumulative = [ cumulative[x] for x in range(len(cumulative)) if cumulative[x] > q1 ]
    # Get index by cumulative data
    index = [ x for x in range(len(cumulative)) if cumulative[x] == get_cumulative[0] ]
    # Get data from index
    get_data = [y for x, y in enumerate(data) if x == int("".join(map(str, index)))]
    # Return hasil 
    result = min(get_data[0]) - 0.5 + ((q1 - get_cumulative_bottom[-1]) * interval / frequently[index[0]])
    return result

def get_median_deviation() -> int:    
    # Mencari nilai besar rata-rata dari titik tengah dan frekuensi
    fi_xi = numpy.multiply(fx, frequently)
    # Mencari nilai pembatas dengan membagikan dari total fi_xi / frequently
    xA = sum(fi_xi) / Y
    # Mencari nilai dari median xi  - xA
    xi_xA = [ abs(x - xA) for x in fx ]
    # result for calculation
    res = numpy.multiply(xi_xA, frequently)
    # Returh hasil operasi
    return sum(res) / Y

def get_desil(k: int) -> int:
    # Mencari nilai interval desil
    y = (k * Y + 1) / 10
    # Mencari data didalam frekuensi kumulatif yang lebih kecil dari interval desil
    top_cumulative = [x for x in cumulative if x < y]
    # Mencari index dari data kumulative yang lebih besar daripada interval desil
    index = [ x for x in range(len(cumulative)) if cumulative[x] > y]
    # Mendapatkan data dari index yang tersedia 
    get_data = [ data[x] for x in range(len(data)) if x == index[0]]
    # Menghitung hasilnya
    result = min(get_data[0]) + (((y - top_cumulative[-1]) * interval) / frequently[index[0]])
    
    return result

def get_persentil(k: int) -> int:
    # Mencari nilai interval desil
    y = (k * Y) / 100
    # Mencari data didalam frekuensi kumulatif yang lebih kecil dari interval desil
    top_cumulative = [x for x in cumulative if x < y]
    # Mencari index dari data kumulative yang lebih besar daripada interval desil
    index = [ x for x in range(len(cumulative)) if cumulative[x] > y]
    # Mendapatkan data dari index yang tersedia 
    get_data = [ data[x] for x in range(len(data)) if x == index[0]]
    # Menghitung hasilnya
    result = min(get_data[0]) + (((y - top_cumulative[-1]) * interval) / frequently[index[0]])
    
    return result

def get_varians() -> int:
    # Mencari nilai besar rata-rata dari titik tengah dan frekuensi
    fi_xi = numpy.multiply(fx, frequently)
    # Mencari nilai pembatas dengan membagikan dari total fi_xi / frequently
    xA = float(f"{sum(fi_xi) / Y:.1f}")
    # Memangkatkan dari nilai xi dengan 2 dan melakukan pengurangan dari data xi
    xi_xA = [ pow((float(f"{x - xA:.1f}")), 2) for x in fx]
    # Mengkalikan nilai xi - Xa dengan frekuensi
    fi_xA = numpy.multiply(xi_xA, frequently)
    # Menghitung hasil
    return sum(fi_xA) / Y

def get_standar_deviation() -> int:
    # Mencari nilai besar rata-rata dari titik tengah dan frekuensi
    fi_xi = numpy.multiply(fx, frequently)
    # Mencari nilai pembatas dengan membagikan dari total fi_xi / frequently
    xA = float(f"{sum(fi_xi) / Y:.1f}")
    # Memangkatkan dari nilai xi dengan 2 dan melakukan pengurangan dari data xi
    xi_xA = [ pow((float(f"{x - xA:.1f}")), 2) for x in fx]
    # Mengkalikan nilai xi - Xa dengan frekuensi
    fi_xA = numpy.multiply(xi_xA, frequently)
    # Akar kuadrat
    result = math.sqrt(sum(fi_xA) / (sum(frequently) - 1))
    # Menghitung hasil
    return result

if __name__ == "__main__":
    head = ["Judul", "Hasil"]
    data = [
        ["Mean", f"{get_mean()}"],
        ["Median", f"{get_median()}"],
        ["Modus", f"{get_modus():.3f}"],
        ["Quartil 1", f"{get_quartil_one():.3f}"],
        ["Quartil 2", f"{get_quartil_two():.3f}"],
        ["Quartil 3", f"{get_quartil_three():.3f}"],
        ["Jangkauan Quartil", f"{get_quartil_three() - get_quartil_one():.3f}"],
        ["Simpangan Rata Rata", f"{get_median_deviation():.3f}"],
        ["Desil 7", f"{get_desil(7):.3f}"],
        ["Persentil 50", f"{get_persentil(50):.3f}"],
        ["Varians", f"{get_varians():.3f}"],
        ["Standar Deviasi", f"{get_standar_deviation():.3f}"],
    ]

    print(tabulate(data, headers=head, tablefmt="simple_grid"))
