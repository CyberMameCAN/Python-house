class TestClass:
    pass

def object_memory_size():
    """
    オブジェクトのメモリサイズ
    システムパス
    """
    import sys
    test = TestClass()
    print(sys.getsizeof(test), 'byte')
    print(sys.path)


object_memory_size()


def max_value() -> float:
    """NaNがある時でも最大値として数値の最大値を返す"""
    import numpy as np

    a = np.array([0., np.nan, 5., 3., 8.])
    _max = np.nanargmax(a)
    return _max

# max_value()

def random_value() -> None:
    """乱数を作る"""
    import numpy as np

    for _ in range(10):
        print(np.random.randint(0, 10))

# random_value()

def none_practice():
    a = None
    # こちらが、よりPythonっぽい
    if not a:
        print('OK') # <<
    else:
        print('NG')

    a = None
    if a is not None:
        print('OK')
    else:
        print('NG') # <<

none_practice()

def numpy_diff():
    import numpy as np

    np.diff([1,2,3,4,5])

# numpy_diff()

def numpy_str_to_number():
    """文字列 -> 数値へ変換"""
    import numpy as np

    np.asfarray(['01', '02'])
    # array([1., 2.])

def shift_practice():
    import pandas as pd

    twod_array = [[0,1,2,10],[3,4,5,11],[6,7,8,12]]
    data = pd.DataFrame(twod_array, columns=['A','B','C','D'])
    
    shift_val = data[['A', 'B']].shift(-1)
    shift_val.columns = ['preA', 'preB']

    data.loc[:, ['preA', 'preB']] = shift_val[['preA','preB']]
    #data.loc[:, 'preB'] = shift_val['preB']

def not_defined_practice():
    """オブジェクトが作られていなかったら例外でキャッチ"""
    try:
        dummy
    except NameError as e:
        print('[NameError] Exception occured,', e)

not_defined_practice()

def args_practice():
    """"""
    # args: tuple = ('a', 2)
    args: tuple = (1, 'b')
    # tpl[0]
    def func(a, b):
        print(a, b)
        
    func(*args)

args_practice() # >> 1 b

"""デコレータのテスト"""
def my_decorator(func):
    def wrapper():
        print(f"Running {func.__name__}")
        func()
        print("Complete")
    return wrapper

@my_decorator
def do_this():
    print('Doing This')
	
@my_decorator
def do_that():
    print('Doing That')
	
do_this()
do_that()


"""可変長引数"""
def func(X, Y, Z):
    return X+Y, X*Y, Z+Y+X

# 第一感のやり方
# def xy(return_func, X, Y):
#     x, y = return_func(X, Y)
#     print(x, y)

# 可変長引数が使えるとなると便利バク上がり
def xy(return_func, *args):
    x, y, z = return_func(*args)
    print(x, y, z)

xy(func, 5, 3, 1)


"""filterの使い方"""
nums = range(1000, 2000)

def is_prime(num: int) -> bool:
	for x in range(2, int(num/2)+1):
		if (num % x) == 0:
			return False
	return True

# filter(関数名, コレクション要素) コレクションを1つづつ関数に渡して、Trueとなる要素となるコレクションを作成する
# (オブジェクトのアドレスが返る)
# list()などで変換する
# primes = filter(is_prime, nums)
primes = list(filter(is_prime, nums))
print(len(primes), primes)


"""関数の中で関数を呼ぶ"""
# def print_(letter: str):
#     return letter
def print_():
    print('HELLO, Kagoshima')
    
def junk(return_func):
    return return_func
    
junk(print_())  #-> HELLO, Kagoshima
# junk(print_)  # function object

def lambda_call():
    """無名関数の使い方"""
    import pandas as pd

    l = list(range(1, 9))
    # for x in l:
    #     if x in([1, 2, 3]):
    #         print('1')
    #     else:
    #         print('0')

    junk = lambda x: 1 if x in([1, 2, 3]) else 0
    pd.Series(l).map(junk)
# lambda_call()

def lambda_call2():
    s = (lambda x, y: x * y)(2, 5)
    print(s)
lambda_call2()

def useage_apply():
    """df.apply()で引数2つの場合"""
    import pandas as pd

    train = pd.DataFrame(columns=['Age','Sex'])  # データ入ってないから駄目
    train['Person'] = train[['Age','Sex']].apply(get_person, axis=1)

    def get_person(passenger):
        age, sex = passenger
        return 'child' if age < 16 else sex

def set_object():
    data_list = [104, 195, 195, 104, 512, 592, 902, 421]
    set(data_list)  # 重複は取り除かれる
    # {104, 195, 421, 512, 592, 902}


def cycle_practice():
    """ループを繰り返す"""
    import time
    from itertools import cycle

    lights = [
        ('Green', 2),
        ('Yellow', 0.5),
        ('Red', 2)
    ]
    colors = cycle(lights)
    while True:
        c, s = next(colors)
        print(c)
        time.sleep(s)
# cycle_practice()

def map_practice():
    """この様な使い方もある"""
    x = [4, -5, 6]
    y = lambda x: abs(x//2)
    z = list(map(y, x))
    print(list(map(y, x)))
map_practice()

def int_delimiter():
    """数値だけどこういう区切り方も出来る"""
    num1 = 1_000_000_000
    num2 = 2_000

    ans = num1 * num2
    print(ans)  # 2000000000000
    print(f'{ans:,}')  # 2,000,000,000,000
    print(f'{ans:_}')  # 2_000_000_000_000
int_delimiter()

