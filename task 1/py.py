def func(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "**":
        return num1 ** num2
    elif operator == "//":
        return num1 // num2
    elif operator == "/" and num1 % num2 > 0:
        return "error"
    elif operator == "/":
        return num1 / num2
print(func(int(input("enter num 1: ")), int(input("enter num 2: ")), input("enter operator: ")))