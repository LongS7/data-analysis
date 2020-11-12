from flask import Flask, render_template, request
import mpld3, numpy as np
from matplotlib import pyplot as plt
from mpld3 import plugins
import pandas as pd
import pos

application = Flask(__name__)

import weight

@application.route("/", methods=["POST", "GET"])
def index():
    text = ""
    if request.method == "POST":
        text = request.form["text"]

    return render_template("index.html", text=text)

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

    return render_template("trinh-bay-du-lieu.html", listTitle=listTitle, listIndexs=listIndexs, listColumns=listColumns, listData=listData, listCharts=listCharts)

@application.route("/mo-ta-du-lieu")
def mo_ta_du_lieu():
    

    return render_template("mo-ta-du-lieu.html")

@application.route("/khao-sat-dang-phan-phoi")
def khao_sat_dang_phan_phoi():
    
    return render_template("khao-sat-dang-phan-phoi.html")


def toTableFormat(df):
    listData = []

    indexs = df.index.tolist()
    columns = df.columns

    for item in indexs:
        listData.append(list(df.loc[item]))
    return indexs, columns, listData
    

if __name__ == "__main__":
    application.run(debug=True)
