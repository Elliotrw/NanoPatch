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

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.template_folder,
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
