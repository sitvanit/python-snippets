# A list is an ordered set of objects in Python.

########################################################################################################################
# A list can contain various data types
ints_and_strings = [1, 2, 3, 'four', 'five', 'any_string']

########################################################################################################################
# nested list
ages = [['Aaron', 15], ['Dhruti', 16]]

########################################################################################################################
# zip
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)

print(names_and_dogs_names)
# [('Jenny', 'Elphonse'), ('Alexus', 'Dr. Doggy DDS'), ('Sam', 'Carter'), ('Grace', 'Ralph')]
print(list_of_names_and_dogs_names)
# [('Jenny', 'Elphonse'), ('Alexus', 'Dr. Doggy DDS'), ('Sam', 'Carter'), ('Grace', 'Ralph')]


########################################################################################################################
# append
orders = ['daisies', 'periwinkle']

orders.append('tulips')
# ['daisies', 'periwinkle']
orders.append('roses')
# ['daisies', 'periwinkle', 'tulips', 'roses']
print(orders)

########################################################################################################################
# concat lists
orders1 = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']
new_orders = orders1 + ['lilac', 'iris']
broken_prices = [5, 3, 4, 5, 4] + [4]

########################################################################################################################
# range
print(range(8))
# [0, 1, 2, 3, 4, 5, 6, 7]
print(range(5, 15, 3))
# [5, 8, 11, 14]

########################################################################################################################
# len
list1 = range(2, 20, 2)
list1_len = len(list1)
print(list1_len)

########################################################################################################################
# index
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4 = employees[4]
# Selecting an element that does not exist produces an IndexError.

########################################################################################################################
# index from the end
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
last_element = shopping_list[-1]

########################################################################################################################
# sublist
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
beginning = suitcase[0:4]
print(beginning)
# we can omit the 0
start = suitcase[:3]
print(start)
# ['shirt', 'shirt', 'pants']
# if we like the last element we can use -
end = suitcase[-2:]
print(end)
# ['pajamas', 'books']

########################################################################################################################
# count
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake',
         'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')
print(jake_votes)

########################################################################################################################
# sort - sort the list
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

cities.sort()
print(cities)

########################################################################################################################
# sorted - return a variable of the sorted list

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games_sorted)
