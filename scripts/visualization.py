import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("metrics_results.csv")

# Scatter plot: LOC vs Maintainability Index
sns.scatterplot(x=df["LOC"], y=df["Maintainability_Index"])
plt.title("LOC vs Maintainability Index")
plt.xlabel("Lines of Code (LOC)")
plt.ylabel("Maintainability Index")
plt.savefig("scatter_loc_mi.png")
plt.show()

# Box plot: Cyclomatic Complexity across LOC ranges
df["LOC_Range"] = pd.cut(df["LOC"], bins=[0, 200, 500, 1000, 2000], labels=["<200", "200-500", "500-1000", "1000+"])
sns.boxplot(x=df["LOC_Range"], y=df["Cyclomatic_Complexity"])
plt.title("Cyclomatic Complexity Across LOC Ranges")
plt.xlabel("LOC Range")
plt.ylabel("Cyclomatic Complexity")
plt.savefig("boxplot_cc.png")
plt.show()
