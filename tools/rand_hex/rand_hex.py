import sys
import os
import hashlib


def chk(args):
    if len(args) == 1:
        print('INPUT ERROR：第1引数に生成数を指定')
        exit()

    if not args[1].isdigit():
        print('INPUT ERROR：第1引数に数値を指定')
        exit()

    return int(args[1])


def main(order):
    print('-------------------------')
    print(' ■32桁の乱数生成 {0}件'.format(order))
    print('-------------------------')
    param = ''
    output = ''
    cnt = 0
    for cnt in range(order):
        param = _rand_hex(32)
        print(param)
        output += param + '\n'
    return output


def _rand_hex(length):
    work = ''
    while len(work) < length:
        work += hashlib.md5(os.urandom(100)).hexdigest()

    return work[0:length]


if __name__ == '__main__':
    args = sys.argv
    order = chk(args)
    output = main(order)
    with open("hoge.txt", "w") as f:
        f.write(output)
