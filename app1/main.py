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
            for index, list_item in enumerate(todos):
                print(f"{index + 1}.{list_item.strip()}")
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
