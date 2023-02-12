"""データを格納するのに特化したクラス

dataclass  python3.7以上
"""
from dataclasses import dataclass, field, asdict

#@dataclass(flozen=True)  # 変更できないクラス
@dataclass
class User:
    name: str
    age: int = 38  # デフォルト値も設定できる
    #items: list[int] = field(default_factory=list)  # インミュータブル 空のリスト
    items: list[int] = field(default_factory=lambda: ['note', 'pen'])

user = User('Suzuki', 21)
print(user.name)
print(user.age)
print(user.items)

result = asdict(user)  # 辞書型を作って返す事ができる
print(result)

'''
user1 = User('Subaru')
user1 = User('Honda')
print(user1 == user2)  # dataclassではTrue
                       # 普通のクラスではオブジェクトが別だから、Falseだが
                       # フィールド同士を比べている
'''