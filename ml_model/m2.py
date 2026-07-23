from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

linear_model = LinearRegression()
logistic_model = LogisticRegression()
random_forest_classifier = RandomForestClassifier(
    n_estimators=200, random_state=42)
random_forest_reg = RandomForestRegressor(n_estimators=2000, random_state=42)


df = load_diabetes(as_frame=True).frame
print(df.head(5))

X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_tain, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


linear_model.fit(X_train, y_tain)
logistic_model.fit(X_train, y_tain)
random_forest_classifier.fit(X_train, y_tain)
random_forest_reg.fit(X_train, y_tain)

linear_prediction = linear_model.predict(X_test)
logistic_prediction = logistic_model.predict(X_test)
random_forest_classifier_prediction = random_forest_classifier.predict(X_test)
random_forest_reg_prediction = random_forest_reg.predict(X_test)

print("the answers:", y_test)
print(
    f"\n linear models Prediction : {linear_prediction} \n\nwith the accuracy of   {r2_score(y_test, linear_prediction)}")
print(
    f"\n logistic models Prediction : {logistic_prediction} \n\nwith the accuracy of {accuracy_score(y_test, logistic_prediction)}")
print(
    f"\n ;random forest classifier models Prediction : {random_forest_classifier_prediction} \n\nwith the accuracy of {accuracy_score(y_test, random_forest_classifier_prediction)}")
print(
    f"\n ;ramdom forest reggresion models Prediction : {random_forest_reg_prediction} \n\nwith the accuracy of {r2_score(y_test, random_forest_reg_prediction)}")

importance = pd.Series(random_forest_reg.feature_importances_)
print(
    f"the import features for ramdom_forest_reg model is \n\n {importance.sort_values(ascending=False)}")
