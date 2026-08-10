
#! File no found.
try:
    with open('file.txt') as file:
        file.read()
except FileNotFoundError:
    open('file.txt', 'w')
    file.write('Something')
