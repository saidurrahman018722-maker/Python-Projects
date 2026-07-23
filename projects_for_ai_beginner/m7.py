import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


n = 300

df = pd.DataFrame({
    "income": np.random.randint(15000, 120000, n),
    "credit_score": np.random.randint(400, 850, n),
    "loan_amount": np.random.randint(50000, 2000000, n),
    "employment_years": np.random.randint(0, 25, n)
})

approval_score = (
    (df["income"] > 40000).astype(int) +
    (df["credit_score"] > 650).astype(int) +
    (df["employment_years"] > 2).astype(int) -
    (df["loan_amount"] > 1000000).astype(int)
)
df["approved"] = (approval_score >= 2).astype(int)

X = df[["income", "credit_score", "loan_amount", "employment_years"]]
y = df["approved"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

grid_params = {
    "n_estimators": [100, 150, 200, 400],
    "max_depth": [5, 10, 15, 20, None],
    "min_samples_split": [2, 5, 10, 15]
}

model = RandomForestClassifier(random_state=42)

grid_search = GridSearchCV(
    estimator=model,
    param_grid=grid_params,
    n_jobs=-1,
    cv=5,
    verbose=1,
    scoring="accuracy"
)

ramdomized = RandomizedSearchCV(
    estimator=model,
    param_distributions=grid_params,
    n_iter=20,
    cv=5,
    verbose=1,
    n_jobs=-1,
    scoring="accuracy"
)

grid_search.fit(X_train, y_train)
ramdomized.fit(X_train, y_train)
print("Best estimator :", grid_search.best_estimator_)
print("Best Parameter :", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)
print("\n\n\n")

print("Best estimator :", ramdomized.best_estimator_)
print("Best Parameter :", ramdomized.best_params_)
print("Best Score:", ramdomized.best_score_)

print("\n\n\n")
best_model = grid_search.best_estimator_
next_best_model = ramdomized.best_estimator_

next_best_model.fit(X_train, y_train)
best_model.fit(X_train, y_train)


prediction = best_model.predict(X_test)
prediction_2 = next_best_model.predict(X_train)

print(f"the answers are : {y_test}\n\n")
print(f"the models predictions are : {prediction}\n\n")
print(
    f"the Grid's best models accuracy is : {accuracy_score(y_test, prediction)}")
print(best_model.score(X_test, y_test))
print(
    f"the ramdomized's best models accuracy is : {accuracy_score(y_test, prediction)}")
print(best_model.score(X_test, y_test))
