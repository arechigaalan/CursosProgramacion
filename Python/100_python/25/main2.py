# import csv
# import pandas as pd

# # with open('./weather_data.csv') as weather:
# #     weather_list = weather.readlines()
# #     print(weather_list)

# # with open('./weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)


# data = pd.read_csv('./weather_data.csv')
# # print(data['temp'])

# #! Métodos de conversión
# data_dict = data.to_dict()
# list_temp = data['temp'].to_list()

# #! Métodos para cálculos
# mean_temp = data['temp'].mean()
# max_temp = data.temp.max()

# #! Obtener una fila
# print(data[data.day == 'Monday']) #! Obtiene la fila del lunes.
# print(data[data.temp == max_temp]) #! Obtener la fila que tiene la mayor temperatura.

# #! Filtrado de datos
# monday_data = data[data.day == 'Monday']
# monday_condition = monday_data.condition
# monday_temp = monday_data.temp
# monday_temp_fahren = ((monday_temp * 9) / 5) + 32
# print(monday_temp_fahren)

# #! Crear un dataframe from scratch

# students_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }

# data_students = pd.DataFrame(students_dict)
# data_students.to_csv('students_data.csv')

import pandas as pd

data = pd.read_csv('./Squirrel_Data.csv')
gray = data[data['Primary Fur Color'] == 'Gray'].count()['Primary Fur Color']
cinnamon = data[data['Primary Fur Color'] == 'Cinnamon'].count()['Primary Fur Color']
black = data[data['Primary Fur Color'] == 'Black'].count()['Primary Fur Color']

squirrel_count = {
    'Fur color': ['gray', 'cinnamon', 'black'],
    'Count': [gray, cinnamon, black]
}

squirrel_count_df = pd.DataFrame(squirrel_count)
squirrel_count_df.to_csv('squirrel_count.csv')
