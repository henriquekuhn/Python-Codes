#word_list = ["what", "is", "the", "Airspeed", "velocity", "of", "an", "Unladen", "Swallow?"]
word_list = input("Enter a sentence: ").split()
word_dict = {word:len(word) for word in word_list}
print(word_dict) 

temp_c_dict = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14
    }

temp_f_dict = {key:(value*9/5)+32 for key, value in temp_c_dict.items()}
print(temp_f_dict)