todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for list_item in todos:
                    print(list_item)
        case 'exit':
            break
        case _:
            print("Invalid input")

print("Goodbye!")