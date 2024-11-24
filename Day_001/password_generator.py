import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like in your password?\n"))
number_of_numbers = int(input("How many numbers would you like in your password?\n"))

password_components = []
for letter in range(0, number_of_letters):
    password_components.append(random.choice(letters))

for symbol in range(0, number_of_symbols):
    password_components.append(random.choice(symbols))

for number in range(0, number_of_numbers):
    password_components.append(random.choice(numbers))

print(password_components)
random.shuffle(password_components)
print(password_components)

password = ""
for p in password_components:
    password += p

print(password)
