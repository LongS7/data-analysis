import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import base64
from io import BytesIO
from scipy.stats import norm
import scipy

df = pd.read_excel("https://firebasestorage.googleapis.com/v0/b/data-analysis-68b5a.appspot.com/o/WORLDCUP.xlsx?alt=media&token=64d3d72e-97a7-4fde-93f3-091d53788eeb")

def getFTable():
    age = df["Age"]

    n1 = [i  for i in age if i <= 25]
    n2 = [i  for i in age if i > 25 and i <= 31]
    n3 = [i  for i in age if i > 31 and i <= 38]
    n4 = [i  for i in age if i > 38]

    ts = pd.Series([len(n1), len(n2), len(n3), len(n4)])

    tsuat = ts / ts.sum() * 100

    tsuatTL = tsuat.cumsum()

    result = pd.DataFrame([np.array(ts), np.array(tsuat), np.array(tsuatTL)], columns=["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4"], index=["Tần số", "Tần suất", "Tần suất tích lũy"]).T

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
    plt.bar(["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4"], data["Tần số"], width=width)
    plt.title("Tần số các nhóm độ tuổi của cầu thủ trong World Cup")
    plt.xlabel("Nhóm độ tuổi")
    plt.ylabel("Số lượng")

    charts.append(convert_fig_to_html(fig))
    

    # Tần suất
    fig = plt.figure()
    plt.pie(data["Tần suất"],labels=["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4"], autopct=my_autopct,shadow =True,startangle=100)
    plt.axis('equal')
    plt.legend(title="Danh sách vị trí",loc='best',bbox_to_anchor=(1, 0.5, 0.5, 0.5))
    plt.title("Tần suất độ tuổi của cầu thủ World Cup")

    charts.append(convert_fig_to_html(fig))

    # Tần suất tích lũy
    fig = plt.figure()
    plt.xlabel("Vị trí")
    plt.ylabel("Tần suất tích lũy")
    plt.title("Biểu đồ thể hiện tần suất tích lũy nhóm độ tuổi của cầu thủ")
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

def boxplot():
    fig = plt.figure()
    plt.boxplot(df["Age"])

    return convert_fig_to_html(fig)

def histogram():
    fig = plt.figure()

    plt.hist(df["Age"], density=True)
    plt.title('Biểu đồ Histogram của độ tuổi')

    mu = df["Age"].mean()
    std = df["Age"].std()
    x = np.sort(df["Age"])
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=1, color="r")

    return convert_fig_to_html(fig)

def qq():
    fig = plt.figure()
    
    scipy.stats.probplot(df['Age'], dist="norm", plot=plt)
    plt.xlabel('Normal')
    plt.ylabel('Age')
    plt.title('QQ-Plot Age')

    return convert_fig_to_html(fig)