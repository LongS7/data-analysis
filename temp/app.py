import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

f= pd.read_excel("WCTEAMS.xlsx")
# print(f.head(10))
keep_col = ['Team','Pos','Birth Date','Club','Height','Weight']
new_f = f[keep_col]

age = [2018 - int(item[6:]) for item in new_f["Birth Date"]]
year = [int(item[6:]) for item in new_f["Birth Date"]]

new_f["Birth Date"] = year
new_f["Age"] = age

# print(new_f)

# new_f.to_excel("WORLDCUP.xlsx", index=False)

age = sorted(age)

plt.plot(age)
plt.show()