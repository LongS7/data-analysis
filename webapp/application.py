from flask import Flask, render_template, request
import mpld3, numpy as np
from matplotlib import pyplot as plt
from mpld3 import plugins

application = Flask(__name__)


@application.route("/", methods=["POST", "GET"])
def index():
    text = ""
    if request.method == "POST":
        text = request.form["text"]

    return render_template("index.html", text=text)

@application.route("/linechart")
def linechart():
    data = 15 * np.random.random_sample(10)

    fig, ax = plt.subplots()
    ax.plot(data)
    ax.set_title("Line chart")
    ax.set_xlabel("x value")
    ax.set_ylabel("y value")

    chart_html = mpld3.fig_to_html(fig)

    return render_template("linechart.html", chart=chart_html)

@application.route("/barchart")
def barchart():
    fig, ax = plt.subplots()

    divisions = ["Div A", "Div B", "Div C", "Div D", "Div E"]
    division_average_marks = np.random.randint(5, 25, size=5)
    boys_average_marks = np.random.randint(5, 25, size=5)

    index = np.arange(len(divisions))
    width = 0.3

    ax.set_title("Bar chart")
    ax.bar(index, division_average_marks, width, color="green", label="Division Mark")
    ax.bar(index + width, boys_average_marks, width, color="blue", label="Boy Mark")
    ax.set_xticks(index + width/2, divisions)
    ax.legend(loc="best")

    chart_html = mpld3.fig_to_html(fig)

    return render_template("barchart.html", chart=chart_html)

@application.route("/piechart")
def piechart():
    data = 15 * np.random.random_sample(5)
    names = ["Product A", "Product B", "Product C", "Product D", "Product E"]

    explode = np.zeros(len(data))

    for i in range(len(data)):
        if data[i] == max(data):
            explode[i] = 0.1

    fig, ax = plt.subplots()
    ax.pie(data,explode=explode, labels=names)
    ax.set_title("Pie chart")

    chart_html = mpld3.fig_to_html(fig)

    return render_template("piechart.html", chart=chart_html)

@application.route("/scatterchart")
def scatterchart():
    data = 15 * np.random.random_sample(15)
    labels = [i for i in range(len(data))]
    fig, ax = plt.subplots()
    ax.scatter(x=labels, y=data, color="green")
    ax.set_title("Scatter chart")

    chart_html = mpld3.fig_to_html(fig)

    return render_template("scatterchart.html", chart=chart_html)

if __name__ == "__main__":
    application.run(debug=True)
