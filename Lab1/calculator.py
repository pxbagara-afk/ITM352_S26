def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_operation():
    ops = {'+', '-', '*', '/'}
    while True:
        op = input("Choose operation (+, -, *, /): ").strip()
        if op in ops:
            return op
        print("Invalid operation. Choose +, -, *, or /.")


def calculate(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


def main():
    print("Simple calculator")
    while True:
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        op = get_operation()
        try:
            result = calculate(a, b, op)
        except ZeroDivisionError:
            print("Error: division by zero.")
        else:
            print(f"Result: {a} {op} {b} = {result}")
        again = input("Perform another calculation? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye.")
            break


if __name__ == '__main__':
    main()
