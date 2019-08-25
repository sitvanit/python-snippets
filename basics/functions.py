# The keyword def tells Python that we are defining a function.
# Everything that is indented after the : is what is run when greet_customer() is called.


def sing_song():
    print("You may say I'm a dreamer")
    print("But I'm not the only one")
    print("I hope some day you'll join us")
    print("And the world will be as one")


sing_song()


########################################################################################################################
def multi_x_add_y(number, x, y):
    print(number * x + y)


# positional arguments
multi_x_add_y(1, 3, 1)


########################################################################################################################
def greet_customer(grocery_store, special_item):
    print("Welcome to " + grocery_store + ".")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")


# keyword arguments
greet_customer(special_item="chips and salsa", grocery_store="Stu's Staples")


########################################################################################################################
def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit


low, high = get_boundaries(100, 20)


########################################################################################################################
def repeat_stuff(stuff, num_repeats=10):
    return stuff * num_repeats


lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)
print(song)
