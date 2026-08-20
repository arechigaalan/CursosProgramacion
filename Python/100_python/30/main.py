
#! File no found.
try:
    with open('file.txt') as file:
        file.read()
except FileNotFoundError:
    open('file.txt', 'w')
    file.write('Something')

#! KeyError
try: #? Código que podría ir lanzar un error.
    a_dictionary = {'key', 'value'}
    value = a_dictionary['non_existent_key']
except: #? Hacer esto si hubo error en lugar de terminar la ejecución.
    print('key don\'t exist. Error.')
else: #? Hacer esto si no hubo error.
    print('There wasn\'t an error.')
finally: #? Hacer esto independientemente de si hubo error o no.
    print('This allways is going to print.')
#! IndexError
try:
    fruit_list = ['Apple', 'Bannana', 'Pear']
    selected_fruit = fruit_list[3]
except:
    print('Fruit don\'t exist.')

#! TypeError
try:
    text = 'abc'
    print(text + 5)
except:
    print('TypeError')
