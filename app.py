from flask import Flask, render_template
from api import db, itemdata
app = Flask(__name__)




@app.route("/")
def index():
    datas = db()
    return render_template("index.html", data = datas)

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/product/<index>")
def product(index):
    idata = itemdata(int(index))
    return render_template("product.html", item = idata)

@app.route("/admin")
def adm():
   

    return render_template("admin.html")
if __name__ == "__main__":
    app.run(debug=True)

