import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel("WORLDCUP.xlsx")

print(df.describe()["Age"])

plt.boxplot(df["Age"])
plt.show()
