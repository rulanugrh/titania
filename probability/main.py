import math
from typing import List, Optional

def permutation(arr: List[str] | List[int], x: int) -> int | float:
    res = math.factorial(len(arr)) / math.factorial((len(arr) - x))
    return res

def combination(n: int, k: int) -> int | float:
    res = math.factorial(n) / (math.factorial(k) * math.factorial((n - k)))
    return res

def harapan(x: List[int], y: List[int], n: int) -> int:
    k = [i / n for i in y]
    multiply = [a * b for a, b in zip(x, k)]
    return sum(multiply)

if __name__ == "__main__":
    arr = ["A", "B", "C", "D", "E", "F"]

    print(f"Banyak susunan dari 3 huruf: {permutation(arr, 3)}")
    print(f"Banyak anggota yang terbentuk: {combination(10, 3)}")
    print(f"Keanggotaan terdiri dari 2 Pria dan 1 Wanita: {combination(4, 2) * combination(6, 1)}")
    print(f"Banyak cara Minimal 2 Perempuan: {harapan(x=[2, 3, 4], y=[3, 2, 1], n=8)}")