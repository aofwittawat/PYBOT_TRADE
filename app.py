from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/SIGNALS", methods =['POST'])
def SIGNALS_RECEIVER():
    if request.method == "POST":
        msg = request.data.decode("utf-8")
        print(msg)
        json_msg = json.loads(msg)
        print(json_msg)
    return "200"

if __name__ == "__main__":
    app.run(debug=True, port=8080)