import flask
from product_data import *

app = flask.Flask(__name__)


@app.route("/")
def homepage():
    return flask.render_template("index.html")


@app.route("/products")
def all_products():
    return flask.render_template("products.html", products=retrieve_all_products())


@app.route("/products/<product_id>")
def requested_product(product_id):
    return flask.render_template("base.html", product_id=retrieve_requested_product(product_id))


@app.route("/cart")
def cart_display():
    return flask.render_template("")


if __name__ == '__main__':
    app.run()
