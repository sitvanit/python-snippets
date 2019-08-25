# with
# with keyword invokes something called a context manager for the file that we are calling open() on. This context
# manager takes care of opening the file when we call open() and then closing the file after we leave the indented
# block.
# Why is closing the file so complicated? Well, most other aspects of our code deal with things that Python itself
# controls. All the variables you create integers, lists, dictionaries. these are all Python objects, and Python knows
# how to clean them up when it is done with them. Since your files exist outside your Python script, we need to tell
# Python when we are done with them so that it can close the connection to that file. Leaving a file connection open
# unnecessarily can affect performance or impact other programs on your computer that might be trying to access that
# file.
# The with syntax replaces older ways to access files where you need to call .close() on the file object manually.
# We can still open up a file and append to it with the old syntax, as long as we remember to close the file connection
# afterwards.

########################################################################################################################

# read file
with open('welcome.txt') as text_file:
    text_data = text_file.read()
    print(text_data)

########################################################################################################################
# read lines
with open('how_many_lines.txt') as lines_doc:
    for line in lines_doc.readlines():
        print(line)

########################################################################################################################
# read line
with open('how_many_lines.txt') as lines_doc:
    first_line = lines_doc.readline()
    print(first_line)

########################################################################################################################
# write file
# It turns out that our open() function that we are using to open a file to read needs another argument to open a file
# to write to.

# write and override the file
with open('welcome.txt', 'w') as text_file:
    text_file.write('bye bye bye')

# write and append it to the file
with open('welcome.txt', 'a') as text_file:
    text_file.write('\nwelcome')

########################################################################################################################
# open and close the file in the old way (instead of with)
text_file = open('welcome.txt', 'a')
# We can now append a line to "fun_cities".
text_file.write("bye bye bye")
# But we need to remember to close the file
text_file.close()

########################################################################################################################
# CSV files
# Text files are not the only thing that Python can read, but they are the only thing that we do not any need additional
# parsing library to understand. CSV files are an example of a text file that impose a structure to their data. CSV
# stands for Comma-Separated Values and CSV files are usually the way that data from spreadsheet software (like
# Microsoft Excel or Google Sheets) is exported into a portable format. CSV files are just plain text files
with open('csv_file.csv') as log_csv_file:
    print(log_csv_file.readlines())

# there is a csv module in order to read it properly

########################################################################################################################
# read json file
import json

with open('message.json') as message_json:
    message = json.load(message_json)
    print(message['text'])

# write json file
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

with open('data.json', 'w') as data_json:
    json.dump(data_payload, data_json)
