import pandas as pd
import numpy as np

df = pd.read_csv("prepared_dataset.csv")
print(df.columns)
print(df['class'].unique())