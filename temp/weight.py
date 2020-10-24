import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Chia 4 khoảng < 1.7, < 1.8, < 1.9, > 1.9

df = pd.read_excel("WORLDCUP.xlsx")

height = df["Weight"]

n1 = [i / 100 for i in height if i <= 70]
n2 = [i / 100 for i in height if i > 70 and i <= 80]
n3 = [i / 100 for i in height if i > 80 and i <= 90]
n4 = [i / 100 for i in height if i > 90]

#Tính tần số của
ts = pd.Series([len(n1), len(n2), len(n3), len(n4)])

#Tần số tích lũy của Pos
tstl = ts.cumsum()

#Tần suất của Pos
tsuat = ts / ts.sum() * 100

#Tần suất tích lũy của Pos
tsuatTL = tsuat.cumsum()

result = pd.DataFrame([np.array(ts), np.array(tstl), np.array(tsuat), np.array(tsuatTL)], columns=["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4"], index=["Tần số", "Tần số tích lũy", "Tần suất", "Tần suất tích lũy"]).T

print(result)


plt.bar(["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4"], ts)
plt.show()