import csv
import numpy as np
import matplotlib.pyplot as plt

# ※注：実行時は日本語フォント必須（実行環境のmatplotlib配下へインストール）
# https://qiita.com/katuemon/items/5c4db01997ad9dc343e0


def main():

    # 回答CSVの読み込んで回答サマリを返す
    ans = _csv_read()

    # 棒グラフ要素定義
    left = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    height = np.array([ans[0], ans[1], ans[2], ans[3], ans[4], ans[
                      5], ans[6], ans[7], ans[8], ans[9], ans[10]])
    label = ["項目1", "項目2", "項目3", "項目4", "項目5",
             "項目6", "項目7", "項目8", "項目9", "項目10", "項目11"]

    # 日本語フォント読み込み
    plt.rcParams['font.family'] = 'IPAexGothic'

    # 初期ウィンドウサイズ指定
    plt.figure(figsize=(15, 6), dpi=150)

    # 棒グラフの天井を「読み込んだ値×1.2」にする
    plt.ylim(ymax=max(height) * 1.2, ymin=0)

    # 棒グラフ描画
    plt.bar(left, height, color="#FF5B70", edgecolor="#CC4959",
            linewidth=4, tick_label=label, align="center")
    plt.tick_params(axis='x', which='major', labelsize=13)
    plt.tick_params(axis='y', which='major', labelsize=16)
    plt.title("サンプルグラフ", fontsize=18)
    plt.xlabel("（回答項目）\n\na", fontsize=12)
    plt.ylabel("（回答件数）\n", fontsize=12)
    for x, y in zip(left, height):
        plt.text(x, y, str(y) + '件\n', ha='center', va='bottom', fontsize=18)

    # 棒グラフ表示
    plt.show()


def _csv_read():
    cnt = 0
    list_ans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    csv_file = open("./out.csv", "r", encoding="ms932",
                    errors="", newline="")
    f = csv.reader(csv_file, delimiter=",", doublequote=True,
                   lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    for row in f:
        for cnt in range(10):
            list_ans[cnt] = list_ans[cnt] + int(row[cnt + 1])
            cnt = cnt + 1
        cnt = 0
    return list_ans


if __name__ == "__main__":
    main()
