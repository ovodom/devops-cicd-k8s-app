from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🔥 AUTO DEPLOY WORKING - Version 3 again! sweeeeeet!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    