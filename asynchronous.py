"""
Python 3.7+ 
https://docs.python.org/ja/3/library/asyncio.html?highlight=asyncio#module-asyncio

並列処理の時に使う。
いったん処理を中断(一時停止)した後、続きから処理を再開する。

- async   コルーチン関数を定義する(作る)
- await   何か別の処理が完了するまで待たせる
- asyncio   コルーチンを実行する

コルーチンは**タスク**として実行される
awaitすることで内部的にタスクが作成 >> 実行という流れ

タスクを作成
  - asyncio.create_task()
  - Python3.11以降だと**asyncio.TaskGroup()**というのもある

"""
import asyncio
import time


async def task(delay: int):
    print(f'{delay}s Hello ...')
    await asyncio.sleep(delay)  # 3秒待つ
    print(f'  {delay}s ... World!')

async def main():  # コルーチンオブジェクトを返す
    print(f"started at {time.strftime('%X')}")

    await task(3)
    print('task(3) の次の行')
    await task(1)
    print('task(1) の次の行')
    # await asyncio.gather(task(3), task(1))  # これは同時に実行される
    task(2)  # awaitが付いていないから実行されない(箱だけ作ったイメージ)
    print(f"finished at {time.strftime('%X')}")

if __name__ == '__main__':
    # コルーチンを実行するにはrun()を使う
    asyncio.run(main())

