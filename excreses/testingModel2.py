from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
from sklearn.datasets import fetch_california_housing
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer


X, y = fetch_california_housing(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)
grid_params = {
    'model__n_estimators': [100, 150, 200, 300],
    'model__max_depth': [5, 10, 15, 20]
}

pipline = Pipeline([
    ('scales', StandardScaler()),
    ("model", RandomForestRegressor(random_state=42))
])

ramdomized_search = RandomizedSearchCV(
    pipline,
    param_distributions=grid_params,
    n_iter=10,
    n_jobs=-1,
    cv=5,
    verbose=1,
    scoring="r2"
)

ramdomized_search.fit(X_train, y_train)

print("the models best params are :", ramdomized_search.best_params_)
print("\n\n the models best accuracy is(before testing) :",
      ramdomized_search.best_score_)

prediction = ramdomized_search.predict(X_test)
print("the accuracy after the test = :", r2_score(y_test, prediction))
