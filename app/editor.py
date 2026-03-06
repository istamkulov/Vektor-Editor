from .shapes import Point, Segment, Circle, Square


class VectorEditor:

    def __init__(self):
        self.shapes = []

    def create_shape(self, shape_type: str, args):

        try:

            if shape_type == "point":
                x, y = map(int, args)
                shape = Point(x, y)

            elif shape_type == "segment":
                x1, y1, x2, y2 = map(int, args)
                shape = Segment(x1, y1, x2, y2)

            elif shape_type == "circle":
                x, y, r = map(int, args)
                shape = Circle(x, y, r)

            elif shape_type == "square":
                x, y, side = map(int, args)
                shape = Square(x, y, side)

            else:
                raise ValueError("Unknown shape")

            self.shapes.append(shape)

            return "Shape created"

        except Exception as e:
            return f"Error: {e}"

    def list_shapes(self):

        if not self.shapes:
            return ["No shapes"]

        return [f"{i+1}. {shape}" for i, shape in enumerate(self.shapes)]

    def delete_shape(self, index: int):

        if index < 0 or index >= len(self.shapes):
            return "Invalid index"

        del self.shapes[index]

        return "Shape deleted"