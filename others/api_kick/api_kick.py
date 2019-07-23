# 基本的なAPIキックの処理フォーマット
import requests
import json

url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
res = requests.get(url)
lists = json.loads(res.text)

for list in lists:
    print(list)
