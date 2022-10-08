from ast import get_source_segment
from cgitb import small
from urllib import response
import requests
import json 



# 大エリアを取得する
def large_area_masta():
    # エリアマスタAPI用のクエリ
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

    large_area = {}
    # 小エリアのコードと名称を取得
    print(type(result))
    print(result["large_area"])
    print(result["large_area"][0])
    print('----------------------------------------')
    for i in range(47):
        print(result["large_area"][i]["code"])
        print(result["large_area"][i]["name"])
        print(result["large_area"][i]["large_service_area"]["code"])
        print(result["large_area"][i]["large_service_area"]["name"])
        print(result["large_area"][i]["service_area"]["code"])
        print(result["large_area"][i]["service_area"]["name"])
        print(result["api_version"])
        print('----------------------------------------')
    
    # for i in result:
    #     # print(result[i])
    #     # print(i['large_area']['name'])
    #     # print(i['large_area']['service_area']['code'])
    #     # print(i['large_area']['service_area']['name'])
    #     # print(i['large_area']['large_service_area']['code'])
    #     # print(i['large_area']['large_service_area']['name'])
    #     print('------------------------------')
        
        
    
    
    return large_area

# 中エリアを取得する
def middle_area_masta():
    # エリアマスタAPI用のクエリ
    query = {
    'key':'2bc4f479e6c2392d',
    'large_area':'Z026', #　大エリアコードで東京を指定
    'format':'json'
    }
    # エリアマスタAPIのリクエストURL
    url = 'http://webservice.recruit.co.jp/hotpepper/middle_area/v1/'
    # JSONを取得
    responce = requests.get(url, query)
    # JSONの読み込み
    result = json.loads(responce.text)['results']

    middle_area = {}
    # 中エリアのコードと名称を取得
    print(result)
    print(len(result))
    print(len(result["middle_area"]))
    for i in range(len(result["middle_area"])):
        print(result["middle_area"][i]["code"])
        print(result["middle_area"][i]["name"])
        print(result["middle_area"][i]["large_area"]["code"])
        print(result["middle_area"][i]["large_area"]["name"])
        print(result["middle_area"][i]["service_area"]["code"])
        print(result["middle_area"][i]["service_area"]["name"])
        print(result["middle_area"][i]["large_service_area"]["code"])
        print(result["middle_area"][i]["large_service_area"]["name"])
        print(result["api_version"])
        print("--------------------------------------------------")

    
    return middle_area


# 小エリアを取得する
def small_area_masta(middle_area_code):
    # エリアマスタAPI用のクエリ
    query = {
    'key':'2bc4f479e6c2392d',
    'middle_area':middle_area_code, #　大エリアコードで東京を指定
    'format':'json'
    }
    # エリアマスタAPIのリクエストURL
    url = 'http://webservice.recruit.co.jp/hotpepper/small_area/v1/'
    # JSONを取得
    responce = requests.get(url, query)
    # JSONの読み込み
    result = json.loads(responce.text)['results']['small_area']

    small_area = {}
    # 小エリアのコードと名称を取得
    for (u,v) in enumerate(result):
        print(v['code'],'-',v['name'])
        print('"{}"'.format(v['name']),',')
        print('--------------------------------------------')
        small_area[v['name']] = v['code']
    
    return small_area




def get_area():
    # 大エリアマスタ用のクエリ
    query_l = {
    'key':'2bc4f479e6c2392d',
    'format':'json'
    }
    url_l = 'http://webservice.recruit.co.jp/hotpepper/large_area/v1/'
    responce_l = requests.get(url_l, query_l)
    result_l = json.loads(responce_l.text)['results']

    # 中エリアマスタ用のクエリ
    query_m = {
    'key':'2bc4f479e6c2392d',
    'keyword':'',
    'large_area':large_area_code, #　大エリアコードで東京を指定
    'format':'json'
    }
    url_m = 'http://webservice.recruit.co.jp/hotpepper/middle_area/v1/'
    responce_m = requests.get(url_m, query_m)
    result_m = json.loads(responce_m.text)['results']

    # 小エリアマスタ用のクエリ
    query_s = {
    'key':'2bc4f479e6c2392d',
    'middle_area':middle_area_code, #　大エリアコードで東京を指定
    'format':'json'
    }
    url_s = 'http://webservice.recruit.co.jp/hotpepper/small_area/v1/'
    responce_s = requests.get(url_s, query_s)
    result_s = json.loads(responce_s.text)['results']


    print(result_l)
    print(result_m)
    print(result_s)

    return result_l,result_m,result_s













# 店舗情報等を取得する
# 場所のみ絞り込みが出来ている。後は価格帯を整形する。


def gourmet_search(area_code,budget_code):
    # グルメサーチAPI用のクエリ
    query = {
    'key': '2bc4f479e6c2392d',
    # 'lat': '35.75012327488292', # 北千住駅の緯度
    # 'lng': '139.80508505043517', # 北千住駅の経度
    'middle_area': area_code, # 中エリアのコードを入力する
    'budget': budget_code, # 平均予算のコード
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

    # print('gourment')
    return gourment
    

# 予算を出す
def budget_masta():
    query = {
    'key': '2bc4f479e6c2392d',
    'format': 'json'
        }
    
    url = 'http://webservice.recruit.co.jp/hotpepper/budget/v1/'

    responce = requests.get(url, query)

    result = json.loads(responce.text)['results']['budget']

    b = {}
    # 中エリアのコードと名称を取得
    for (u,v) in enumerate(result):
        b[v['name']] = v['code']
    print(b['～500円'])
    return b




# middle_area_masta()
# gourmet_search(area_code,budget_code)
# budget_masta()

# middle_area = middle_area_masta()
# middle_area_code = middle_area['渋谷']
# small_area_masta(middle_area_code)

# get_area()

middle_area_masta()