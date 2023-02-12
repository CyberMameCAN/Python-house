"""クラスの作り方

とりあえず、これだけを覚える(これだけで何とかなる)
  1. dataclass
  2. property
  3. setter
Raises:
    Exception: _description_

Returns:
    _type_: _description_
"""

from datetime import date, timedelta
from dataclasses import dataclass

# @ ではじまるキーワードはデコレータと呼称
#   関数やクラスに特殊な振る舞いを注入することのできる機能
# @property 変数のように参照が出来る。関数だけど使い方は object.name と使う。()は付けない。
# @xxx.setter プロパティに代入したい時
@dataclass
class User:
    id: int = 0
    email: str = ''
    first_name: str = ''
    last_name: str = ''
    _birthday: date = date.today()

    @property
    def name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @name.setter
    def name(self, _name: str) -> None:
        if ' ' not in _name:
            raise Exception('invalid fullname error')
        self.first_name, self.last_name = _name.split(' ')

    @property
    def age(self) -> int:
        timedelta = date.today() - self._birthday
        return timedelta.days // 365

    @property
    def birthday(self) -> date:
        return self._birthday

    @birthday.setter
    def birthday(self, _birthday: date) -> None:
        self._birthday = _birthday

    def __repr__(self) -> str:
        return f'User<id: {self.id}, email: {self.email}, name: {self.name}, age: {self.age}>'

user = User()
user.id = 1
user.email = 'test@example.ts'
user.first_name = 'John'
user.last_name = 'Conner'
user.birthday = date(1999, 7, 15)
print(user)