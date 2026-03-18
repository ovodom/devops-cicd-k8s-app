from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is version 2 of the app!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    