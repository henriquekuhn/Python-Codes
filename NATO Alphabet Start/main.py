import os
import pandas

DIR = os.getcwd() + "/NATO Alphabet Start"
os.chdir(DIR)
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for index, row in data.iterrows()}
print(phonetic_dict)



def generate_phonetic():

    word = input("Enter a word: ").upper()
    
    try:
        phonetic_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only words in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()