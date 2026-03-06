from .editor import VectorEditor


def run_cli():

    editor = VectorEditor()

    while True:

        command = input("> ").strip()

        if not command:
            continue

        parts = command.split()

        action = parts[0]

        if action == "create":

            shape_type = parts[1]
            args = parts[2:]

            result = editor.create_shape(shape_type, args)

            print(result)

        elif action == "list":

            for item in editor.list_shapes():
                print(item)

        elif action == "delete":

            index = int(parts[1]) - 1

            print(editor.delete_shape(index))

        elif action == "exit":

            print("Bye!")
            break

        else:

            print("Unknown command")