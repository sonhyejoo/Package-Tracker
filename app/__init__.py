from flask import Flask, redirect, render_template, url_for
from .shipping_form import ShippingForm
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    return "<h1>Package Tracker</h1>"


@app.route("/new_package", methods=["GET", "POST"])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        return redirect(url_for(".index"))
    return render_template("shipping_request.html", form=form)
