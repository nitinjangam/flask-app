from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello World'


if __name__ == "__main__":
    print("running application on port 1234")
    app.run(host="0.0.0.0", debug=True)