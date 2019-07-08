# 画像の縦横幅をチェックする簡易ツール

import numpy as np
import glob
import sys
from PIL import Image


def main(x, y, type_str, path, file_type):
    files = glob.glob(path + file_type)
    ng_cnt = 0
    ok_cnt = 0

    for file in files:
        sample = Image.open(file)
        sizestr = str(sample.size)
        chkstr_yoko = '(' + str(x) + ', ' + str(y) + ')'
        chkstr_tate = '(' + str(y) + ', ' + str(x) + ')'

        if sizestr != chkstr_yoko and sizestr != chkstr_tate:
            print('NG:' + file)
            ng_cnt = ng_cnt + 1
        else:
            ok_cnt = ok_cnt + 1
        #    print('OK:' + file)
        # print(chkstr)

    print()
    print(type_str)
    print('Tate: W = ' + str(y) + ', H = ' + str(x) +
          ' / Yoko: W = ' + str(x) + ', H = ' + str(y))
    print('OK：' + str(ok_cnt))
    print('NG：' + str(ng_cnt))

args = sys.argv
err = ''
if len(args) == 5:
    if args[1].isdigit():
        x = int(args[1])
    else:
        err += 'x,'
    if args[2].isdigit():
        y = int(args[2])
    else:
        err += 'y,'
    path = args[3]
    file_type = args[4]
    if err != '':
        print('Input Error:' + err)
        exit()
    type_str = '# Test_Image'
else:
    x = 140
    y = 95
    path = 'C:/Users/sawai/Test'
    file_type = '/*.gif'
    type_str = '# Test_Image'
print(err)
main(x, y, type_str, path, file_type)
