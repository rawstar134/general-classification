import pandas as pd
import numpy as np
#check the original data file
df = pd.read_csv("prepared_dataset.csv")
print(df.columns)
print(df['class'].unique())