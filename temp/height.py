import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Chia 4 khoảng < 1.7, < 1.8, < 1.9, > 1.9

df = pd.read_excel("WORLDCUP.xlsx")

height = df["Height"]

n1 = [i / 100 for i in height if i <= 170]
n2 = [i / 100 for i in height if i > 170 and i <= 180]
n3 = [i / 100 for i in height if i > 180 and i <= 190]
n4 = [i / 100 for i in height if i > 190]

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

#Biểu đồ cột tần số 
plt.bar(["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4"], ts)
plt.xlabel('Chiều cao')
plt.ylabel('Số người')
plt.title('Biểu đồ thể hiện độ tương quan giữa nhóm chiều cao và số người')
plt.legend(title='Nhóm 1: <= 1.7m \nNhóm 2: > 1.7m - 1.8m \nNhóm 3: > 1.8m - 1.9m \nNhóm 4: > 1.9m')
plt.show()

#biểu đồ đường tần số tích luỹ
plt.plot(["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4"], tstl)
plt.xlabel('Chiều cao')
plt.ylabel('Số người')
plt.title('Biểu đồ thể hiện độ tương quan giữa tuần số tích lũy và nhóm chiều cao')
plt.legend(title='Nhóm 1: <= 1.7m \nNhóm 2: > 1.7m - 1.8m \nNhóm 3: > 1.8m - 1.9m \nNhóm 4: > 1.9m')
plt.show()

#biểu đồ tròn tuần suất
labels = ["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4"]
explode = (0, 0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
plt.pie(tsuat, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Biểu đồ thể hiện độ tương quan giữa tuần suất và nhóm chiều cao')
plt.axis('equal') 
plt.legend(['Nhóm 1: <= 1.7m','Nhóm 2: > 1.7m - 1.8m','Nhóm 3: > 1.8m - 1.9m','Nhóm 4: > 1.9m'],
bbox_to_anchor=(0.65, 0.5, 0.5, 0.5))
plt.show()