from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class ShippingForm(FlaskForm):
    sender = StringField("sender", validators=[DataRequired()])
    recipient = StringField("recipient", validators=[DataRequired()])
    origin = SelectField("origin", validators=[DataRequired()])
    destination = SelectField("destination", validators=[DataRequired()])
    express = BooleanField("express")
    submit = SubmitField("Submit")
