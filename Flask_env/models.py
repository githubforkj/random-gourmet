from datetime import date
from multiprocessing.heap import Arena
from turtle import title
import app
from datetime import datetime

class Task(app.db.Model):
    id = app.db.Column(app.db.Integer(), primary_key=True)
    price = app.db.Column(app.db.String(100))
    people = app.db.Column(app.db.String(100))
    area = app.db.Column(app.db.String(100))
    area_code = app.db.Column(app.db.String(100))
    date = app.db.Column(app.db.DateTime(), default=datetime.now())
    judge = app.db.Column(app.db.Boolean(), default=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self):
        return f'<Task id: {self.id}・{self.price}'