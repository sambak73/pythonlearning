'''
feet_inches = input("Enter the measurements:")

def parse_input(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}

def convert_feet_inches_to_meters(feet,inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

parsed = parse_input(feet_inches)

result = convert_feet_inches_to_meters(parsed['feet'],parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Not eligible")
else:
    print("Eligible")    
'''
'''
year_of_birth = int(input("Enter your year of birth:"))


def calculate_age(birth_year,current_year=2023):
    age = current_year - birth_year
    return age

result_age = calculate_age(year_of_birth)
if result_age > 120:
    print("You should be one of oldest to be alive, contact Guinness")
else:
    print("Congratulations for long life")    
'''

names = input("Enter names separated by a comma:")


def get_names(names):
    name = names.split(",")
    return len(name)

print(f"The number of names entered is {get_names(names)}")