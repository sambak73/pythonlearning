'''
filenames = ['document', 'report', 'presentation']
for index, file in enumerate(filenames):
    filename = file.title()
    filename = f"{index}-{filename}.txt"
    print(filename)
'''
'''
ips = ['100.122.133.105', '100.122.133.111']
user_input = int(input("Enter the index:"))
return_value = f"You chose {ips[user_input]}"
print(return_value)
'''
'''
menu = ["pasta", "pizza", "salad"]
 
for i, j in enumerate(menu):
    print(f"{i}.{j}")
'''   
menu = ["pasta", "pizza", "salad"]
 
for i, j in enumerate(menu):
    print("f{i}.{j}")