from flask import Flask, render_template

app = Flask(__name__)

list = ["lol", "arup", 'a']


@app.route("/")
def index():
    return render_template("index.html", data=list)

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/product")
def product():
    return render_template("product.html")


if __name__ == "__main__":
    app.run(debug=True)

