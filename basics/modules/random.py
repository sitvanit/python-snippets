import random

random_list = []
for i in range(101):
    random_list.append(random.randint(1, 100))

random_number = random.choice(random_list)
print(random_number)
