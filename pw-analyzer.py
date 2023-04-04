from datetime import datetime
import os
from random import randint
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
        - アルファベット(小文字)
        - 数字
        """
        self.pwd = []
        # print(string.ascii_lowercase)
        for _letter in string.ascii_lowercase:
            # print(_letter)
            self.pwd.append(_letter)
            
        for _fig in range(10):
            self.pwd.append(str(_fig))
        

    """
    メイン処理
    パスワードをランダムに生成して、
    生成したパスワードと入力のパスワードが一致したら、
    そのパスワードを返す
    
    Attrbutes
    ---------
    user_pwd: str
        調べる(目的の)パスワード

    Return
    ---------
    pw: str
        一致したパスワード
    """
    def rockn_roll(self, user_pwd: str) -> str:
        # 想定パスワード長の1.5倍を超えても見つからない場合は、ループを抜ける
        max_password_length = (len(self.pwd) ** len(user_pwd)) * 1.5
        print(f"最大カウント {max_password_length}")

        i = 0
        while True:
            os.system('clear')  # 画面の表示をクリアする(Mac/Linux), Winは'cls'

            pw = ''
            for letter in range(len(user_pwd)):
                guess_pwd = self.pwd[randint(0, len(self.pwd) - 1)]
                pw = str(guess_pwd) + str(pw)

            print(f"{i}: {pw}")
            print('Cracking Password...Please Wait')

            if pw == user_pwd:
                # パスワード一致
                break

            i += 1
            if i > max_password_length:
                pw = '見つからない'
                break

        return pw


if __name__ == "__main__":
    # 開始時刻を取得
    start = datetime.today()

    pw_checker = PasswordChecker()
    # 入力待ち
    user_pwd = input('Enter a password: ')
    # 解析開始
    hit_pw = pw_checker.rockn_roll(user_pwd)

    print(f'Your Password Is: {hit_pw}')

    # 終了時刻を取得
    end = datetime.today()
    # 差分を計算
    dif = end - start
    print(dif)

