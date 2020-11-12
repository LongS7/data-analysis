import pandas as pd
from matplotlib import pyplot as plt
from mpld3 import plugins
import mpld3

df = pd.read_excel("https://firebasestorage.googleapis.com/v0/b/data-analysis-68b5a.appspot.com/o/WORLDCUP.xlsx?alt=media&token=64d3d72e-97a7-4fde-93f3-091d53788eeb")

def getFTable():
    result = pd.DataFrame()

    result["Tần số"] = df["Pos"].value_counts()
    result["Tần suất"] = round(result["Tần số"] / result["Tần số"].sum() * 100, 2)
    result["Tần suất tích lũy"] = round(result["Tần suất"].cumsum(), 2)

    return result

data = getFTable()

def plot():
    charts = []
    title = []

    fig = plt.figure()
    width = 0.5
    plt.bar(data.index.tolist(), data["Tần số"], width=width)
    plt.xlabel("Vị trí")
    plt.ylabel("Số lượng cầu thủ")
    plt.title("Biều đồ thể hiện số lượng cầu thủ theo từng vị trí")

    charts.append(mpld3.fig_to_html(fig))

    # Tần suất
    fig = plt.figure()
    plt.pie(data["Tần suất"], labels=data.index.tolist(), autopct=my_autopct,shadow=True,startangle=90)
    plt.axis('equal')
    plt.legend(title="Danh sách vị trí",loc='best',bbox_to_anchor=(0.7, 0.5, 0.5, 0.5))

    charts.append(mpld3.fig_to_html(fig))

    # Tần suất tích lũy
    fig = plt.figure()
    plt.xlabel("Vị trí")
    plt.ylabel("Tần suất tích lũy")
    plt.title("Biểu đồ thể hiện tần suất tích lũy số lượng cầu thủ theo từng vị trí")
    plt.plot(data.index.tolist(), data["Tần suất tích lũy"])

    charts.append(mpld3.fig_to_html(fig))

    return charts

def my_autopct(pct):
    return ('%.2f%s' % (pct, '%') ) if pct > 10 else ''