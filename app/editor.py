import json
from app.shapes import Point, Segment, Circle, Square, Rectangle, Oval


class Editor:

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def delete_shape(self, index):
        if 0 <= index < len(self.shapes):
            self.shapes.pop(index)

    def list_shapes(self):
        for i, shape in enumerate(self.shapes):
            print(f"{i}: {shape}")

    def save(self, filename):

        data = []

        for shape in self.shapes:

            if isinstance(shape, Point):
                data.append({"type": "point", "x": shape.x, "y": shape.y})

            elif isinstance(shape, Segment):
                data.append({
                    "type": "segment",
                    "x1": shape.x1,
                    "y1": shape.y1,
                    "x2": shape.x2,
                    "y2": shape.y2
                })

            elif isinstance(shape, Circle):
                data.append({"type": "circle", "x": shape.x, "y": shape.y, "r": shape.r})

            elif isinstance(shape, Square):
                data.append({"type": "square", "x": shape.x, "y": shape.y, "side": shape.side})

            elif isinstance(shape, Rectangle):
                data.append({
                    "type": "rectangle",
                    "x": shape.x,
                    "y": shape.y,
                    "width": shape.width,
                    "height": shape.height
                })

            elif isinstance(shape, Oval):
                data.append({
                    "type": "oval",
                    "x": shape.x,
                    "y": shape.y,
                    "rx": shape.rx,
                    "ry": shape.ry
                })

        with open(filename, "w") as f:
            json.dump(data, f)

    def load(self, filename):

        with open(filename) as f:
            data = json.load(f)

        self.shapes = []

        for item in data:

            t = item["type"]

            if t == "point":
                self.shapes.append(Point(item["x"], item["y"]))

            elif t == "segment":
                self.shapes.append(Segment(item["x1"], item["y1"], item["x2"], item["y2"]))

            elif t == "circle":
                self.shapes.append(Circle(item["x"], item["y"], item["r"]))

            elif t == "square":
                self.shapes.append(Square(item["x"], item["y"], item["side"]))

            elif t == "rectangle":
                self.shapes.append(Rectangle(item["x"], item["y"], item["width"], item["height"]))

            elif t == "oval":
                self.shapes.append(Oval(item["x"], item["y"], item["rx"], item["ry"]))