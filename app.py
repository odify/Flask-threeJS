from flask import Flask, jsonify, render_template, request
from flask_cors import CORS








from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)



@app.route("/", methods=["GET", 'POST'])
def home():
    """
    Home page route
    """
    if request.method == 'POST':
        message = request.form['message']
        return jsonify(your_message=message)
    return render_template("index.html")

@app.route("/hello", methods=["GET"])
def hello():
    """
    Hello route
    """
    return 'hello'

@app.route('/message', methods=['POST'])
def message():
    """
    Message route
    """
    message = request.json.get("message")
    return jsonify(your_message=message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")