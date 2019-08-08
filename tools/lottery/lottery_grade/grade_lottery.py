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
    csv_lottery = './sample.csv'
    list_lottery = _csv_read(csv_lottery)

    # 等級表の読み込み
    csv_grade = './sample_grade.csv'
    list_grade = _csv_read(csv_grade)
    _check_input(list_lottery, list_grade)
    
    # 当選者選定
    for row in list_grade:
        grade_name = row[0] 
        grade_total = int(row[1])
        array = []
        while len(array) < grade_total:
            if (len(list_lottery) < win):
                break
            array.append(grade_name)
            array += _get_win(list_lottery, grade_total)
            list_lottery = _del_win(list_lottery, array)
            win = win - len(list_win)
        list_win.append(array)

    # 当選者出力
    for row in list_win:
        print(row)
        #print(row[0] + ',' + row[1])


# 抽選対象データ（csv）の読み込み
def _csv_read(filepath):
    list_lottery = []
    csv_file = open(filepath, "r", encoding="ms932",
                    errors="", newline="")
    f = csv.reader(csv_file, delimiter=",", doublequote=True,
                   lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    for row in f:
        list_lottery.append([row[0], row[1]])
    return list_lottery


# 入力値チェック
def _check_input(list_lottery, list_grade):
    total = 0
    for row in list_grade:
        total = total + int(row[1])
    if len(list_lottery) < total:
        print('INPUT ERROR：抽選対象数よりも当選対象数が大きい')
        exit()


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


