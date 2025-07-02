import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1/n2

def multiply(n1, n2):
    return n1 * n2

calculator = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

while True:
    print(art.logo)
    first_number = float(input("Enter first number: "))
    continue_with_answer = True
    while continue_with_answer:
        for symbol in calculator:
            print(symbol)
        operation = input("Enter an operator: ")

        second_number = float(input("Enter second number: "))

        answer = calculator[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {answer}")
        continue_with_answer = input(f"Type 'Y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if continue_with_answer == "y":
            first_number = answer
        else:
            continue_with_answer = False
            print("\n" * 20)
