import pandas

def transcribe_user_input():
    user_input = input("Enter the word to transcribe: ").upper()
    try:
        new_code_list = [new_dict[char] for char in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        transcribe_user_input()
    else:
        print(new_code_list)


df = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index, row) in df.iterrows()}

transcribe_user_input()


