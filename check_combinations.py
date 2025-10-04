import pandas as pd
from sklearn.linear_model import LinearRegression

# Multiple linear regression.  This lets you see which combination of events
# best predicts rating.
# This requires more data, so may not be suitable for what we have right now.

df = pd.read_csv("data.csv")
X = df.drop(columns=["filename", "rating"])   # all events
y = df["rating"]

model = LinearRegression().fit(X, y)
coefs = pd.Series(model.coef_, index=X.columns).sort_values(key=abs, ascending=False)

print(coefs)
