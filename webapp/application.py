from flask import Flask, render_template, request
import mpld3, numpy as np
from matplotlib import pyplot as plt
from mpld3 import plugins
import pandas as pd
import pos, weight, height, age
import os

os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

application = Flask(__name__)

@application.route("/")
def index():

    return render_template("index.html")

@application.route("/hieu-du-lieu")
def hieu_du_lieu():
    return render_template("hieu-du-lieu.html")

@application.route("/tai-du-lieu")
def tai_du_lieu():    
    return render_template("tai-du-lieu.html")

@application.route("/thong-ke-du-lieu-thieu")
def thong_ke_du_lieu_thieu():

    conclude = "Không có cột dữ liệu nào bị thiếu!"

    return render_template("thong-ke-du-lieu-thieu.html", conclude=conclude)

@application.route("/xu-ly-du-lieu")
def xu_ly_du_lieu():
    df = pd.read_excel("https://firebasestorage.googleapis.com/v0/b/data-analysis-68b5a.appspot.com/o/WORLDCUP.xlsx?alt=media&token=64d3d72e-97a7-4fde-93f3-091d53788eeb")

    tableTitle = "10 dòng đầu của dữ liệu sau khi được xử lý"

    indexs, columns, data = toTableFormat(df.head(10))

    return render_template("xu-ly-du-lieu.html", tableTitle=tableTitle, indexs=indexs, columns=columns, data=data)

@application.route("/trinh-bay-du-lieu")
def trinh_bay_du_lieu():
    listData = []
    listIndexs = []
    listColumns = []
    listCharts = []
    listTitle = []

    # Cột Pos
    df = pos.getFTable()
    indexs, columns, data = toTableFormat(df)

    listTitle.append("Bảng tần số, tần suất, tần suất tích lũy")
    listIndexs.append(indexs)
    listColumns.append(columns)
    listData.append(data)
    listCharts.append(pos.plot())

    # Cột Height
    df = height.getFTable()
    indexs, columns, data = toTableFormat(df)

    listTitle.append("Bảng tần số, tần suất, tần suất tích lũy")
    listIndexs.append(indexs)
    listColumns.append(columns)
    listData.append(data)
    listCharts.append(height.plot())

    # Cột Weight
    df = weight.getFTable()
    indexs, columns, data = toTableFormat(df)

    listTitle.append("Bảng tần số, tần suất, tần suất tích lũy")
    listIndexs.append(indexs)
    listColumns.append(columns)
    listData.append(data)
    listCharts.append(weight.plot())

    # Cột Age
    df = age.getFTable()
    indexs, columns, data = toTableFormat(df)

    listTitle.append("Bảng tần số, tần suất, tần suất tích lũy")
    listIndexs.append(indexs)
    listColumns.append(columns)
    listData.append(data)
    listCharts.append(age.plot())

    return render_template("trinh-bay-du-lieu.html", listTitle=listTitle, listIndexs=listIndexs, listColumns=listColumns, listData=listData, listCharts=listCharts)

# @application.route("/mo-ta-du-lieu")
# def mo_ta_du_lieu():
#     hi1, hc1, h1 = toTableFormat(height.doTapTrung())
#     hi2, hc2, h2 = toTableFormat(height.doPhanTan())
#     charth = height.boxplot()
    
#     wi1, wc1, w1 = toTableFormat(weight.doTapTrung())
#     wi2, wc2, w2 = toTableFormat(weight.doPhanTan())
#     chartw = weight.boxplot()
    
#     ai1, ac1, a1 = toTableFormat(age.doTapTrung())
#     ai2, ac2, a2 = toTableFormat(age.doPhanTan())
#     charta = age.boxplot()
    
#     return render_template("mo-ta-du-lieu.html", hc1=hc1, h1=h1, hc2=hc2, h2=h2, charth=charth, wc1=wc1, w1=w1, wc2=wc2, w2=w2, chartw=chartw, ac1=ac1, a1=a1, ac2=ac2, a2=a2, charta=charta)

# @application.route("/khao-sat-dang-phan-phoi")
# def khao_sat_dang_phan_phoi():
#     hisH = height.histogram()
#     hisW = weight.histogram()
#     hisA = age.histogram()

#     df = pd.read_excel("https://firebasestorage.googleapis.com/v0/b/data-analysis-68b5a.appspot.com/o/WORLDCUP.xlsx?alt=media&token=64d3d72e-97a7-4fde-93f3-091d53788eeb")

#     qq1 = height.qq()
#     qq2 = weight.qq()
#     qq3 = age.qq()

#     ketLuan = "Dữ liệu tuân theo phân phối chuẩn"

#     cc_cn = df['Height'].corr(df['Weight'])

#     kl_cc_cn = "Tương quan giữa chiều cao và cân nặng là tương quan "

#     if cc_cn > 0:
#         kl_cc_cn += "thuận"
#     else:
#         kl_cc_cn += "nghịch"

#     return render_template("khao-sat-dang-phan-phoi.html", hisH=hisH, hisW=hisW, hisA=hisA, ketLuan=ketLuan, qq1=qq1, qq2=qq2, qq3=qq3, cc_cn=cc_cn, kl_cc_cn=kl_cc_cn)


def toTableFormat(df):
    listData = []

    indexs = df.index.tolist()
    columns = df.columns

    for item in indexs:
        listData.append(list(df.loc[item]))
    return indexs, columns, listData
    

if __name__ == "__main__":
    application.run(debug=True)
