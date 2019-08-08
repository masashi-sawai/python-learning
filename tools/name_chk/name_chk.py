import csv
import pickle
import pandas
import time
import sys
from tqdm import tqdm


def partial_match(str_name):
    # print('# 部分一致 (名前の末尾１文字を検索)')
    cnt_m = 0
    cnt_w = 0
    m_p = 0
    w_p = 0
    f = _csv_load("./test_dict_last2.csv")
    start = time.time()
    for row in f:
        if str_name in row['名']:
            #print(' * ' + row['名'] + ':' + row['性別'])
            if row['性別'] == '男性':
                cnt_m = cnt_m + 1
            elif row['性別'] == '女性':
                cnt_w = cnt_w + 1

    if (cnt_m + cnt_w) > 0:
        m_p = cnt_m / (cnt_m + cnt_w)
        w_p = cnt_w / (cnt_m + cnt_w)
    #    print('')
    #    print('>> ' + str_name + 'さんが男性の可能性：' + str('{:.2%}'.format(m_p)))
    #    print('>> ' + str_name + 'さんが女性の可能性：' + str('{:.2%}'.format(w_p)))
    # else:
    #    print('
    #    print('>> ' + str_name + 'さんは判定不能')
    #elapsed_time = time.time() - start
    #ti = "elapsed_time:{0}".format(elapsed_time) + "[sec]"
    #sys.stdout.write("\r%s" % ti)
    # sys.stdout.flush()

    return m_p, w_p


def perfect_match(str_name):
    # print('# 完全一致 (名前をそのまま検索)')
    cnt_m = 0
    cnt_w = 0
    m_p = 0
    w_p = 0
    f = _csv_load("./test_dict.csv")
    for row in f:
        if str_name == row['名']:
            #print(' * ' + row['名'] + ':' + row['性別'])
            if row['性別'] == '男性':
                cnt_m = cnt_m + 1
            elif row['性別'] == '女性':
                cnt_w = cnt_w + 1

    if (cnt_m + cnt_w) > 0:
        m_p = cnt_m / (cnt_m + cnt_w)
        w_p = cnt_w / (cnt_m + cnt_w)
        print('')
        print('>> ' + str_name + 'さんが男性の可能性：' + str('{:.2%}'.format(m_p)))
        print('>> ' + str_name + 'さんが女性の可能性：' + str('{:.2%}'.format(w_p)))
    else:
        print('')
        print('>> ' + str_name + 'さんは判定不能')

    return m_p, w_p


def _csv_load(file):
    csv_file = open(file, "r", encoding="utf8", errors="", newline="")
    f = csv.DictReader(csv_file, delimiter=",", doublequote=True,
                       lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    return f


# メイン処理
def main():
    partial_probability = {}
    perfect_probability = {}

    with open('./test_out.csv', 'w') as f:
        f.write("名")
        f.write(",")
        f.write("男性の確率（末尾判定）")
        f.write(",")
        f.write("女性の確率（末尾判定）")
        # f.write(",")
        # f.write("男性の確率（全文判定）")
        # f.write(",")
        # f.write("女性の確率（全文判定）")
        f.write("\n")

    f = _csv_load("./check_data.csv")

    for row in tqdm(f):
        partial_probability = partial_match(row['名'][-1])
        #perfect_probability = perfect_match(row['名'])
        with open('./test_out.csv', 'a') as f:
            f.write(row['名'])
            f.write(",")
            f.write(str(partial_probability[0]))
            f.write(",")
            f.write(str(partial_probability[1]))
            # f.write(",")
            # f.write(str(perfect_probability[0]))
            # f.write(",")
            # f.write(str(perfect_probability[1]))
            f.write("\n")

# partial_match
# perfect_matching

main()
