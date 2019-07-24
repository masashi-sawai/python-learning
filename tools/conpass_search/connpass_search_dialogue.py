import random
import requests
import time
from datetime import datetime


def main():
    keywords = []
    ym = ""

    print('---------------------------------------------')
    print('# (・∀・) connpassイベント 何がでるかな？')
    print('# 機能：ランダムで1件 イベントを検索します')
    print('---------------------------------------------')

    keywords, ym = _input_data()
    keywords, ym = _check(keywords, ym)
    print('')
    print('検索中・・・')
    print('')
    event_data = _req(keywords, ym, 10)

    event_data = _req(keywords, ym, 10)
    if len(event_data['events']) == 1:
        print('■ 検索結果')
    else:
        time.sleep(1)
        event_data = _req(keywords, ym, 1)
        if len(event_data['events']) == 1:
            print('■ 検索結果')
        else:
            print('(*_*;) 検索失敗 該当するイベントが見つかりませんでした')
            exit()

    for event in event_data['events']:
        if event['catch'] is not None:
            print('イベント名：' + event['title'] + ' ' + event['catch'])
        else:
            print('イベント名：' + event['title'])
        if event['started_at'] is not None:
            print('開　催　日：' + event['started_at'])
        if event['address'] is not None:
            print('場　　　所：' + event['address'])
        if event['place'] is not None:
            print('会　　　場：' + event['place'])
        if event['event_url'] is not None:
            print('詳細ページ：' + event['event_url'])
        if event['limit'] is not None:
            print('参加者定員：' + str(event['limit']))
        if event['accepted'] is not None:
            print('参　加　者：' + str(event['accepted']))
        if event['waiting'] is not None:
            print('補　欠　者：' + str(event['waiting']))
        # if event['description'] is not None:
        #     print('概　　　要：' + event['description'])
        if event['series'] is not None:
            if event['series']['title'] is not None:
                print('主催グループ名 ：' + event['series']['title'])
            if event['series']['url'] is not None:
                print('主催グループURL：' + event['series']['url'])
        print('')
        print('↑ピン！ときたら、ぜひ参加してみよう！')
        print('---------------------------------------------')


def _input_data():
    print('■ 検索キーワードを入力してください（単体検索例：python　複数検索例：python,大阪）')
    keywords = input()
    if keywords == "":
        print('(*_*;) INPUT ERROR：検索キーワードは必須です')
        exit()
    print('')
    print('■ 開催年月を「yyyymm」で入力してください 省略時は当月を検索対象とします（検索例：201908）')
    ym = input()
    return keywords, ym


def _check(keywords, ym):
    if ym == "":
        ym = datetime.now().strftime("%Y%m")
    else:
        if (len(ym) != 6 and len(ym) != 8) or not ym.isdigit():
            print('(*_*;) INPUT ERROR：第2引数（開催年月）の入力時は「yyyymm」または「yyyymmdd」の形式で入力してください')
            exit()
    return keywords, ym


def _req(keywords, ym, rand):
    params = {
        'keyword': keywords,
        'order': random.randint(1, 3),
        'start': random.randint(1, rand),
        'count': 1
    }
    if len(ym) == 6:
        params['ym'] = ym
    else:
        params['ymd'] = ym
    url = 'https://connpass.com/api/v1/event/'
    r = requests.get(url, params=params)
    return r.json()


if __name__ == '__main__':
    main()
