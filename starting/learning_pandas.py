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

data = pd.DataFrame({'color': ['Red', 'Green', 'Blue', 'Red']})

print(pd.get_dummies(data, prefix="color", drop_first=True, dtype=int))


A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6, 3],
              [7, 8, 3]])

result = np.matmul(A, B)
print(result)
