from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)
    first_number = float(input("What is the first number?: "))
    while True:
        for key in operations:
            print(key)
        selected_operator = input("Pick an operation: ")
        second_number = float(input("What is the next number?: "))
        answer = operations[selected_operator](first_number, second_number)
        print(f"{first_number} {selected_operator} {second_number} = {answer}")
        continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, anything else to exit: ").lower()
        if continue_calculating == "n":
            print("\n" *25)
            calculator()
        elif continue_calculating == "y":
            first_number = answer
        else:
            print("Goodbye")
            return False

calculator()
