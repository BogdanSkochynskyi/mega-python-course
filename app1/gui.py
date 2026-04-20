import FreeSimpleGUI as sg

import modules.functions as functions
import time

sg.theme('DarkBlue')

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button(image_source="images/add.png", tooltip="Add a to-do", key="Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button(key="Complete", image_source="images/complete.png", tooltip="Complete a to-do")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
clock = sg.Text("", key="clock")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                       [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))  # Each list inside list is next line
while True:
    event, values = window.read(timeout=1000) # event = action element(button, listbox, etc) name, values = input data
    window['clock'].update(value=time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'])
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please, select an item first", font=('Helvetica', 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_complete)

                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todo'].update(value="")
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please, select an item first", font=('Helvetica', 20))
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
