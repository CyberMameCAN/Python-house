from decimal import Decimal
from decimal import getcontext

getcontext().prec = 250

_miracle_number = Decimal('1') / Decimal('9801')
miracle_number = f"{_miracle_number}"

_decimal = miracle_number.split('.')[1]  # 小数点で分けて、小数部のみ抜き出す
max_string = len(_decimal)
step_num = 2  # 2文字ずつ
for i in range(0, max_string, step_num):
    print(f"{_decimal[i:i+step_num]} [{int(i/step_num)+1}]")