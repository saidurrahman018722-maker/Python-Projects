import pandas as pd
import numpy as np


np.random.seed(42)

birth_dates = pd.date_range(start='1960-1-1', end='2010-1-1', freq="YE")

data = {
    "birth_date": np.random.choice(birth_dates, 10)
}
df = pd.DataFrame(data)

df['age'] = (pd.Timestamp.now()-df['birth_date']).dt.days//365.25

df['category'] = pd.cut(
    df['age'],
    bins=[0, 30, 50, 70],
    labels=["Child", "Middle Aged", "Senior"]
)


print(df)

# One-HOT Encoding.......
city = ['dhaka', 'chitagong', 'kulna', 'rajshahi', 'sylhet']

data_2 = {
    'visited_cities': np.random.choice(city, 20)
}

df_2 = pd.DataFrame(data_2)
df_2 = pd.get_dummies(df_2['visited_cities'], prefix='city_name',
                      drop_first=True)
print(df_2)
