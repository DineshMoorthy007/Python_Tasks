def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "Error: Division by zero"
    elif operator == '%':
        return a % b if b != 0 else "Error: Modulo by zero"
    else:
        return "Invalid operator"

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter an operator (+, -, *, /, %): ").strip()
    result = calculate(num1, num2, op)
    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter numeric values.")