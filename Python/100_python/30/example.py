
#! File not found.

# try:
#     file = open('a_file.txt')
#     a_dictionary = {'key':'value'}
#     print(a_dictionary['fadf'])
# except FileNotFoundError as file_error_message:
#     file = open('a_file.txt', 'w')
#     file.write('Hola')
# except KeyError as key_error_message:
#     print(f'The {key_error_message} does not exist.')
# else:
#     content = file.read()
#     # print(content)
# finally:
#     file.close()
#     print('File was close')

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Human height should not be over 3 meters.')

bmi = weight / (height ** 2)
print(bmi)
