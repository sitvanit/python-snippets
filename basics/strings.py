# multiple lines """""" or ''''''
to_you = """
Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
"""

print(to_you)

########################################################################################################################
# A string can be thought of as a list of characters.
# Like any other list, each character in a string has an index.
my_name = 'Sitvanit'
first_initial = my_name[0]

########################################################################################################################
# Operations on strings are creating an entirely new string.
# This is because strings are immutable. This means that we cannot change a string once it is created.

########################################################################################################################
# substring in string


def contains(big_string, little_string):
    return little_string in big_string


########################################################################################################################
# case
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author_fixed)

########################################################################################################################
# split
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya"
author_names = authors.split(',')
print(author_names)

########################################################################################################################
# join
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = " ".join(reapers_line_one_words)
print(reapers_line_one)

########################################################################################################################
# strip
# strip() - Stripping a string removes all whitespace characters from the beginning and end.
# strip(!) - Stripping a string removes all ! characters from the beginning and end.

########################################################################################################################
# replace
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, 
D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, 
North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of
 African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')

########################################################################################################################
# find
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find('disown')

########################################################################################################################
# format


def poem_title_card(poet, title):
    poem_desc = "The poem \"{}\" is written by {}".format(title, poet)
    return poem_desc


def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
    return poem_desc

