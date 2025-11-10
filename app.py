from flask import Flask
from helpers import restresponse

app = Flask(__name__)

@app.route("/hello")
def hello():
    return restresponse("Hello World")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
