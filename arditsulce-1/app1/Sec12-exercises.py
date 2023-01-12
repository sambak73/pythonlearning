'''
liters = float(input("Enter liter value:"))

def convert_liter_to_cubic(liters):
    liters_to_cubics = liters * 1000
    return liters_to_cubics

result = convert_liter_to_cubic(liters)
print(result)
'''

password = input("Enter the password:")

def password_check(password):
    password_chk = []
    case_upper = False
    digit = False
    if len(password) >= 8:
        password_chk.append(True)
    else:
        password_chk.append(False)    
    case_upper = [c.isupper() for c in password if c == c.upper()]   
    password_chk.append(case_upper)
    #print(case_upper)
    digit = [c.isdigit() for c in password if c == c.isdigit()]
    #password_chk.append(digit)
    #print(digit)
    #print(password_chk[2])
    if all(password_chk):
        return f"The password is strong"
    else:
        return f"The password is weak"  

result = password_check(password)  
print(result)  