import math
from typing import List, Optional

def permutation(arr: List[str] | List[int], x: int) -> int | float:
    res = math.factorial(len(arr)) / math.factorial((len(arr) - x))
    return res

def combination(n: int, k: int) -> int | float:
    res = math.factorial(n) / (math.factorial(k) * math.factorial((n - k)))
    return res

if __name__ == "__main__":
    arr = ["A", "B", "C", "D", "E", "F"]

    print(f"Banyak susunan dari 3 huruf: {permutation(arr, 3)}")
    print(f"Banyak anggota yang terbentuk: {combination(10, 3)}")
    print(f"Keanggotaan terdiri dari 2 Pria dan 1 Wanita: {combination(4, 2) * combination(6, 1)}")