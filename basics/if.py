def dave_check(user_name):
    if user_name == "Dave":
        return "Get off my computer Dave!"
    if user_name == "angela_catlady_87":
        return "I know it is you Dave! Go away!"


# Enter a user name here, make sure to make it a string
user_name = "Dave"

print(dave_check(user_name))


########################################################################################################################
def greater_than(x, y):
    if x > y:
        return x
    if x < y:
        return y

    return "These numbers are the same"


########################################################################################################################
def graduation_reqs(credits):
    if credits >= 120:
        return "You have enough credits to graduate!"


print(graduation_reqs(120))


########################################################################################################################
def graduation_reqs_with_and(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"


########################################################################################################################
def graduation_mailer(gpa, credits):
    if (credits >= 120) or (gpa >= 2.0):
        return True


########################################################################################################################
def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"
    if (gpa >= 2.0) and not (credits >= 120):
        return "You do not have enough credits to graduate."
    if not (gpa >= 2.0) and (credits >= 120):
        return "Your GPA is not high enough to graduate."
    else:
        return "You do not meet the GPA or the credit requirement for graduation."


########################################################################################################################
def grade_converter(gpa):
    if gpa >= 4.0:
        return "A"
    elif gpa >= 3.0:
        return "B"
    elif gpa >= 2.0:
        return "C"
    elif gpa >= 1.0:
        return "D"
    elif gpa >= 0.0:
        return "F"
