from decimal import Decimal
from decimal import getcontext
"""
巡回小数の 1 / 9801 を求める
https://blog.tstylestudio.com/2023/04/06/1%e3%82%929801%e3%81%a7%e5%89%b2%e3%81%a3%e3%81%9f%e8%a8%88%e7%ae%97%e7%b5%90%e6%9e%9c/

"""
getcontext().prec = 250

_miracle_number = Decimal('1') / Decimal('9801')
miracle_number = f"{_miracle_number}"

_decimal = miracle_number.split('.')[1]  # 小数点で分けて、小数部のみ抜き出す
max_string = len(_decimal)
step_num = 2  # 2文字ずつ
for i in range(0, max_string, step_num):
    print(f"{_decimal[i:i+step_num]} [{int(i/step_num)+1}]")