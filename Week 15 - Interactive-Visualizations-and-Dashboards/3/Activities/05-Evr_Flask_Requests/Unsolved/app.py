# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request)


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome!"


if __name__ == "__main__":
    app.run(debug=True)
