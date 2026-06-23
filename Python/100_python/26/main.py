 #! """ Comprensión de listas en Python"""

numbers = [1, 2, 3]
numbrers_plus_one = [number + 1 for number in numbers]
print(numbrers_plus_one)
numbers2 = [n * 2 for n in range(1, 5)]
print(numbers2)
names = ['Alex', 'Beth', 'Alan', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
longs_names = [name.upper() for name in names if len(name) >= 5]
print(longs_names)