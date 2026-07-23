import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 6, 7, 1, 5],
    "attendance_percent": [55, 60, 65, 78, 85, 90, 95, 98, 58, 68, 88, 92, 50, 80],
    "passed": [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1]
})

X = df[["study_hours", "attendance_percent"]]
y = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("আসল:", list(y_test))
print("Predicted:", list(predictions))
probabilities = model.predict_proba(X_test)
print(probabilities)

accuracy = accuracy_score(y_test, predictions)
print(accuracy)
cm = confusion_matrix(y_test, predictions)
print(cm)
print(classification_report(y_test, predictions))
print(df.corr())
