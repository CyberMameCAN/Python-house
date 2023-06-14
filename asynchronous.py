"""
Python 3.7+ 
https://docs.python.org/ja/3/library/asyncio.html?highlight=asyncio#module-asyncio


- async def コルーチン関数を定義する
- asyncio   コルーチンを実行する

"""
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... Wirld!')


if __name__ == '__main__':
    asyncio.run(main())
