"""デコレーター

ポイント: Pythonでは関数もオブジェクト
Returns:
    _type_: _description_
"""
from ast import arg
from functools import wraps
from unittest import result

def logger(separator: str='-'):
    """関数の前後にマークを入れる

    Args:
        separator (str, optional): _description_. Defaults to '-'.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):  # 可変長引数
            # 事前処理
            print(10 * separator)
            result = func(*args, **kwargs)  # 後でresult()と呼び出す
            # 事後処理
            print(result)
            print(10 * separator)
            return result
        return wrapper
    return decorator # 関数ない関数のオブジェクトを返す

@logger('-')
def simple_sum1(x: int, y: int) -> int:
    return x + y

@logger('+')
def simple_time1(x: int,y: int) -> int:
    return x * y

if __name__ == '__main__':
    simple_sum1(10, 20)
    simple_time1(10, 20)