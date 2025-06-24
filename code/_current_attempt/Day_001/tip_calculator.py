print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15 "))
number_of_people = int(input("How many people to split the bill? "))
individual_amount = ((tip_percentage/100 + 1) * bill)/number_of_people
print(f"Each person should pay: ${individual_amount}")
