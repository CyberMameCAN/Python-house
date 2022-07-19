from concurrent.futures import ThreadPoolExecutor  # 並列処理(マルチスレッド)
#from concurrent.futures import ProcessPoolExecutor  # 並行処理(マルチプロセス)
import time

def func_1(x):
    for n in range(3):
        time.sleep(2)
        print(f'func_1 - {n} ({x})')

    return '結果1'

def func_2(x, y):
    for n in range(3):
        time.sleep(1)
        print(f'func_2 - {n} ({x}, {y})')

def main():
    print('開始')
    with ThreadPoolExecutor(max_workers=2) as executor:
        # 逐次処理
        back_to_the = executor.submit(func_1, 'あ')
        executor.submit(func_2, 'ウィニング', 'チケット')

        ## 複数にする時は以下の使い方もある
        # 
        # executor.map(func_1, ['A', 'B', 'C', 'D'])
        # 返り値がある場合はwithを抜けた後に list(返り値) で取得する

    rtn = back_to_the.result()  # futureクラスのresultメソッドで返り値を取得
    print(f'返って来たのは {rtn}')

    print('終了')

if __name__ == '__main__':
    main()