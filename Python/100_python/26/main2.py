 #! """Comprensión de diccionarios"""
import random

students = ['Alan', 'Alex', 'Beth', 'Caroline', 'Dave']

students_scors = {student:random.randint(1, 100) for student in students}

passed_students = {student:score for (student, score) in students_scors.items() if score >= 60}
print(students_scors)
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_list = sentence.split(' ')
len_words = [len(word) for word in words_list]
result = {word:len_words for word, len_words in zip(words_list, len_words)}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)
