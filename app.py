from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="./dist/assets", template_folder="./dist")
CORS(app)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/values")
def values():
    values = [{"N": 10}, {"P": 11}, {"K": 12}, {"T": 5}, {"H": 6}, {"M": 7}]
    return jsonify(values)

@app.route("/past-values")
def pastValues():
    past_values = {"npkData": {
        "nitrogen": [10, 22, 15, 18, 25, 30, 35],
        "phosphorus": [5, 8, 10, 12, 20, 22, 25],
        "potassium": [8, 12, 13, 17, 23, 28, 33]
      },
      "thmData": {
        "temperature": [4, 15, 16, 18, 20, 10, 12],
        "humidity": [25, 12, 2, 22, 19, 16, 25],
        "moisture": [8, 12, 13, 33, 23, 28, 10]
      }}
    return jsonify(past_values)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.template_folder,
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
