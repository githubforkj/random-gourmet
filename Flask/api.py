import requests
import json 


# 検索クエリ

query = {
    'key': '＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊',
    'lat': '35.75012327488292', # 北千住駅の緯度
    'lng': '139.80508505043517', # 北千住駅の経度
    'range': '1',
    'count': 50,
    'format': 'json'
}


# グルメサーチAPIのリクエストURL
url1 = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

# URLとクエリでリクエスト
responce = requests.get(url1, query)

# 戻り値をjson形式で読み出し、['results']['shop']を抽出
result = json.loads(responce.text)['results']['shop']

# 'non_smoking'フィールドが'全面禁煙'以外の場合
# 店名、'non_smoking'フィールド、ジャンルを表示
for i in result:
    print(i)
    print('----------------------------------------------------------')
    # if i['non_smoking'] !='全面禁煙':
    #     print(
    #         i['name'], '■',
    #         i['non_smoking'],'■',
    #         i['genre']['name']
    #     )


# エリアマスタAPIのリクエストURL
url2 = http://webservice.recruit.co.jp/hotpepper/middle_area/v1/

query = {
    # ＊＊＊＊
}
