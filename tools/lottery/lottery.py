import sys
import csv
import random


def main():
    args = sys.argv
    win_max = _check_input(args)
    win = win_max
    lottery_list = []
    win_list = []
    unique_list = []

    # 抽選対象者の配列化
    lottery_list = _get_input(_csv_read())

    while len(win_list) < win_max:
        # 重複を除外した当選者リスト
        win_list += _get_unique(_get_win(lottery_list, win))

        # 抽選対象者の配列から当選者を除外
        lottery_list = _del_win(lottery_list, win_list)
        win = win - len(win_list)

    print('---------')
    print(' 当選者 ')
    print('---------')
    for row in win_list:
        print(row[0] + ',' + row[1])


def _check_input(args):
    if len(args) == 1:
        print('INPUT ERROR：第1引数に生成数を指定')
        exit()

    if not args[1].isdigit():
        print('INPUT ERROR：第1引数に数値を指定')
        exit()

    return int(args[1])


def _csv_read():
    csv_file = open("./sample.csv", "r", encoding="ms932",
                    errors="", newline="")
    f = csv.reader(csv_file, delimiter=",", doublequote=True,
                   lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    return f


def _get_input(f):
    lottery_list = []
    for row in f:
        lottery_list.append([row[0], row[1]])
    return lottery_list


def _get_win(lottery_list, win):
    win_list = random.sample(lottery_list, win)
    return win_list


def _get_unique(win_list):
    unique_list = []
    for win in win_list:
        if win not in unique_list:
            unique_list.append(win)
    return unique_list


def _del_win(lottery_list, win_list):
    arr = []
    for lottery in lottery_list:
        if lottery not in win_list:
            arr.append(lottery)
    return arr

if __name__ == "__main__":
    main()
