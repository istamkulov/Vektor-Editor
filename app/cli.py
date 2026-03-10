from app.editor import Editor
from app.shapes import *


def run_cli():

    editor = Editor()

    while True:

        command = input(">> ").split()

        if not command:
            continue

        if command[0] == "create":

            shape = command[1]

            if shape == "point":
                editor.add_shape(Point(int(command[2]), int(command[3])))

            elif shape == "segment":
                editor.add_shape(Segment(int(command[2]), int(command[3]),
                                         int(command[4]), int(command[5])))

            elif shape == "circle":
                editor.add_shape(Circle(int(command[2]), int(command[3]), int(command[4])))

            elif shape == "square":
                editor.add_shape(Square(int(command[2]), int(command[3]), int(command[4])))

            elif shape == "rectangle":
                editor.add_shape(Rectangle(int(command[2]), int(command[3]),
                                           int(command[4]), int(command[5])))

            elif shape == "oval":
                editor.add_shape(Oval(int(command[2]), int(command[3]),
                                      int(command[4]), int(command[5])))

        elif command[0] == "list":
            editor.list_shapes()

        elif command[0] == "delete":
            editor.delete_shape(int(command[1]))

        elif command[0] == "save":
            editor.save(command[1])

        elif command[0] == "load":
            editor.load(command[1])

        elif command[0] == "help":

            print("""
Commands:

create point x y
create segment x1 y1 x2 y2
create circle x y r
create square x y side
create rectangle x y width height
create oval x y rx ry

list
delete index

save filename
load filename

exit
""")

        elif command[0] == "exit":
            break