class CallBackTest:

    def handler(self, func, *args):
        """コールバック関数を呼び出す関数を定義"""
        return func(*args)

    def say_hello(self, name):
        """コールバック関数を定義"""
        print("Hello.", name)

def main():
    cb = CallBackTest()

    """関数名に()を付けないことで関数ポインタになる。"""  
    callback = cb.say_hello
    cb.handler(callback, 'good morning.')

if __name__ == '__main__':
    main()