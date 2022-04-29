from ast import Num
from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    description=db.Column(db.String)
    num_moon=db.Column(db.Integer)
    color=db.Column(db.String)


    