import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)
n = 150

df = pd.DataFrame({
    "student_id": range(1, n+1),
    "study_hours": np.random.randint(1, 10, n),
    "attendance_percent": np.random.randint(50, 100, n),
    "sleep_hours": np.random.randint(4, 9, n),
    "social_media_hours": np.random.randint(0, 6, n),
})

df["marks"] = (
    df["study_hours"] * 6 +
    df["attendance_percent"] * 0.3 -
    df["social_media_hours"] * 2 +
    np.random.normal(0, 5, n)
).clip(0, 100).round(1)

print(df.head())

corr = df[['marks', "student_id", "study_hours",
           "attendance_percent", "sleep_hours", "social_media_hours"]].corr()

print(corr['marks'].sort_values(ascending=False))
plt.scatter(df['study_hours'], df['marks'], alpha=0.5)
plt.title("The Relation Between study hours vs marks")
plt.ylabel('marks')
plt.xlabel('study hours')
plt.tight_layout()
# plt.show()


fig, ax = plt.subplots(figsize=(6, 5))
cax = ax.matshow(corr, cmap="coolwarm")
plt.colorbar(cax)
ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45)
ax.set_yticklabels(corr.columns)
plt.title("Correlation Heatmap")
# plt.show()


dates = pd.date_range(start="2025-01-01", end="2026-06-30", freq="D")
sales = pd.DataFrame({
    "date": dates,
    "revenue": np.random.randint(5000, 15000, len(dates)) +
    np.sin(np.arange(len(dates)) * 2 * np.pi / 365) * 3000   # seasonal pattern
})
sales["revenue"] = sales["revenue"].round(0)

sales["month"] = sales["date"].dt.to_period("M")
monthly_revenue = sales.groupby("month")["revenue"].sum()
print(monthly_revenue.tail())


print(np.arange(len(dates)))
sales["revenue_7day_avg"] = sales["revenue"].rolling(window=7).mean()
sales["revenue_30day_avg"] = sales["revenue"].rolling(window=30).mean()

plt.figure(figsize=(12, 5))
plt.plot(sales["date"], sales["revenue"],
         alpha=0.3, label="Daily Earnings(Real)")
plt.plot(sales["date"], sales["revenue_7day_avg"],
         color="red", label="7-days avarage")
plt.plot(sales["date"], sales["revenue_30day_avg"],
         color="black", label="30-days avarage")
plt.legend()
plt.title("Daily earings vs 7 days Moving Average")
plt.show()
