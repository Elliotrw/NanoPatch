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
        "nitrogen": [120, 118, 119, 121, 120, 122, 120],
        "phosphorus": [110, 112, 111, 113, 110, 112, 111],
        "potassium": [115, 116, 117, 115, 114, 116, 117]
    },
        "thmData": {
        "temperature": [18, 19, 20, 18, 17, 18, 19],
        "humidity": [50, 52, 53, 50, 49, 51, 52],
        "moisture": [40, 42, 45, 43, 41, 40, 44]
    }}
    return jsonify(past_values)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.template_folder,
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
