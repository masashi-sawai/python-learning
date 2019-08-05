import sys
import csv
import random


# メイン処理
def main():
    args = sys.argv
    list_lottery = []
    list_win = []
    win_max = 0
    win = 0

    # 抽選対象者の読み込み
    list_lottery = _csv_read()
    win_max = _check_input(args, len(list_lottery))
    win = win_max

    # 当選者選定
    while len(list_win) < win_max:
        if (len(list_lottery) < win):
            break
        list_win += _get_win(list_lottery, win)
        list_lottery = _del_win(list_lottery, list_win)
        win = win - len(list_win)

    # 当選者出力
    for row in list_win:
        print(row[0] + ',' + row[1])


# 抽選対象データ（csv）の読み込み
def _csv_read():
    list_lottery = []
    csv_file = open("./sample.csv", "r", encoding="ms932",
                    errors="", newline="")
    f = csv.reader(csv_file, delimiter=",", doublequote=True,
                   lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    for row in f:
        list_lottery.append([row[0], row[1]])
    return list_lottery


# 入力値チェック
def _check_input(args, csv_len):
    if len(args) == 1:
        print('INPUT ERROR：第1引数に生成数を指定')
        exit()
    if not args[1].isdigit():
        print('INPUT ERROR：第1引数に数値を指定')
        exit()
    if csv_len < int(args[1]):
        print('INPUT ERROR：抽選対象数よりも当選対象数が大きい')
        exit()

    return int(args[1])


# 当選者選定
def _get_win(list_lottery, win):
    list_win = random.sample(list_lottery, win)
    list_unique = []
    for win in list_win:
        if win not in list_unique:
            list_unique.append(win)
    return list_unique


# 抽選対象者から当選者を除外
def _del_win(list_lottery, list_win):
    arr = []
    for lottery in list_lottery:
        if lottery not in list_win:
            arr.append(lottery)
    return arr


if __name__ == "__main__":
    main()
