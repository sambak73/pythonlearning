#todos = []
from modules import functions
from datetime import datetime
now =datetime.now()
dt = now.strftime("%d %b %Y")
print(dt)
while True:
    user_action = input("Type add (to add), show (to view) , edit (to edit), complete (to remove) or exit(exit app):")
    user_action = user_action.strip()
    if "add" in user_action:

        todos = functions.get_todos()
        
        todo = user_action[4:].title() + "\n"
        todos.append(todo)
        #print(todo)
        functions.write_todos(todos)  
    elif "show" in user_action:

        todos = functions.get_todos()
        
        for index, item in enumerate(todos):

            item = item.strip("\n")
            item = f"{index+1}.{item}"
            print(item)
                            
    elif "edit" in user_action:
        try:
            #edit_number = int(input("Enter the item number to edit:"))  
            edit_number = int(user_action[5:]) - 1  
            todos = functions.get_todos()
            new_todo = input("Enter the new todo item:")
            todos[edit_number] = new_todo + "\n"
            
            functions.write_todos(todos)    
        except IndexError:
            print("Check the todo item to edit")
            
    elif "complete" in user_action:
        try:
            #complete_number = int(input("Enter the number of completed todo item:"))
            complete_number = int(user_action[9:]) - 1
            
            todos = functions.get_todos()    
            todo_removed = todos[complete_number].strip("\n")   
            todos.pop(complete_number)      
            
            functions.write_todos(todos)    
            print(f"Selected todo {todo_removed} removed from the todos list")    
        except IndexError:
            print("Check the correct todo item to complete")    
             
    elif user_action == "exit":
        break    
    else:
        print("Command is not valid.")
print("Thank you for using this app, Bye!")        