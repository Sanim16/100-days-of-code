print(r'''
*******************************************************************************
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
*******************************************************************************
''')

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10 12 15 "))
number_of_people = int(input("How many people to split the bill? "))
tip_as_percent = tip/100
total_amount = total_bill * (1 + tip_as_percent)
each_persons_bill = total_amount / number_of_people
payment = round(each_persons_bill, 2)
print(f"Each person should pay: ${payment}")
