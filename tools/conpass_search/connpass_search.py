import sys
import random
import requests
from datetime import datetime


def chk(args):
    if len(args) == 1:
        print('INPUT ERROR：コマンドライン第1引数に「検索キーワード」は必須です')
        exit()

    keywords = args[1]

    ym = datetime.now().strftime("%Y%m")
    if len(args) == 3:
        if len(args[2]) == 6 and args[2].isdigit():
            ym = args[2]
        else:
            print('INPUT ERROR：コマンドライン第2引数は「開催月」を「yyyymm」で入力してください（省略時は当月で検索します）')
            exit()
    return keywords, ym


def main(keywords, ym):
    # print(keyword)
    # exit()
    rand = random.randint(1, 100)
    print(rand)
    params = {
        'keyword': keywords,
        'ym': ym,
        'order': 3,
        'start': rand,
        'count': 1
    }
    url = 'https://connpass.com/api/v1/event/'
    r = requests.get(url, params=params)
    event_info = r.json()

    print('---------------------------------')
    print('# conpassイベント 何がでるかな？')
    print('---------------------------------')
    print(event_info['events'])
    if event_info['events'] != "":
        for event in event_info['events']:
            print('イベント名：' + event['title'] + ' ' + event['catch'])
            print('開　催　日：' + event['started_at'])
            print('場　　　所：' + event['address'])
            print('会　　　場：' + event['place'])
            print('詳細ページ：' + event['event_url'])
            print('参加者定員：' + str(event['limit']))
            print('参　加　者：' + str(event['accepted']))
            print('補　欠　者：' + str(event['waiting']))
            #print('概　　　要：' + event['description'])
            if 'series' is event:
                print('主催グループ名 ：' + event['series']['title'])
                print('主催グループURL：' + event['series']['url'])
            print('---------------------------------')
    else:
        '検索失敗, 同じ検索キーワードでも再検索でヒットすることもあります'


if __name__ == '__main__':
    args = sys.argv
    keywords = []
    keywords, ym = chk(args)
    main(keywords, ym)
