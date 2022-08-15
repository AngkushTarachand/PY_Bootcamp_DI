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
    return flask.render_template("product.html", product_id=retrieve_requested_product(product_id))


@app.route("/cart")
def cart_display():
    return flask.render_template("cart.html", product=requested_product)


cart_items = []


@app.route("/add_product_to_cart/<product_id>")
def cart_items(cart_item):
    cart_items.append(cart_item)
    return cart_items


@app.route("/sign_up")
def sign_up_sign_in():
    if check_user() == "homepage":
        return flask.render_template("products.html", sign_up=check_user)
    else:
        return flask.render_template_string("sign_in.html")


@app.route("/delete_product_from_cart/<product_id>")
def cart_items(cart_item):
    cart_items.pop(cart_item)
    return cart_items


if __name__ == '__main__':
    app.run()
