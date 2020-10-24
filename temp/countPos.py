import pandas as pd

df = pd.read_excel("WORLDCUP.xlsx")

#Tính tần số của Cột POS
ts = df["Pos"].value_counts()

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


# Tương quan giữa vị trí và ccao cân nặng(bmi)
# bmi = df["Weight"] / ((df["Height"] / 100) * (df["Height"] / 100))

# bmiTB = bmi.sum() / len(bmi)

temp = df.groupby("Pos")["Weight", "Height", "Age"].mean()

bmi = pd.DataFrame({"BMI": temp["Weight"] / ((temp["Height"] / 100) * (temp["Height"] / 100))})

tuoi = df.groupby("Pos")["Age"].sum() / df.groupby("Pos")["Age"].count()

pos = pd.DataFrame()

pos["Tần số"] = ts
pos["Tần số tích lũy"] = tstl
pos["Tần suất"] = tsuat
pos["Tần suất tích lũy"] = tsuatTL
pos["BMI trung bình"] = bmi
pos["Tuoi trung bình"] = tuoi

print("------Bảng tần số tần suất và chỉ số BMI------")
print(pos)



