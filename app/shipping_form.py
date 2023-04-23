from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from app.maps import maps

cities = list(maps.keys())


class ShippingForm(FlaskForm):
    sender = StringField("sender", validators=[DataRequired()])
    recipient = StringField("recipient", validators=[DataRequired()])
    origin = SelectField("origin", choices=cities, validators=[DataRequired()])
    destination = SelectField(
        "destination", choices=cities, validators=[DataRequired()]
    )
    express = BooleanField("express", validators=[DataRequired()])
    submit = SubmitField("Submit")
