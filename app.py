from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS

from db_sqlite import read_latest_entry_as_json

app = Flask(__name__, static_folder="./dist/assets", template_folder="./dist")
CORS(app)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/values")
def values():
    return read_latest_entry_as_json()


@app.route("/past-values")
def pastValues():
    past_values = {"npkData": {
        "nitrogen": [40, 60, 55, 80, 48, 18, 43],
        "phosphorus": [36, 20, 8, 42, 87, 77, 111],
        "potassium": [90, 100, 160, 183, 200, 120, 99]
    },
        "thmData": {
        "temperature": [18, 19, 20, 24, 28, 15, 19],
        "humidity": [50, 52, 53, 50, 46, 51, 54],
        "moisture": [55, 50, 44, 52, 57, 55, 49]
    }}
    return jsonify(past_values)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.template_folder,
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
