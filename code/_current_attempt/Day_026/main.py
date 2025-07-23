import pandas

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {
    row.letter:row.code for (index, row) in df.iterrows()
}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter the word to transcribe: ").upper()

new_code_list = [
    new_dict[char] for char in user_input
]
print(new_code_list)
