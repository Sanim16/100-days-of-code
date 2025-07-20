PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names:
    list_of_names = [name.strip() for name in names.readlines()]

for name in list_of_names:
    # Open the file in read mode
    with open("Input/Letters/starting_letter.txt", "r") as file:
        content = file.read()

    # Perform modifications (replace text)
    modified_content = content.replace(PLACEHOLDER, name)

    # Create the file in write mode
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        file.write(modified_content)
