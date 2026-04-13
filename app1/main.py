# from functions import get_todos, write_todos
import time

from modules import functions

print(time.strftime("Now is %d.%m.%Y %H:%M:%S", time.localtime()))

while True:
    user_action = input("Type add [Task], show, edit [number], complete [number] or exit: ")
    user_action = user_action.strip().lower()
    todos = []

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        # todos = get_todos(filepath=TODOS_TXT)
        # todos = get_todos(new_todos.txt)
        todos = functions.get_todos()

        todos.append(todo)

        # write_todos(filepath=TODOS_TXT, local_todos=todos)
        # write_todos(todos, "new_todos.txt")
        functions.write_todos(todos)

    elif user_action.startswith('show'):

        # new_todos = []
        # for item in todos:
        #     new_todos.append(item.strip('\n'))
        # Same:
        # new_todos = [item.strip('\n') for item in todos]
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            new_text = input(f"You want to edit {todos[int(number) - 1].strip('\n')} write new todo text ") + '\n'
            todos[number - 1] = new_text

            functions.write_todos(todos)
        except ValueError:
            print("Invalid input. Use number of task to edit.")
            continue
        except IndexError:
            print("Invalid index.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            completed_item = todos.pop(number - 1)

            functions.write_todos(todos)

            print(f"You completed {completed_item}")
        except ValueError:
            print("Invalid input. Use number of task to complete.")
            continue
        except IndexError:
            print("Invalid index.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid input")

print("Goodbye!")
