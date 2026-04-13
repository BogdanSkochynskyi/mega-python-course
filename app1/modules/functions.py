TODOS_TXT = "todos.txt"

def get_todos(filepath=TODOS_TXT):
    """ Return a list of todos from a file. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(local_todos, filepath=TODOS_TXT):
    """ Write a list of todos to a file. """
    with open(filepath, "w") as local_file:
        local_file.writelines(local_todos)

# print(help(get_todos))