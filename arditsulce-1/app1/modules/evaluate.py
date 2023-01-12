low_val = 0
high_val = 100
def evaluate_type(temp):
    result = ""
    temp = float(temp)
    if temp < 0:
        return "Solid"
    elif temp >= 100:
        return "Gas"
    elif low_val < temp < high_val:
        return "Liquid"
#    return result            