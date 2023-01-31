import os
from contextlib import suppress
import re

def practise():

    with suppress(FileNotFoundError):
        # ファイルがなくてもエラーにならない
        os.remove('test.txt')

    sk = ('shinji', 'kawasaki', 80)
    # sk[2] = 99  # イミュータブル TypeError
    # print(sk)

def regex_practise():
    sss = '54.5△'
    _sss = re.sub(r'\D\Z', '', sss)
    print(_sss)

    pattern = re.compile(r'(\d{3})-(\d{3})-(\d{3})')
    mo = pattern.search(f'123-456-789')
    print(mo.group(0))
    print(mo.group(1))
    print(mo.group(2))
    print(mo.group(3))

    _junk = pattern.match(f'123-456-789')
    print(_junk.group(1))

def main():
    # practise()
    regex_practise()

if __name__ == '__main__':
    main()
