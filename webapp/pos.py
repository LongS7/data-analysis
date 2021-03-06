import pandas as pd
from matplotlib import pyplot as plt
import base64
from io import BytesIO
import numpy as np

df = pd.read_excel("https://firebasestorage.googleapis.com/v0/b/data-analysis-68b5a.appspot.com/o/WORLDCUP.xlsx?alt=media&token=64d3d72e-97a7-4fde-93f3-091d53788eeb")

def getFTable():
    result = pd.DataFrame()

    result["Tần số"] = df["Pos"].value_counts()
    result["Tần suất"] = round(result["Tần số"] / result["Tần số"].sum() * 100, 2)
    result["Tần suất tích lũy"] = round(result["Tần suất"].cumsum(), 2)

    return result

data = getFTable()

def convert_fig_to_html(fig):
    """ Convert Matplotlib figure 'fig' into a <img> tag for HTML use using base64 encoding. """
  
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    return '<img style=\'width: 80%\' src=\'data:image/png;base64,{}\'>'.format(encoded)

def plot():
    charts = []

    fig = plt.figure()
    width = 0.5
    plt.xlabel("Vị trí")
    plt.ylabel("Số lượng cầu thủ")
    plt.title("Biều đồ thể hiện số lượng cầu thủ theo từng vị trí")
    plt.bar(data.index.tolist(), data["Tần số"], width=width)

    charts.append(convert_fig_to_html(fig))
    

    # Tần suất
    fig = plt.figure()
    plt.pie(data["Tần suất"], labels=data.index.tolist(), autopct=my_autopct,shadow=True,startangle=90)
    plt.axis('equal')
    plt.title("Biểu đồ thể hiện tần suất cầu thủ theo từng vị trí")
    plt.legend(title="Danh sách vị trí",loc='best',bbox_to_anchor=(0.7, 0.5, 0.5, 0.5))

    charts.append(convert_fig_to_html(fig))

    # Tần suất tích lũy
    fig = plt.figure()
    plt.xlabel("Vị trí")
    plt.ylabel("Tần suất tích lũy")
    plt.title("Biểu đồ thể hiện tần suất tích lũy số lượng cầu thủ theo từng vị trí")
    plt.plot(data.index.tolist(), data["Tần suất tích lũy"])

    charts.append(convert_fig_to_html(fig))

    return charts

def my_autopct(pct):
    return ('%.2f%s' % (pct, '%') ) if pct > 10 else ''


def doTapTrung():
    s = ""
    for item in df["Age"].mode().tolist():
        s += str(item) + " "

    x = [df["Age"].min(), df["Age"].max(), round(df["Age"].mean(), 2), s, df["Age"].median(), df["Age"].quantile(0.25), df["Age"].quantile(0.5), df["Age"].quantile(0.75)]

    
    rs = pd.DataFrame(np.reshape(x, (1, 8)), columns=["Min", "Max", "Mean", "Mode", "Median", "Q1", "Q2", "Q3"])

    return rs

def doPhanTan():
    s = ""
    for item in df["Age"].mode().tolist():
        s += str(item) + " "

    x = [df["Age"].max() - df["Age"].min(), df["Age"].quantile(0.75) - df["Age"].quantile(0.25), round(df["Age"].var(), 2), round(df["Age"].std(), 2), round(df["Age"].std() / df["Age"].mean(), 2)]

    
    rs = pd.DataFrame(np.reshape(x, (1, 5)), columns=["|Max - Min|", "IQR", "Variance", "Standard deviation", "CV"])

    return rs