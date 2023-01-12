prompt = "Enter a todo:"
#i = 1
#while 5 > i:
#    user_text = input(prompt)
#    print("Todo %d entered is %s" %(i, user_text))
#    i+=1

todos = []

while True:
    todo = input(prompt)
    todos.append(todo)    
    print(todos)