'''
ポイント: __iter__, __next__, 
'''

def my_generator():
    x = 10
    yield x
    x = x + 10
    yield x
    x = x + 10
    yield x

mg = my_generator()  # 関数にyieldがあったらオブジェクトを返す

for x in mg:
    print(x)
# １行ずつ書くならnext()メソッドを使う

print(dir(mg))