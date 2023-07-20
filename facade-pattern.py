"""
Facade Design Pattern
所謂、窓口(facade)を作るパターン
ファクトリーメソッドとは似て非なるデザイン
"""

class SubClassA:
    def method(self):
        return 'A'


class SubClassB:
    def method(self):
        return 'B'


class SubClassC:
    def method(self):
        return 'C'


class Facade:
    def __init__(self):
        print('Facade pattern dojo.')
        print('-' * 20)
        
        self.sub_class_a = SubClassA()
        self.sub_class_b = SubClassB()
        self.sub_class_c = SubClassC()


    def create(self):
        result_a = self.sub_class_a.method()
        result_b = self.sub_class_b.method()
        result_c = self.sub_class_c.method()
        
        print(result_a, result_b, result_c)


def main():
    facade = Facade()
    facade.create()

if __name__ == '__main__':
    main()
    
