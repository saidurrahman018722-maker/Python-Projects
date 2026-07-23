import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Data
df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 3, 5, 7, 2],
    "attendance_percent": [60, 65, 70, 75, 80, 88, 92, 98, 68, 82, 90, 63],
    "marks": [40, 45, 55, 60, 70, 78, 85, 95, 52, 72, 88, 42]
})

X = df[["study_hours", "attendance_percent"]]
y = df["marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual marks:", list(y_test))
print("Predicted marks:", predictions.round(1))

print("Mean Absulute Error:", mean_absolute_error(
    y_test, predictions).__round__(2))
print("R2 Squared:(How effeciantly my model can make predictions):",
      r2_score(y_test, predictions).__round__(2))

print("Weights (w):", model.coef_)
print("Bias (b):", model.intercept_)

# শুধু study_hours দিয়ে simple model (visualize করার সুবিধার জন্য)
X_simple = df[["study_hours"]]
y_simple = df["marks"]

model_simple = LinearRegression()
model_simple.fit(X_simple, y_simple)

plt.scatter(df["study_hours"], df["marks"], label="আসল data")
plt.plot(df["study_hours"], model_simple.predict(
    X_simple), color="red", label="Model-এর রেখা")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.title("Linear Regression Fit")
plt.show()
