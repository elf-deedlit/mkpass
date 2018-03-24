#!/usr/bin/env python3
# vim: set fileencoding=utf-8:
import string
import argparse
import secrets
import random

def main():
    parser = argparse.ArgumentParser(description = "ランダムパスワード生成")
    parser.add_argument('-d', '--digits', action = 'store_true', help = '数値を使う')
    parser.add_argument('-l', '--lower', action = 'store_true', help = 'アルファベット小文字を使用する')
    parser.add_argument('-u', '--upper', action = 'store_true', help = 'アルファベット大文字を使用する')
    parser.add_argument('-s', '--strings', action = 'store_true', help = 'アルファベットを使用する')
    parser.add_argument('-m', '--mark', type = str, nargs = 1, help = '記号を利用する')
    parser.add_argument('num', nargs='?', type=int, default=8, help = "桁数")

    args = parser.parse_args()

    ls = []
    if args.lower or args.strings:
        ls.append(string.ascii_lowercase)
    if args.upper or args.strings:
        ls.append(string.ascii_uppercase)
    if args.digits:
        ls.append(string.digits)
    if args.mark:
        ls.append(args.mark[0])

    stn = len(ls)
    if stn < 1:
        print('文字種の指定が必要です')
        parser.print_usage()
        return

    nr = args.num
    if stn > nr:
        print('文字種類に対して桁数が少なすぎます')
        parser.print_usage()
        return

    passwd = []
    for s in ls[:-1]:
        if nr <= stn:
            max_nr = 1
        else:
            max_nr = secrets.randbelow(nr - stn) + 1
        passwd += [secrets.choice(s) for n in range(0, max_nr)]
        nr -= max_nr
    passwd += [secrets.choice(ls[-1]) for n in range(0, nr)]
    random.shuffle(passwd)
    print(''.join(passwd))

if __name__ == '__main__':
    main()


