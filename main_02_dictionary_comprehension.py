"""
    Dictionary Comprehension - is a dictionary created from value in a list or from existing dictionary
    syntax:
    new_dict = {new_key:new_value for item in list}
    new_dict = {new_key:new_value for (key, value) in dict.items()}
"""
import random

names = ['Alex', "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
random_score = {name: random.randrange(1, 100) for name in names}
print(random_score)
# will print out : {'Alex': 79, 'Beth': 16, 'Caroline': 16, 'Dave': 99, 'Elanor': 71, 'Freddie': 62} *) random value

pass_people = {people: score for (people, score) in random_score.items() if score > 60}
print(pass_people)
# will print out : {'Alex': 79, 'Dave': 99, 'Elanor': 71, 'Freddie': 62}

"""
Challenges : create a dictionary called result that takes each word in the given sentence 
            and calculates the number of letters in each word.
Hints : https://www.w3schools.com/python/ref_string_split.asp
"""
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)
# will print out : {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7,
# 'Swallow?': 8}


"""
Challenges : Use Dictionary Comprehension to create a dictionary called weather_f that 
            takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
hint : To convert temp_c into temp_f
       temp_f = (temp_c * 9/5) + 32 
"""
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
# will printout : {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday':
# 71.6, 'Sunday': 75.2}

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# Loop through dictionary
for (key, value) in student_dict.items():
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# Loop through DataFrame
for (key, value) in student_data_frame.items():
    print(value)
#Loop through rows of DataFrame
for (indx, row) in student_data_frame.iterrows():
    print(indx)
for (indx, row) in student_data_frame.iterrows():
    print(row)
for (indx, row) in student_data_frame.iterrows():
    print(row.student)
for (indx, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)




