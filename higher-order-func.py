# 高階関数
# https://utokyo-ipp.github.io/6/6-2.html
#
# - map()
# - filter()
# - reduce()
#
#
def higher_order():
    # max
    ls = [3, -8, 1, 0, 7, -5]
    print(max(ls))
    print(max(ls, key=abs))  # absを考慮した上でのmaxだった[値そのもの]が返る

    # sorted
    print(sorted(ls))
    print(sorted(ls, key=abs, reverse=True))

    # ラムダ式
    print(sorted(ls, key=lambda x: -x))

    # 型を確認
    print(type(abs))
    print(type(lambda x: -x))
    
    # map
    #print([abs(x) for x in ls])
    #for x in map(abs, ls):
    #    print(x)
    print([x for x in map(abs, ls)])
    it = map(abs, ls)
    print(next(it))
    print(next(it))

    # filter
    print(list(filter(lambda n: n % 3 == 0, ls)))

higher_order()
