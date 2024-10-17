# Download File Kaggle
# import kagglehub
# path = kagglehub.dataset_download("bhanupratapbiswas/fashion-products")
# print(f"Download: {path}")

# Import Pandas Library
import pandas as pd
import sys

# Read dataset and convert to data fraame
df = pd.DataFrame(pd.read_csv('./fashion_products.csv'))
# Grouping to data frame if Rating > 4
data = df[df["Rating"] > 4]

def printout():
    """
    # Description
    Printout dataframe for get all data

    Returns:
        Return data
    """
    return data

def info():
    """
    # Description
    Get info dataset 

    Returns:
        info about dataset
    """
    return data.info()

def get_by_category(category: str) -> pd.DataFrame:
    """
    # Description
    Function for get data by category (Women, Men, and Kids)

    Args:
        category (str): variabel like a women, men and kids

    Returns:
        pd.DataFrame: returning dataframe with contains string
    """
    result = data[data['Category'].str.contains(category)]
    return result

def get_by_product(product: str) -> pd.DataFrame:
    """
    # Description
    Function for get data by product

    Args:
        product (str): variabel to get data

    Returns:
        pd.DataFrame: returning dataframe with contains string
    """
    result = data[data['Product Name'].str.contains(product)]
    return result

def get_null():
    """
    # Description
    To sum null data

    Returns:
        Return total data null
    """
    msg = ""

    if data.isnull().sum().sum() <= 0:
        msg += "Data tidak ada yang Null"
    else:
        msg += f"Total data null adalah: {data.isnull().sum().sum()}"
    
    return msg

def main(argv: str, flag: str):
    """
    # Description
    Function main to running all function

    Args:
        argv (str): string option / flag
    """
    if argv == "info":
        info()
    elif argv == "get_null":
        print(get_null())
    elif argv == "printout":
        print(printout())
    elif argv == "get_by_category":
        if flag == "women":
            print(get_by_category("Women"))
        elif flag == "men":
            print(get_by_category("Men"))
        elif flag == "kids":
            print(get_by_category("Kids"))
    elif argv == "get_by_product":
        if flag == "shirt":
            print(get_by_product("T-shirt"))
        elif flag == "dress":
            print(get_by_product("Dress"))
        elif flag == "sweater":
            print(get_by_product("Sweater"))
        elif flag == "jeans":
            print(get_by_product("Jeans"))
        elif flag == "shoes":
            print(get_by_product("Shoes"))
    else:
        print("Sorry invalid command: \npython main.py [args] \n\ninfo (for get info dataset) \nnull (for get data null) \nhistogram (for get histogram data)\n")

if __name__ == "__main__":

    arg = sys.argv[1]
    flag = sys.argv[2]
    main(argv=arg, flag=flag)