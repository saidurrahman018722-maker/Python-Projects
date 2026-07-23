import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


df = pd.DataFrame({
    "income": [30000, 55000, 42000, 80000, 25000, 60000, 48000, 90000, 35000, 70000,
               33000, 65000, 45000, 85000, 28000, 62000, 50000, 95000, 38000, 72000],
    "credit_score": [620, 720, 650, 780, 580, 700, 640, 800, 610, 750,
                     615, 710, 655, 790, 590, 705, 645, 810, 605, 745],
    "approved": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

X = df[['income', 'credit_score']]
y = df['approved']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

single_tree = DecisionTreeClassifier(max_depth=3, random_state=42)

single_tree.fit(X_train, y_train)

single_tree_prediction = single_tree.predict(X_test)

forset = RandomForestClassifier(n_estimators=2000, random_state=42)
forset.fit(X_train, y_train)
forest_prediction = forset.predict(X_test)


print(f"the actual answers are :", list(y_test))
print(
    f"\n the single_dicision_tree answers:{single_tree_prediction} with the accuracy of:= {accuracy_score(y_test, single_tree_prediction)}")
print(
    f"\n the the random foreset  answers:{forest_prediction} with the accuracy of:= {accuracy_score(y_test, forest_prediction)}")

importance = pd.Series(single_tree.feature_importances_, index=X.columns)
print(importance)

importance_forest = pd.Series(forset.feature_importances_, index=X.columns)
print(importance_forest)
