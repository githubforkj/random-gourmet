from ast import get_source_segment
from urllib import response
import requests
import json 

# 中エリアを取得する
def middle_area_masta():
    # エリアマスタAPI用のクエリ
    query = {
    'key':'2bc4f479e6c2392d',
    'keyword':'',
    'large_area':'Z011', #　大エリアコードで東京を指定
    'format':'json'
    }
    # エリアマスタAPIのリクエストURL
    url = 'http://webservice.recruit.co.jp/hotpepper/middle_area/v1/'
    # JSONを取得
    responce = requests.get(url, query)
    # JSONの読み込み
    result = json.loads(responce.text)['results']['middle_area']

    middle_area = {}
    # 中エリアのコードと名称を取得
    for (u,v) in enumerate(result):
        # print(v['code'],'-',v['name'])
        # print('"{}"'.format(v['name']),',')
        # print('--------------------------------------------')
        middle_area[v['name']] = v['code']
    
    return middle_area

# 店舗情報等を取得する
# 場所のみ絞り込みが出来ている。後は価格帯を整形する。
def gourmet_search(code):
    # グルメサーチAPI用のクエリ
    query = {
    'key': '2bc4f479e6c2392d',
    # 'lat': '35.75012327488292', # 北千住駅の緯度
    # 'lng': '139.80508505043517', # 北千住駅の経度
    'middle_area': code, # 中エリアのコードを入力する
    'range': '3',
    'count': 100,
    'format': 'json'
        }
    #  グルメサーチAPIのリクエストURL
    url = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

    # APIを使用し、JSONを取得
    responce = requests.get(url, query)

    # JSONを読み込む
    result = json.loads(responce.text)['results']['shop']

    gourment = []

    # 店名、予算、中エリア、店舗URL、画像、営業時間の取得
    for (u,v) in enumerate(result):
        g = []
        # 店idと店名
        g.append(v['id'])
        g.append(v['name'])
        
        # 予算とコード
        g.append(v['budget']['name'])
        g.append(v['budget']['code'])

        # 中エリアとコード
        g.append(v['middle_area']['name'])
        g.append(v['middle_area']['code'])

        # 店舗URL
        g.append(v['urls']['pc'])

        # 画像
        g.append(v['photo']['pc']['l'])
        g.append(v['photo']['mobile']['l'])

        # 営業時間
        g.append(v['open'])

        gourment.append(g)

    print('gourment')
    return gourment
    
    


middle_area_masta()
# gourmet_search()