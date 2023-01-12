user_input = input("Enter a new password:")
if len(user_input) > 7:
    print(len(user_input))
    print("Great password there!")
elif len(user_input) == 7:
    print("Password is ok, but not too strong")   
else:
    print("Your password is weak")
    