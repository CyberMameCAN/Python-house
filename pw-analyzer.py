from collections import Counter
from datetime import datetime
import os
import secrets
import string
"""
使い方
    poetry run python pw-analyzer.py

    処理したいパスワードを入力すると、
    一致するか、パスワードの長さの1.5倍の数をランダムに総当りで調べる。
"""

class PasswordChecker:
    """
    パスワードをチェックするクラス
    """
    def __init__(self):
        """パスワードに使う文字列を生成
        - アルファベット(小文字・大文字)
        - 数字
        """
        self.available_character = string.ascii_letters + string.digits


    def password_producer(self, string_length=8) -> str:
        """
        パスワードを生成する
        
        Attributes
        ----------
        string_length: int
            生成するパスワード長
            デフォルト値: 8

        Return
        ----------
        _pwd: str
            生成したパスワード
        """
        self.string_length = string_length

        _pwd = ''.join(secrets.choice(self.available_character) for i in range(string_length))
        return _pwd


    def validation_check(self, _pwd: str) -> bool:
        """
        生成したパスワードをチェックする
        - 全てが同じ文字列だった時はERROR
        - 他はOK
        
        Attributes
        ----------
        _pwd: str
            チェックするパスワード

        Return
        ----------
        is_good: bool
            パスワードのチェック結果
            - True
            - False
        """
        is_good = True

        _counter = Counter(_pwd)
        args = dict(_counter)
        _max_value = max(args.values())
        if len(_pwd) == _max_value:  # 所謂、全部が同一文字列だった場合
            print(max(args, key=args.get))
            print(max(args.values()))

            is_good = False  # 不可

        return is_good


    def rockn_roll(self, user_pwd) -> str:
        """
        メイン処理
        生成したパスワードと入力のパスワードが同じかどうか調べる。
        一致したらそのパスワードを返す。
        
        Attributes
        ----------
        user_pwd: str
            調べる(目的の)パスワード

        Return
        ----------
        pw: str
            一致したパスワード
        """
        # 想定パスワード長の1.25倍を超えても見つからない場合は、ループを抜ける
        max_password_length = (len(self.available_character) ** len(user_pwd)) * 1.25
        print(f"最大カウント {max_password_length}")

        i = 0
        while True:
            os.system('clear')  # 画面の表示をクリアする(Mac/Linux), Winは'cls'

            # pw = ''
            # for _ in range(len(self.user_pwd)):
            #     guess_pwd = self.pwd[randint(0, len(self.pwd) - 1)]  # パスワード生成では非推奨
            #     pw = str(guess_pwd) + str(pw)
            pw = self.password_producer(self.string_length)
            print(f"{i}: {pw}")
            print('Cracking Password...Please Wait')

            # if pw == user_pwd:  # 非推奨(タイミング攻撃)
            if secrets.compare_digest(pw, user_pwd):
                # パスワード一致
                break

            i += 1
            if i > max_password_length:
                pw = 'Give up...!'
                break

        return pw


if __name__ == "__main__":
    # 開始時刻を取得
    start = datetime.today()

    pw_checker = PasswordChecker()
    string_length = 3
    user_pwd = pw_checker.password_producer(string_length)
    print(f"今回パスワード {user_pwd}")
    # 入力待ち
    # user_pwd = input('Enter a password: ')
    if pw_checker.validation_check(user_pwd):
        # 解析開始
        hit_pw = pw_checker.rockn_roll(user_pwd)
        print(f'Your Password Is: {hit_pw}')
    else:
        print("パスワードチェックエラー")

    # 終了時刻を取得
    end = datetime.today()
    # 差分を計算
    dif = end - start
    print(dif)

