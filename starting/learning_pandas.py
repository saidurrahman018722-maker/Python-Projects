import pandas as pd
import numpy as np

data = {
    "name": ["Rafi", "Nila", "Tanvir", "Rafi", "Mim"],
    "age": [25, np.nan, 22, 25, 28],
    "salary": [45000, 62000, np.nan, 45000, 51000]
}

df = pd.DataFrame(data)
print(df.isnull().sum())

df['age'] = df['age'].fillna(df['age'].median())
df['salary'] = df['salary'].fillna(df['salary'].mean())

print(df)

df = df.drop_duplicates()
print(df)
