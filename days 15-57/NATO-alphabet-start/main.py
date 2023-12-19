
import pandas
df=pandas.read_csv("nato_phonetic_alphabet.csv")
lettersDataFrame=pandas.DataFrame(df)
#Loop through rows of a data frame
# for (index, row) in lettersDataFrame.iterrows():
#     print(index.code)
#     pass
letters_dict={row.letter:row.code for (index,row) in lettersDataFrame.iterrows()}
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
word=input("Enter a word\n").upper()
phonetic_code=[letters_dict[letter] for letter in word]
print(phonetic_code)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

