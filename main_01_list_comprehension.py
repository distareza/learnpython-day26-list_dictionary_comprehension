"""
    List Comprehension - is a list created from previous list
    syntax:
    [ new_list for item in list if condition ]

"""
numbers = [1, 2, 3]

print([n + 1 for n in numbers])
# will print out : [2, 3, 4]

print([n * n for n in numbers])
# will print out : [1, 4, 9]

name = "Angela"
print([letter for letter in name])
# will print out : ['A', 'n', 'g', 'e', 'l', 'a']

print([n * 2 for n in range(1, 5)])
# range(1, 5) = [1, 2, 3, 4]
# will print out : [2, 4, 6, 8]

# Conditional List Comprehension
names = ['Alex', "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
print([name for name in names if len(name) < 5])
# will printout : ['Alex', 'Beth', 'Dave']

print([name.upper() for name in names if len(name) > 5])
# will print out : ['CAROLINE', 'ELANOR', 'FREDDIE']

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
square_number = [n*n for n in numbers]
print(square_number)
even_number = [n for n in numbers if n % 2 == 0]
print(even_number)

# create a list called result which contains the numbers that are common in both files.
list_1 = []
with open("file1.txt") as file_1:
    list_1 = [int(n.strip()) for n in file_1.readlines()]
list_2 = []
with open("file2.txt") as file_2:
    list_2 = [int(n.strip()) for n in file_2.readlines()]
print(list_1)
print(list_2)
print([n for n in list_1 if n in list_2])

