#Uses module argv from sys
from sys import argv  

#defining the arguments for argv
script, filename = argv

#Assigning opening a file to a variable
txt = open(filename)

#prints the file name to the user
print(f"Here's your file {filename}:")

#reads and prints the file that was opened
print(txt.read())

#Requesting any other file names
print("Type the filename again:")
file_again = input("> ")

#file requested is opened
txt_again = open(file_again)

#file requested is read and printed
print(txt_again.read())

