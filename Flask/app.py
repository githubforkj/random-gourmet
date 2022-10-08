from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
import api
import data


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


# DBの設定
class Attr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, default=0)
    num = db.Column(db.Integer, default=0)
    place = db.Column(db.String(30), default=0)
    area_id = db.Column(db.String(30), default=0)
    budget_id = db.Column(db.String(30), default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<record %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        price = request.form.get('price')
        num = request.form.get('num')
        place = request.form.get('place')
        api1 = api.middle_area_masta()
        api2 = api.budget_masta()

        new_record = Attr(price=price, num=num, place=place, area_id = api1[place], budget_id = api2[price])

        try:
            db.session.add(new_record)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your record'

    else:
        records = Attr.query.order_by(Attr.date_created).all()
        codes = Attr.query.order_by(Attr.id.desc()).first()
        if codes != None:
            area_code = codes.area_id
            budget_code = codes.budget_id
            middle_area = data.middle_area_list()
            budget = data.budget_list()
            api1 = api.middle_area_masta()
            api2 = api.budget_masta()
            api3 = api.gourmet_search(area_code,budget_code)
            
            return render_template('index.html', records=records, api1=api1, api2=api2, api3=api3, middle_area = middle_area, budget = budget)
        else:
            middle_area = data.middle_area_list()
            budget = data.budget_list()
            return render_template('index.html', middle_area=middle_area, budget = budget)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Attr.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')

    except:
        return ('There was a problem deleting that task')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Attr.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)


if __name__ == '__main__':
    app.run(debug=True)
