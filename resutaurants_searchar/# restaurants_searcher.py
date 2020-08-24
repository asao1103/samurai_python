# restaurants_searcher.py

import csv
import json
import requests

# 初期設定
KEYID = "2cd3fc383c95fa2e5270c99b9df974b1"
HIT_PER_PAGE = 100
PREF = "PREF13"
FREEWORD_CONDITION = 1
FREEWORD = "渋谷駅"

PARAMS = {"keyid": KEYID, "hit_per_page":HIT_PER_PAGE, "pref":PREF, "freeword_condition":FREEWORD_CONDITION, "freeword":FREEWORD}

def write_data_to_csv(params):
    resturants = [["名称","住所","営業日","電話番号"]]
    json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/", params=params).text
    response = json.loads(json_res)
    if "error" in response:
        return print("エラーが発生しました！")
    for resturant in response["rest"]:
        rest_info = [resturant["name"], resturant["address"], resturant["opentime"], resturant["tel"]]
        resturants.append(rest_info)
    with open("requests_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(resturants)
    return print(resturants)
    
write_data_to_csv(PARAMS)
