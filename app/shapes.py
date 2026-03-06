class Shape:
    def __str__(self):
        return "Shape"


class Point(Shape):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Segment(Shape):

    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f"Segment(({self.x1},{self.y1}) -> ({self.x2},{self.y2}))"


class Circle(Shape):

    def __init__(self, x: int, y: int, r: int):
        if r <= 0:
            raise ValueError("Radius must be positive")

        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return f"Circle(center=({self.x},{self.y}), r={self.r})"


class Square(Shape):

    def __init__(self, x: int, y: int, side: int):

        if side <= 0:
            raise ValueError("Side must be positive")

        self.x = x
        self.y = y
        self.side = side

    def __str__(self):
        return f"Square(top-left=({self.x},{self.y}), side={self.side})"