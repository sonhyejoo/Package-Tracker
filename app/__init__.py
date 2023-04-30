from flask import Flask, redirect, render_template, url_for
from .shipping_form import ShippingForm
from .config import Config
from flask_migrate import Migrate
from .models import db, Package

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return "<h1>Package Tracker</h1>"


@app.route("/new_package", methods=["GET", "POST"])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        data = form.data
        print(data)
        new_package = Package(
            sender=data["sender"],
            recipient=data["recipient"],
            origin=data["origin"],
            destination=data["destination"],
            express=data["express"],
        )
        db.session.add(new_package)
        db.session.commit()
        return redirect("/")
    return render_template("shipping_request.html", form=form)
