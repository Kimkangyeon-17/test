"""
도형을 나타내는 클래스 시스템을 만드세요.
Shape 클래스: 기본 도형 클래스 (색상 속성)
Rectangle 클래스: Shape 상속, 가로/세로 길이로 면적 계산
Triangle 클래스: Shape 상속, 밑변/높이로 면적 계산

각 도형의 면적을 계산하고 색상과 함께 정보를 출력하세요.

테스트 코드:
rect = Rectangle("빨강", 5, 3)
tri = Triangle("파랑", 4, 6)
rect.display_info()
tri.display_info()
"""

class Shape():
    def __init__(self, color):
        self.color = color
    
    def get_area(self):
        pass

    def display_info(self):
        print(f"도형 색상 : {self.color}")
        print(f"도형 면적 : {self.get_area()}")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        Shape.__init__(self, color)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
class Triangle(Shape):
    def __init__(self, color, base, height):
        Shape.__init__(self, color)
        self.base = base
        self.height = height

    def get_area(self):
        return (self.base * self.height) / 2
    
rect = Rectangle("빨강", 5, 3)
tri = Triangle("파랑", 4, 6)
rect.display_info()
tri.display_info()