def add(numbers):
    return sum(numbers)

def subtract(numbers):
    return numbers[0] - sum(numbers[1:])

def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

def divide(numbers):
    try:
     result = numbers[0]
     for n in numbers[1:]:
        result /= n
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    return result

while True:
    try:
        print("\nSimple basics CLI Calculator")
        operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")
        if operation.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if operation not in ('+', '-', '*', '/'):
            print("Invalid operation. Please try again.")
            continue
        numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
        if len(numbers) < 2:
            print("Please enter at least two numbers.")
            continue

        if operation == '+':
            result=add(numbers)
        elif operation == '-':
            result=subtract(numbers)
        elif operation == '*':
            result=multiply(numbers)
        elif operation == '/':
            result=divide(numbers)

        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numbers only.")
