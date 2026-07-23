import pandas as pd
import numpy as np


df = pd.read_csv(
    r"D:\Backend\Learning Python\projects_for_ai_beginner\csv_project_3.csv")

print(df)
df['date'] = pd.to_datetime(df['date'])

# 1


def to_n_expresses(df, n):
    print(df.sort_values(by='amount', ascending=False).head(n))


to_n_expresses(df, 3)


def trend(df):
    data = df.groupby(['month', 'category'])['amount'].sum()
    print(data)


trend(df)


def most_transaction(df):
    data = df.groupby('category')['amount'].count().sort_values()
    print(data)
    make = pd.DataFrame(data)

    print(make.sort_values(by="amount", ascending=False))


most_transaction(df)
