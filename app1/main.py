while True:
    user_action = input("Type add [Task], show, edit [number], complete [number] or exit: ")
    user_action = user_action.strip().lower()
    todos = []

    if 'add' in user_action:
        todo = user_action[4:] + '\n'

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif 'show' in user_action:

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
    elif 'edit' in user_action:
        number = int(user_action[5:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_text = input(f"You want to edit {todos[int(number) - 1].strip('\n')} write new todo text ") + '\n'
        todos[number - 1] = new_text

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        completed_item = todos.pop(number - 1)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        print(f"You completed {completed_item}")
    elif 'exit' in user_action:
        break
    else:
        print("Invalid input")

print("Goodbye!")
