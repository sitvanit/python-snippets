# for loop
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
    print(breed)

########################################################################################################################
# using range in loop
promise = "I will not chew gum in class"

for i in range(5):
    print(promise)

########################################################################################################################
# break
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for breed in dog_breeds_available_for_adoption:
    print(breed)
    if breed == dog_breed_I_want:
        print("They have the dog I want!")
        break

########################################################################################################################
# continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
    if age < 21:
        continue
    print(age)

########################################################################################################################
# while
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
    students_in_poetry.append(all_students.pop())

########################################################################################################################
# nested loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  print(location)
  for flavor in location:
    scoops_sold += flavor

print(scoops_sold)

########################################################################################################################
# if inside a loop
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

########################################################################################################################
# convert all of the loop elements
celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [temperature * 9/5 +32 for temperature in celsius]
print(fahrenheit)
