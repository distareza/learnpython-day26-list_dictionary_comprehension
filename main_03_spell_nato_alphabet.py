"""
    Tool for phonetic alphabet code generator
    Phonetic alphabets are used to indicate, through symbols or codes, what a speech sound or letter sounds like.
    The NATO Phonetic Alphabet is instead a spelling alphabet (also known as telephone alphabet, radio alphabet,
    word-spelling alphabet, or voice procedure alphabet).
"""
import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = { row.letter : row.code for (idx, row) in nato_dataframe.iterrows() }
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word :")
print([nato_dict[letter] for letter in word.upper()])
for c in word:
    word_spelling = nato_dict[c.upper()]
    print(f" {c} for {word_spelling}")