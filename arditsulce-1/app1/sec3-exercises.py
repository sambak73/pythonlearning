"""
while True:
    user_input = input("Enter the country:")
    user_input = user_input.upper()
    match user_input:
        case "USA":
            print("Hello")
        case "INDIA":
            print("Namaste")
        case "GERMANY":
            print("Hallo")
"""
ingredients = ["john smith", "sen plakay", "dora ngacely"]              
for item in ingredients:
    item = item.title()
    print(item)