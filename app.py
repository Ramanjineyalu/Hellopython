from flask import Flask

app = Flask(__name__)

def print():
    return "Python"

@app.route("/")
def start():
    return "Hello %s" % print()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8070)