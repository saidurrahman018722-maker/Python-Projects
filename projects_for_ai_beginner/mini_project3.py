import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2026-01-01", end="2026-03-31", freq="D")
print(dates)
categories = ["Food", "Transport", "Shopping", "Bills", "Entertainment"]

data = {
    "date": np.random.choice(dates, 150),
    "category": np.random.choice(categories, 150),
    "amount": np.random.randint(50, 2000, 150)
}

df = pd.DataFrame(data)
df = df.sort_values("date").reset_index(drop=True)
df.to_csv(r"D:\Backend\Learning Python\projects_for_ai_beginner\csv_project_3.csv", index=False)
data = pd.read_csv(
    r"D:\Backend\Learning Python\projects_for_ai_beginner\csv_project_3.csv")

data['date'] = pd.to_datetime(data['date'])

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["weekday"] = df["date"].dt.day_name()

print(df.head(10))

catagory_wish_cost = data.groupby(
    'category')['amount'].sum().sort_values(ascending=False)

print(catagory_wish_cost)


def monthly_trend(df):
    monthly = df.groupby("month")["amount"].sum()
    print("\n📅 মাসিক খরচ:")
    print(monthly)

    import matplotlib.pyplot as plt
    monthly.plot(kind="line", marker="o", x='Month',
                 y='Total Cost', figsize=(8, 4))
    plt.title("Monthly Cost Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Cost")
    plt.grid(True)
    plt.show()


monthly_trend(df)


def weekday_pattern(df):
    weekday_avg = df.groupby("weekday")["amount"].mean().round(3)
    order = ["Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_avg = weekday_avg.reindex(order)

    print("\n📆 In which weekday You have Spended the Most Amount of Money:")
    print(weekday_avg)


weekday_pattern(df)
