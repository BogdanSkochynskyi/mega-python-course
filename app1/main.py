while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()
    todos = []

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case 'show' | 'display':

            # new_todos = []
            # for item in todos:
            #     new_todos.append(item.strip('\n'))
            # Same:
            # new_todos = [item.strip('\n') for item in todos]
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}.{item}"
                print(row)
        case 'edit':
            number = int(input("Write a number of todo item to edit "))

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_text = input(f"You want to edit {todos[int(number) - 1].strip('\n')} write new todo text ") + '\n'
            todos[number - 1] = new_text

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Write a number of todo item to complete "))

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            completed_item = todos.pop(number - 1)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            print(f"You completed {completed_item}")
        case 'exit':
            break
        case _:
            print("Invalid input")

print("Goodbye!")
