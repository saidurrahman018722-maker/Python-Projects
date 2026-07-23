import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error, f1_score, recall_score, precision_score, accuracy_score

np.random.seed(42)
n = 200

df = pd.DataFrame({
    "sqft": np.random.randint(600, 3500, n),
    "bedrooms": np.random.randint(1, 6, n),
    "age_years": np.random.randint(0, 40, n),
    "distance_from_city_km": np.random.uniform(1, 30, n)
})
df["price"] = (
    df["sqft"] * 150 +
    df["bedrooms"] * 200000 -
    df["age_years"] * 3000 -
    df["distance_from_city_km"] * 8000 +
    np.random.normal(0, 150000, n)
).clip(500000, None)


X = df[["sqft", "bedrooms", "age_years", "distance_from_city_km"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

single_tree = DecisionTreeRegressor(random_state=42)
linear_model = LinearRegression()
forest_reg = RandomForestRegressor(random_state=42)


single_tree.fit(X_train, y_train)
linear_model.fit(X_train, y_train)
forest_reg.fit(X_train, y_train)

single_tree_prediction = single_tree.predict(X_test)
linear_model_prediction = linear_model.predict(X_test)
forest_reg_prediction = forest_reg.predict(X_test)


print(f"\n\nthe answer is : {y_test}\n\n")
print(
    f"the linear model's prediction is : {linear_model_prediction}\n RMSE: {root_mean_squared_error(y_test, linear_model_prediction)}  R_2 : {r2_score(y_test, linear_model_prediction)}\n\n")

print(
    f"the single Decision Tree model's prediction is : {single_tree_prediction}\n MAE: {mean_absolute_error(y_test, single_tree_prediction)}  R_2 : {r2_score(y_test, single_tree_prediction)}\n\n")

print(
    f"the Random Forest Reg model's prediction is : {linear_model_prediction}\n MAE: {mean_absolute_error(y_test, forest_reg_prediction)}  R_2 : {r2_score(y_test, forest_reg_prediction)}\n\n")


np.random.seed(1)
n = 200

df2 = pd.DataFrame({
    "study_hours_per_week": np.random.randint(1, 20, n),
    "attendance_percent": np.random.randint(50, 100, n),
    "sleep_hours": np.random.randint(4, 9, n),
    "previous_grade": np.random.randint(40, 100, n)
})

df2["final_grade"] = (
    df2["study_hours_per_week"] * 1.5 +
    df2["attendance_percent"] * 0.3 +
    df2["previous_grade"] * 0.4 +
    np.random.normal(0, 5, n)
).clip(0, 100)


df2["study_efficiency"] = df2["study_hours_per_week"] / df2["sleep_hours"]

X2 = df2[["study_hours_per_week", "attendance_percent", "sleep_hours",
          "previous_grade", "study_efficiency"]]
y2 = df2["final_grade"]

X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2, y2, test_size=0.2, random_state=42)

model2 = RandomForestRegressor(random_state=42)
model2.fit(X2_train, y2_train)
pred2 = model2.predict(X2_test)

print(f"R² Score: {r2_score(y2_test, pred2):.3f}")

importance = pd.Series(model2.feature_importances_,
                       index=X2.columns).sort_values(ascending=False)
print(importance)


# calssification Models

np.random.seed(7)
n = 300

df3 = pd.DataFrame({
    "income": np.random.randint(15000, 120000, n),
    "credit_score": np.random.randint(400, 850, n),
    "loan_amount": np.random.randint(50000, 2000000, n),
    "employment_years": np.random.randint(0, 25, n)
})

approval_score = (
    (df3["income"] > 40000).astype(int) +
    (df3["credit_score"] > 650).astype(int) +
    (df3["employment_years"] > 2).astype(int) -
    (df3["loan_amount"] > 1000000).astype(int)
)
df3["approved"] = (approval_score >= 2).astype(int)

X3 = df3[["income", "credit_score", "loan_amount", "employment_years"]]
y3 = df3["approved"]

X3_train, X3_test, y3_train, y3_test = train_test_split(
    X3, y3, test_size=0.2, random_state=42, stratify=y3)


clf_models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
}

clf_results = []
for name, model in clf_models.items():
    model.fit(X3_train, y3_train)
    preds = model.predict(X3_test)
    clf_results.append({
        "Model": name,
        "Accuracy": accuracy_score(y3_test, preds),
        "Precision": precision_score(y3_test, preds),
        "Recall": recall_score(y3_test, preds),
        "F1 Score": f1_score(y3_test, preds)
    })

print(pd.DataFrame(clf_results))
