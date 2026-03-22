todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for list_item in todos:
                print(list_item)
        case 'edit':
            number = int(input("Write a number of todo item to edit "))
            new_text = input(f"You want to edit {todos[int(number) - 1]}, write new todo text ")
            todos[number - 1] = new_text
        case 'exit':
            break
        case _:
            print("Invalid input")

print("Goodbye!")
