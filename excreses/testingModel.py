from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score, accuracy_score, mean_absolute_error
from sklearn.datasets import load_breast_cancer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

df = load_breast_cancer(as_frame=True).frame
X, y = load_breast_cancer(return_X_y=True)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)


pipline = Pipeline([
    ('scale', StandardScaler()),
    ('model', LogisticRegression(random_state=42))
])

grid_params = {
    'model__C': [0.1, 5, 10, 100]
}
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
grid_search = GridSearchCV(
    pipline,
    param_grid=grid_params,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1,
    cv=skf
)

grid_search.fit(X_train, y_train)

print("the models best settings is :", grid_search.best_params_)
print("\n\nmodels best scores are(before testing) :", grid_search.best_score_)
prediction = grid_search.predict(X_test)
print(f"\n\n models best scores are after testing:",
      accuracy_score(y_test, prediction))
