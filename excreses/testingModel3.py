from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
from sklearn.datasets import fetch_openml
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer


titanic = fetch_openml("titanic", version=1,
                       as_frame=True, parser="auto").frame


X = titanic[['age', 'fare', 'sex', 'embarked']]
y = titanic['survived']
print(X.head(5))
print(y.head(5))
num_features = ['age', 'fare']
cat_features = ['sex', 'embarked']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scales', StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encode', OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipeline, num_features),
    ('cat', cat_pipeline, cat_features)
])

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestClassifier(random_state=42))
])

grid = {
    'model__n_estimators': [100, 200, 300, 400],
    "model__max_depth": [5, 10, 15, 20]
}
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
search_grid = GridSearchCV(
    estimator=pipeline,
    n_jobs=-1,
    param_grid=grid,
    cv=skf,
    scoring='accuracy',
    verbose=1
)

search_grid.fit(X_train, y_train)

print("the models best params are :", search_grid.best_params_)
print("\n\n the models best accuracy is(before testing) :",
      search_grid.best_score_)

prediction = search_grid.predict(X_test)
print("the accuracy after the test = :", accuracy_score(y_test, prediction))
