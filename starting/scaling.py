import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


np.random.seed(7)
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

scaling = StandardScaler()
scaled_df = scaling.fit_transform(df)
print(scaled_df)
