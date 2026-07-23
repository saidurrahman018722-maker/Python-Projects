from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "income": [30000, 55000, 42000, 80000, 25000, 60000, 48000, 90000, 35000, 70000],
    "credit_score": [620, 720, 650, 780, 580, 700, 640, 800, 610, 750],
    "approved": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

X = df[['income', 'credit_score']]
y = df['approved']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42)

model = DecisionTreeClassifier(max_depth=4, random_state=42)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("the answers:", list(y_test))
print("the model's prediction:", list(prediction))

print("the model's accuricy:", accuracy_score(y_test, prediction))
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=["income", "credit_score"],
          class_names=["Reject", "Approve"], filled=True, rounded=True)
# plt.show()
importances = model.feature_importances_
print(importances)
print(df.corr())
