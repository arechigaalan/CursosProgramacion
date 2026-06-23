with open('file1.txt') as file1:
    file1_list = file1.read().split('\n')

file1_list_int = [int(n) for n in file1_list if n]

with open('file2.txt') as file2:
    file2_list = file2.read().split('\n')

file2_list_int = [int(n) for n in file2_list if n]

result = [n for n in file1_list_int if n in file2_list_int]

print(file1_list_int)