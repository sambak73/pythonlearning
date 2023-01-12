'''
def get_max():
    grades = [9.6, 9.2, 9.7]
    high_grade = max(grades)
    less_grade = min(grades)
    message = f"Max: {high_grade}, Min: {less_grade}"
    return message

max_grade = get_max()
print(max_grade)
'''
def prepare(text):
    text = text.title()
    text = text.strip()
    return text
    
print(prepare("hello    "))