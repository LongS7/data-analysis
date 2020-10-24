import pandas as pd

df = pd.read_excel("WORLDCUP.xlsx")

#Tính tần số của Cột POS
ts = df["Club"].value_counts()

#Tần số tích lũy của Pos
tstl = ts.cumsum()

#Tần suất của Pos
tsuat = ts / ts.sum() * 100

#Tần suất tích lũy của Pos
tsuatTL = tsuat.cumsum()


result = pd.DataFrame()

result["Tần số"] = ts
result["Tần số tích lũy"] = tstl
result["Tần suất"] = tsuat
result["Tần suất tích lũy"] = tsuatTL

print(result)