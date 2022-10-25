from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Not Today Satan"

app.run(host="0.0.0.0", port=80)

