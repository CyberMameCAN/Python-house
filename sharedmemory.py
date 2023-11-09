import random
from collections import namedtuple, deque


def shared_memory():
    l = [0, 1, 2, 3, 4, 0]

    print(list(set(l)))
    print(random.choice(l))
    print(random.choices(l, k=2))  # listが返る
    print(random.sample(l, 3))  # listが返る, 要素の重複はなし

    # 名前付きTuple
    # tupleと同様に変更不可(イミュータブル)
    # https://qiita.com/Seny/items/add4d03876f505442136
    Transition = namedtuple('Transition',
                            ('state', 'action', 'next_state', 'reward'))
    print()

    # 効率的方法
    # 通常使いはlistで十分だろうということらしい。
    # https://note.nkmk.me/python-collections-deque/
    # 　要素の追加・取り出し（削除）・アクセス（取得）が両端のみ -> deque
    # 　両端以外の要素に頻繁にアクセス -> list
    memory_ = deque([], maxlen=3)  # 前もってメモリ確保してる？
                                   # maxlenを超えたら古いものから削除されている
    memory_.append(Transition(0,1,2,3))
    memory_.append(Transition(4,5,6,7))
    memory_.append(Transition(8,9,10,11))
    print(memory_[1].state)  # '名前'でアクセスできる


def main():
    shared_memory()


if __name__ == '__main__':
    main()
