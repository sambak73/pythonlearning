#1. length is 8 or grater
#2. atleast 1 number
#3. atleast 1 uppercase alphabet

user_input = input("Enter the password:")
result = []

if len(user_input) >= 8:
    result.append(True)
else:
    result.append(False) 

digit = False
for i in user_input:
    if i.isdigit():
        digit = True
result.append(digit)

upper = False
for i in user_input:
    if i.upper():
        upper = True
result.append(upper)
#print(result)
if all(result):
    print("Strong password")
else:
    print("Weak password")
        
           