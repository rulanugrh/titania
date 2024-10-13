# Download File Kaggle
# import kagglehub
# path = kagglehub.dataset_download("bhanupratapbiswas/fashion-products")
# print(f"Download: {path}")

import pandas as pd
import sys

df = pd.DataFrame(pd.read_csv('./fashion_products.csv'))
data = df[df["Rating"] > 4]

def info():
    return data.info()

def get_null():
    msg = ""

    if data.isnull().sum().sum() <= 0:
        msg += "Data tidak ada yang Null"
    else:
        msg += f"Total data null adalah: {data.isnull().sum().sum()}"
    
    return msg

def main(argv: str):
    if argv == "info":
        info()
    elif argv == "get_null":
        print(get_null())
    else:
        print("Sorry invalid command: \npython main.py [args] \n\ninfo (for get info dataset) \nnull (for get data null) \nhistogram (for get histogram data)\n")

if __name__ == "__main__":

    arg = sys.argv[1]
    main(argv=arg)