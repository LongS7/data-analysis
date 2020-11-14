import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import base64
from io import BytesIO
from scipy.stats import norm
import scipy

df = pd.read_excel("https://firebasestorage.googleapis.com/v0/b/data-analysis-68b5a.appspot.com/o/WORLDCUP.xlsx?alt=media&token=64d3d72e-97a7-4fde-93f3-091d53788eeb")

def getFTable():
    weight = df["Weight"]

    n1 = [i / 100 for i in weight if i <= 70]
    n2 = [i / 100 for i in weight if i > 70 and i <= 80]
    n3 = [i / 100 for i in weight if i > 80 and i <= 90]
    n4 = [i / 100 for i in weight if i > 90]

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
    plt.title("Tần số các nhóm cân nặng của cầu thủ trong World Cup")
    plt.xlabel("Nhóm cân nặng")
    plt.ylabel("Số lượng")

    charts.append(convert_fig_to_html(fig))
    

    # Tần suất
    fig = plt.figure()
    plt.pie(data["Tần suất"],labels=["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4"], autopct=my_autopct,shadow =True,startangle=100)
    plt.axis('equal')
    plt.legend(title="Danh sách nhóm cân nặng",loc='best',bbox_to_anchor=(1, 0.5, 0.5, 0.5))
    plt.title("Tần suất cân nặng của cầu thủ World Cup")

    charts.append(convert_fig_to_html(fig))

    # Tần suất tích lũy
    fig = plt.figure()
    plt.xlabel("Nhóm cân nặng")
    plt.ylabel("Tần suất tích lũy")
    plt.title("Biểu đồ thể hiện tần suất tích lũy nhóm cân nặng của cầu thủ")
    plt.plot(data.index.tolist(), data["Tần suất tích lũy"])

    charts.append(convert_fig_to_html(fig))

    return charts

def doTapTrung():
    s = ""
    for item in df["Weight"].mode().tolist():
        s += str(item) + " "

    x = [df["Weight"].min(), df["Weight"].max(), round(df["Weight"].mean(), 2), s, df["Weight"].median(), df["Weight"].quantile(0.25), df["Weight"].quantile(0.5), df["Weight"].quantile(0.75)]

    
    rs = pd.DataFrame(np.reshape(x, (1, 8)), columns=["Min", "Max", "Mean", "Mode", "Median", "Q1", "Q2", "Q3"])

    return rs

def doPhanTan():
    s = ""
    for item in df["Weight"].mode().tolist():
        s += str(item) + " "

    x = [df["Weight"].max() - df["Weight"].min(), df["Weight"].quantile(0.75) - df["Weight"].quantile(0.25), round(df["Weight"].var(), 2), round(df["Weight"].std(), 2), round(df["Weight"].std() / df["Weight"].mean(), 2)]

    
    rs = pd.DataFrame(np.reshape(x, (1, 5)), columns=["|Max - Min|", "IQR", "Variance", "Standard deviation", "CV"])

    return rs
    
def my_autopct(pct):
    return ('%.2f%s' % (pct, '%') ) if pct > 10 else ''

def boxplot():
    fig = plt.figure()
    plt.boxplot(df["Weight"])

    return convert_fig_to_html(fig)

def histogram():
    fig = plt.figure()

    plt.hist(df["Weight"], density=True)
    plt.title('Biểu đồ Histogram của cân nặng')

    mu = df["Weight"].mean()
    std = df["Weight"].std()
    x = np.sort(df["Weight"])
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=1, color="r")

    return convert_fig_to_html(fig)

def qq():
    fig = plt.figure()
    
    scipy.stats.probplot(df['Weight'], dist="norm", plot=plt)
    plt.xlabel('Normal')
    plt.ylabel('Weight')
    plt.title('QQ-Plot Weight')
    
    return convert_fig_to_html(fig)