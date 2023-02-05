"""
ファクトリーメッソッド 特徴
  - インスタンスの作り方をスーパークラス側で定める
  - 具体的なクラス名までは定めない
  - 具体的な肉付けは、全てサブクラス側で行う
"""

class Shape:
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        print("Circle.draw")

class Square(Shape):
    def draw(self):
        print("Square.draw")

class Triangle(Shape):
    def draw(self):
        print("Triangle.draw")

class ShapeFactory:
    @classmethod
    def create_shape(cls, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        elif shape_type == "triangle":
            return Triangle()
    """
      @classmethod
        clsが慣例
        class method は self ではアクセスできない
        インスタンス化せずに呼び出し可能
    """

def main():
    shape1 = ShapeFactory.create_shape("circle")
    shape1.draw()

    shape2 = ShapeFactory.create_shape("square")
    shape2.draw()

    shape3 = ShapeFactory.create_shape("triangle")
    shape3.draw()

if __name__ == "__main__":
    main()
