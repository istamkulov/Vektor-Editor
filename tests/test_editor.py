import unittest

from app.editor import VectorEditor


class TestVectorEditor(unittest.TestCase):

    def setUp(self):
        self.editor = VectorEditor()

    def test_create_point(self):

        result = self.editor.create_shape("point", ["1", "2"])

        self.assertEqual(result, "Shape created")

        self.assertEqual(len(self.editor.shapes), 1)

    def test_delete_shape(self):

        self.editor.create_shape("point", ["1", "2"])

        result = self.editor.delete_shape(0)

        self.assertEqual(result, "Shape deleted")

        self.assertEqual(len(self.editor.shapes), 0)

    def test_list_shapes(self):

        self.editor.create_shape("point", ["1", "2"])

        shapes = self.editor.list_shapes()

        self.assertEqual(len(shapes), 1)


if __name__ == "__main__":
    unittest.main()