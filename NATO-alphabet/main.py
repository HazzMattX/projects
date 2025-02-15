import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass
student_data_frame = pandas.DataFrame(student_dict)
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass
# Keyword Method with iterrows()
#TODO 1. Create a dictionary in this format:

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Error. Does not compute. Only letters are valid")
    else:
        print(output_list)
generate_phonetic()