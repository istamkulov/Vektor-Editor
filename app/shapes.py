class Shape:
    def __str__(self):
        return "Shape"


class Point(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Segment(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f"Segment(({self.x1},{self.y1}) -> ({self.x2},{self.y2}))"


class Circle(Shape):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return f"Circle(center=({self.x},{self.y}), r={self.r})"


class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def __str__(self):
        return f"Square(top-left=({self.x},{self.y}), side={self.side})"


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(({self.x},{self.y}), w={self.width}, h={self.height})"


class Oval(Shape):
    def __init__(self, x, y, rx, ry):
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry

    def __str__(self):
        return f"Oval(center=({self.x},{self.y}), rx={self.rx}, ry={self.ry})"