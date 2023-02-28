# 通常の意味
#
# 手信号、信号装置
# Python
#
# 並列処理を行っても問題のないスレッドの数を指定して、並行処理ができるようにするもの
# 排他制御
#
#     lock 1つのスレッドを対象
#     semaphore 複数のスレッドを対象
#
# 実行
# poetry run python semaphore.py
# 
# OUTPUT
# var1 sleep前
# var2 sleep前
# var1 sleep後 //
# var3 sleep前
# var2 sleep後 //
# var4 sleep前
# var3 sleep後 //
# var4 sleep後 //
#
# この変数の値を変更して、どの様に動くか試すと分かりやすかった
# thread_count = 2
#
import logging
import time
from threading import Semaphore, Thread

def my_func(semaphore, var1, var2):
    """
    threadで実行する関数にSemaphoreを引数として渡す
    :param Semaphore semaphore:
    :param str var1:
    :param str var2:
    """
    with semaphore:
        print(f'{var1} sleep前')
        time.sleep(1)
        print(f'{var2} sleep後 //')


def main():
    # threadの起動する数を指定
    thread_count = 2
    s = Semaphore(thread_count)

    t1 = Thread(target=my_func, args=(s, "var1", "var1"))
    t2 = Thread(target=my_func, args=(s, "var2", "var2"))
    t3 = Thread(target=my_func, args=(s, "var3", "var3"))
    t4 = Thread(target=my_func, args=(s, "var4", "var4"))

    t1.start()
    t2.start()
    t3.start()
    t4.start()


if __name__ == '__main__':
    main()
