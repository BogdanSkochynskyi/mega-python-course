import FreeSimpleGUI as sg

from modules import functions

sg.theme('DarkBlue')

label1 = sg.Text("Enter feet:")
input_box1 = sg.InputText(key="feets")
label2 = sg.Text("Enter inches:")
input_box2 = sg.InputText(key="inches")
convert_button = sg.Button("Convert")
label3 = sg.Text(key='result')
exit_button = sg.Button("Exit")

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

window = sg.Window('Convertor',
                   layout=[[label1, input_box1], [label2, input_box2], [convert_button, exit_button, label3]],
                   font=('Helvetica', 20))


while True:
    event, values = window.read()
    match event:
        case "Convert":
            met = convert(float(values['feets']), float(values['inches']))
            window['result'].update(value=met)
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()