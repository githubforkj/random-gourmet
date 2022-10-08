import sqlite3
from urllib import response
import requests
import json 

con = sqlite3.connect('test.db')
c = con.cursor()

# 任意のテーブルを削除する
c.execute("DROP TABLE large_area;")
# large_areaのテーブルを作成する
c.execute("CREATE TABLE large_area(code STRING, name STRING, ss_code STRING, ss_name STRING, ls_code STRING, ls_name STRING, api_version FLOAT)")

# 大エリアマスタAPIからデータを取得する
query = {
    'key':'2bc4f479e6c2392d',
    'format':'json'
    }
    # エリアマスタAPIのリクエストURL
url = 'http://webservice.recruit.co.jp/hotpepper/large_area/v1/'
# JSONを取得
responce = requests.get(url, query)
# JSONの読み込み
result = json.loads(responce.text)['results']

# APIからデータを取得し、テーブルに格納する
for i in range(47):
    sql = "INSERT INTO large_area VALUES(?,?,?,?,?,?,?)"
    c.execute(sql,[result["large_area"][i]["code"],result["large_area"][i]["name"],result["large_area"][i]["large_service_area"]["code"],result["large_area"][i]["large_service_area"]["name"],result["large_area"][i]["service_area"]["code"],result["large_area"][i]["service_area"]["name"],result["api_version"]])
con.commit()
con.close()



