from typing import List, Optional
from collections import Counter

def factorial(num: int) -> int:
    fct = 1
    if num < 0:
        return 0
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            fct = fct * i
        
        return fct

def probability(m: int,  n: int, opsi: str = "dadu", flag: str = ">") -> int:
    if opsi == "dadu":
        if flag == ">":
            a = 6 - m
            b = a / 6
            res = [ b for x in range(n)]
            return sum(res)
        elif flag == "<":
            a = 5 - (6 - m)
            b = a / 6
            res = [ b for x in range(n)]
            return sum(res)
        else:
            return sum([(m / 6) for x in range(n)])
    else:
        return m / n

def loop_probability(m: int, n: int, count: int):
    res = m / n
    for i in range(count):
        if i > 0:
            a = m - 1
            b = a / (n - 1)
            res *= b
        
    
    return res

def permutation_k(arr: List[str] | List[int], x: int) -> int | float:
    res = factorial(len(arr)) / factorial((len(arr) - x))
    return res

def permutation_n(n: int | str, y: List[int] | None) -> int:
    if type(n) is str:
        x = factorial(len(n))
        k = [ char for char, count in Counter(n).items() if count > 1 ]
        b = [ n.count(i) for i in k if len(k) > 1 ]
        num = [ factorial(x) for x in b if len(b) > 1]
        res = lambda nums: x / sum(nums) if len(nums) > 0 else x / 1
        return res(num)
    else:
        x = factorial(len(n))
        num = [ factorial(x) for x in y ]
        return x / sum(num)

def combination(n: int, k: int) -> int | float:
    res = factorial(n) / (factorial(k) * factorial((n - k)))
    return res

def loop_combination(n: int, r: int) -> int | float:
    x = n + r - 1
    res = factorial(x) / (factorial(r) * factorial((x - r)))
    return res

def harapan(x: List[int], y: List[int], n: int) -> int:
    k = [i / n for i in y]
    multiply = [a * b for a, b in zip(x, k)]
    return sum(multiply)

if __name__ == "__main__":
    arr = ["A", "B", "C", "D", "E", "F"]

    print(f"Banyak susunan dari 3 huruf: {permutation_k(arr, 3)}")
    print(f"Banyak anggota yang terbentuk: {combination(10, 3)}")
    print(f"Keanggotaan terdiri dari 2 Pria dan 1 Wanita: {combination(4, 2) * combination(6, 1)}")
    print(f"Banyak cara Minimal 2 Perempuan: {harapan(x=[2, 3, 4], y=[3, 2, 1], n=8)}")
    print(f"Banyak peluang dadu yang lebih dari 4 dalam 6 iterasi adalah: {probability(4, 6, "dadu", ">")}")
    print(f"Cara 4 buku dalam 1 rauk: {factorial(4)}")
    print(f"Cara memilih 3 orang dari 10 orang: {combination(10, 3)}")

    print(f"Probabilitas bola kedua bewarna biru adalah: {loop_probability(m=4, n=7, count=0)}")
    print(f"Harapan dari X: {harapan(x=[1, 2, 3, 4, 5, 6], y=[1, 1, 1, 1, 1, 1], n=6)}")
    print(f"Kedua bola bewarna putih: {loop_probability(m=7, n=10, count=2)}")
    print(f"Banyak cara mengatur kata 'PELUANG' adalah: {permutation_n(n="PELUANG", y=None)}")
    print(f"Cara untuk mendapatkan 3 buah dari 5 jenis buah: {loop_combination(n=5, r=3)}")
