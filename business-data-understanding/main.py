# Download File Kaggle
# import kagglehub
# path = kagglehub.dataset_download("bhanupratapbiswas/fashion-products")
# print(f"Download: {path}")

import pandas as pd

data = pd.read_csv('./fashion_products.csv')
df = pd.DataFrame(data)
df[df["Rating"] > 4].to_csv("fashion_products_rate.csv")