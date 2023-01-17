from modules import functions
import PySimpleGUI as psg
psg.theme(None)
lbl_enter_todo = psg.Text("Enter the ToDo:")
txt_enter_todo = psg.InputText(tooltip="Enter ToDo",key="todo")
btn_add = psg.Button("Add")
btn_cancel = psg.Button("Cancel")
lbx_todos = psg.Listbox(['',''],key='lb',no_scrollbar = True, s=(45,10))
btn_edit = psg.Button("Edit")
space = " "
space = space*26
lbl_space = psg.Text(space)
layout = [[lbl_enter_todo,txt_enter_todo,btn_add,btn_cancel],[lbl_space,lbx_todos,btn_edit]]

window = psg.Window('ToDo App', layout=[layout],font=('Helvetica',12))

while True:
    event, values = window.read()
    psg.Popup(event)
    #window["lb"].update(values=functions.get_todos())
    match event:
        case "Cancel":
            break
        case "Add":
            todos = functions.get_todos()
            todo = values['todo'] + '\n'
            todos.append(todo)
            functions.write_todos(todos) 
            #psg.Listbox([todo],no_scrollbar = True, s=(46,10)) 
            window["lb"].update(values=todos)
        case "Edit":
           psg.Popup(values["lb"]) 
           window["todo"].update(values="")
           window["todo"].text(values=values["lb"])    
window.close()
