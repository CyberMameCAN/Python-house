# メタクラスはtypeを継承する
class Singleton(type):
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print('singleton called.')
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# 以下テスト
class T(metaclass=Singleton):  # 定義時に呼び出せる
# class T:
    def __init__(self):
        print('init')


def main():
    test = T()
    test = T()
    test = T()


if __name__ == '__main__':
    main()