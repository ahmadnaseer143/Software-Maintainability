import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load data
df = pd.read_csv("processed_data.csv")

# Correlation analysis
correlation_matrix = df.corr()
print("Correlation Matrix:\n", correlation_matrix)

# Regression analysis
X = df["LOC"]
Y = df["Maintainability_Index"]
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()

print("Regression Summary:\n", model.summary())

# Save correlation results
correlation_matrix.to_csv("correlation_results.csv")
print("Correlation analysis saved to correlation_results.csv.")
