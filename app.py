from flask import Flask, render_template

app = Flask(__name__)

list = ["lol", "arup", 'a']


@app.route("/")
def hello_world():
    return render_template("index.html", data=list)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

list = ["lol", "arup", 'a']


@app.route("/")
def hello_world():
    return render_template("index.html", data=list)


if __name__ == "__main__":
    app.run(debug=True)
