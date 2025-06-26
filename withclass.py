'''
自作クラスのインスタンスを*with構文*で作成するのは便利だと思う。

with構文と一緒に使う。__enter__(), __exit__()
一般には
  __enter__ メソッドでリソースを確保するような処理、
  __exit__  メソッドでリソースを解放するような処理を実装

https://magazine.techacademy.jp/magazine/31663
'''

from time import time

class Timer:
    def __init__(self):
        self.fmt_str = '{:.3f}'
        self.logger = None

    @property
    def duration(self):
        if self.end is None:
            return 0
        return self.end - self.start

    def __enter__(self):
        """ with文が開始された時に呼ばれる """
        self.start = time()

    def __exit__(self, exc_type, exc_value, traceback):
        """ with文が終了した時に呼ばれる (エラー発生時も) """
        print(exc_type, exc_value, traceback)

        self.end = time()
        out_str = self.fmt_str.format(self.duration)
        if self.logger:
            self.logger.info(out_str)
        else:
            print(out_str)
            

with Timer() as timer:
    print('Timerクラスの実行')

print('---')

with Timer() as c:
    raise Exception('例外が発生')