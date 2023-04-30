from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Package(db.Model):
    __tablename__ = "packages"

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(255), nullable=False)
    recipient = db.Column(db.String(255), nullable=False)
    origin = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    express = db.Column(db.Boolean, nullable=False)
