# A dictionary is an unordered set of key: value pairs
# the keys must always be unchangeable, hashable data types, like numbers or strings.
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}

########################################################################################################################
# Add key
animals_in_zoo = {}
animals_in_zoo['zebras'] = 8
animals_in_zoo['monkeys'] = 12
animals_in_zoo['dinosaurs'] = 0
print(animals_in_zoo)

########################################################################################################################
# Add multiple keys
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

########################################################################################################################
# Overwrite Values
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone",
                 "Animated Feature": "Zootopia"}
oscar_winners["Best Picture"] = "Moonlight"

########################################################################################################################
# List Comprehensions to Dictionaries
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}

########################################################################################################################
# key error
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120, "matcha": 30}

try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Unknown Caffeine Level")

combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
#print(combo_meals[3])
# KeyError

########################################################################################################################
# .get()
# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using.
# If the key you are trying to .get() does not exist, it will return None by default
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# 100000 as a default value if the user doesnt exist
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

########################################################################################################################
# .pop()
# .pop() works to delete items from a dictionary, when you know the key value.

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains")
# If the key does not exist, add 0
health_points += available_items.pop("power stew", 0)

########################################################################################################################
# get all keys
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()

########################################################################################################################
# get all values
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0

for value in num_exercises.values():
    total_exercises += value

########################################################################################################################
# get all items
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for key, value in pct_women_in_occupation.items():
    print("Women make up " + str(value) + " percent of " + key + "s.")

########################################################################################################################
# key in dictionary

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
print(12 in inventory)
# False
print("iron spear" in inventory)
# True

########################################################################################################################
# for on dictionary will get automatically just the keys
oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

for element in oscars:
    print(element)

# Best Actor
# Best Picture
# Animated Feature
# Best Actress
