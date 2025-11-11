from flask import Flask
from helpers import rest_response

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/hello")
def hello():
    return rest_response("Hello World")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
