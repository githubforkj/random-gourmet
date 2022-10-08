import sqlite3
from urllib import response
import requests
import json 

# Tuple  Convert to String　function
def CT(tup):
    str = "".join(tup)
    return str

# sqliteに接続する
con = sqlite3.connect('test.db')
c = con.cursor()

# 任意のテーブルを削除する
c.execute("DROP TABLE middle_area;")


# middle_areaのテーブルを作成する
c.execute("CREATE TABLE middle_area(code STRING, name STRING, l_code STRING, l_name STRING, ss_code STRING, ss_name STRING, lss_code STRING, lss_name STRING, api_version FLOAT)")

# large_areaテーブルから大エリアコードを取得する
la = c.execute("SELECT code FROM large_area;")
la = c.fetchall()


# 中エリアテーブルにAPIからデータを取得し、格納する
for j in range(len(la)):
    # 中エリアマスタAPIからデータを取得する
    query = {
        'key':'2bc4f479e6c2392d',
        'large_area':CT(la[j]),  # 大エリアを入力する
        'format':'json'
        }
        # エリアマスタAPIのリクエストURL
    url = 'http://webservice.recruit.co.jp/hotpepper/middle_area/v1/'
    # JSONを取得
    responce = requests.get(url, query)
    # JSONの読み込み
    result = json.loads(responce.text)['results']

    # APIからデータを取得し、テーブルに格納する
    for i in range(len(result["middle_area"])):
        sql = "INSERT INTO middle_area VALUES(?,?,?,?,?,?,?,?,?)"
        c.execute(sql,[result["middle_area"][i]["code"],result["middle_area"][i]["name"],result["middle_area"][i]["large_area"]["code"],result["middle_area"][i]["large_area"]["name"],result["middle_area"][i]["service_area"]["code"],result["middle_area"][i]["service_area"]["name"],result["middle_area"][i]["large_service_area"]["code"],result["middle_area"][i]["large_service_area"]["name"],result["api_version"]])
    con.commit()
con.close()



