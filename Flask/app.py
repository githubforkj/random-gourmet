from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
import api


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

        new_record = Attr(price=price, num=num, place=place, area_id = api1[place])

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
            code = codes.area_id
            api1 = api.middle_area_masta()
            api2 = api.gourmet_search(code)
            middle_area = ["銀座・有楽町・新橋・築地・月島",
                    "水道橋・飯田橋・神楽坂",
                    "お台場",
                    "東京・大手町・日本橋・人形町",
                    "四ツ谷・麹町・市ヶ谷・九段下",
                    "上野・御徒町・浅草",
                    "北千住・日暮里・葛飾・荒川",
                    "錦糸町・浅草橋・両国・亀戸",
                    "門前仲町・東陽町・木場・葛西",
                    "神田・神保町・秋葉原・御茶ノ水",
                    "品川･目黒･田町･浜松町･五反田",
                    "蒲田・大森・大田区",
                    "渋谷",
                    "原宿・青山・表参道",
                    "恵比寿・中目黒・代官山・広尾",
                    "赤坂・六本木・麻布十番・西麻布",
                    "自由が丘・田園調布",
                    "池袋",
                    "赤羽・王子・十条",
                    "新宿",
                    "新大久保・大久保",
                    "巣鴨・大塚・駒込",
                    "中野・高円寺・阿佐ヶ谷・方南町",
                    "下北沢・代々木上原",
                    "高田馬場",
                    "池尻大橋・三軒茶屋・駒沢大学",
                    "桜新町・用賀・二子玉川",
                    "祐天寺・学芸大学・都立大学",
                    "幡ヶ谷・笹塚・明大前・下高井戸",
                    "調布・府中・千歳烏山・仙川",
                    "経堂・千歳船橋",
                    "祖師ヶ谷大蔵・成城学園前",
                    "大井町･中延･旗の台･戸越･馬込",
                    "不動前・武蔵小山",
                    "雪が谷大塚・池上",
                    "武蔵小金井",
                    "国立・国分寺",
                    "青梅・昭島・小作・青梅線沿線",
                    "多摩センター・南大沢",
                    "吉祥寺・荻窪・三鷹",
                    "町田",
                    "八王子・立川",
                    "西武池袋線（石神井公園～秋津）",
                    "西武新宿線(中井～田無～東村山)",
                    "練馬・板橋・成増・江古田",
                    "都営三田線（新板橋～西高島平）",
                    "聖蹟桜ヶ丘・高幡不動・分倍河原",
                    "東京都その他"]
            return render_template('index.html', records=records, api1=api1, api2 = api2, middle_area = middle_area)
        else:
            middle_area = ["銀座・有楽町・新橋・築地・月島",
                    "水道橋・飯田橋・神楽坂",
                    "お台場",
                    "東京・大手町・日本橋・人形町",
                    "四ツ谷・麹町・市ヶ谷・九段下",
                    "上野・御徒町・浅草",
                    "北千住・日暮里・葛飾・荒川",
                    "錦糸町・浅草橋・両国・亀戸",
                    "門前仲町・東陽町・木場・葛西",
                    "神田・神保町・秋葉原・御茶ノ水",
                    "品川･目黒･田町･浜松町･五反田",
                    "蒲田・大森・大田区",
                    "渋谷",
                    "原宿・青山・表参道",
                    "恵比寿・中目黒・代官山・広尾",
                    "赤坂・六本木・麻布十番・西麻布",
                    "自由が丘・田園調布",
                    "池袋",
                    "赤羽・王子・十条",
                    "新宿",
                    "新大久保・大久保",
                    "巣鴨・大塚・駒込",
                    "中野・高円寺・阿佐ヶ谷・方南町",
                    "下北沢・代々木上原",
                    "高田馬場",
                    "池尻大橋・三軒茶屋・駒沢大学",
                    "桜新町・用賀・二子玉川",
                    "祐天寺・学芸大学・都立大学",
                    "幡ヶ谷・笹塚・明大前・下高井戸",
                    "調布・府中・千歳烏山・仙川",
                    "経堂・千歳船橋",
                    "祖師ヶ谷大蔵・成城学園前",
                    "大井町･中延･旗の台･戸越･馬込",
                    "不動前・武蔵小山",
                    "雪が谷大塚・池上",
                    "武蔵小金井",
                    "国立・国分寺",
                    "青梅・昭島・小作・青梅線沿線",
                    "多摩センター・南大沢",
                    "吉祥寺・荻窪・三鷹",
                    "町田",
                    "八王子・立川",
                    "西武池袋線（石神井公園～秋津）",
                    "西武新宿線(中井～田無～東村山)",
                    "練馬・板橋・成増・江古田",
                    "都営三田線（新板橋～西高島平）",
                    "聖蹟桜ヶ丘・高幡不動・分倍河原",
                    "東京都その他"]
            return render_template('index.html', middle_area=middle_area)


def roulette(num):
    num = random.randrange(100)
    return num


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
