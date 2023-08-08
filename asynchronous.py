"""
Python 3.7+ 
https://docs.python.org/ja/3/library/asyncio.html?highlight=asyncio#module-asyncio

並列処理の時に使う。
いったん処理を中断した後、続きから処理を再開する。

- async def コルーチン関数を定義する
- asyncio   コルーチンを実行する

"""
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')


if __name__ == '__main__':
    asyncio.run(main())
