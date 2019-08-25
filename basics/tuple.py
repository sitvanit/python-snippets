# Tuple is an immutable list - we cannot change, add or remove the elements or change the order
# It can by use as a list
my_info = ('Mike', 24, 'Programmer')

print(my_info[0])
# Mike
print(my_info[-1])
# Programmer

# Unpacking a tuple
name, age, occupation = my_info
print(name)
# Mike

# one element tuple must come with a comma
one_element_tuple = (4,)
print(one_element_tuple)
# (4,)
