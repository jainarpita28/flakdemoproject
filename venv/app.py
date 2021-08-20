from flask import Flask

app = Flask(__name__)

@app.route('/h')
def helloWorld():
    return'<h1>Hello!</h1>'


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()