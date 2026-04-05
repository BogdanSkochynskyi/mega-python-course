while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()
    file = open("todos.txt", "r")
    todos = file.readlines()
    file.close()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case 'show' | 'display':

            # new_todos = []
            # for item in todos:
            #     new_todos.append(item.strip('\n'))
            # Same:
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}.{item}"
                print(row)
        case 'edit':
            number = int(input("Write a number of todo item to edit "))
            new_text = input(f"You want to edit {todos[int(number) - 1]}, write new todo text ")
            todos[number - 1] = new_text
        case 'complete':
            number = int(input("Write a number of todo item to complete "))
            completed_item = todos.pop(number - 1)
            print(f"You completed {completed_item}")
        case 'exit':
            break
        case _:
            print("Invalid input")

print("Goodbye!")
