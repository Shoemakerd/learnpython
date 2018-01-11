tabby_cat = "\tI'm tabbed in." #\t used for inserting a tab.
persian_cat = "I'msplit\non a line."#\n is used to insert a new line.
backslash_cat = "I'm \\ a \\ cat." #\\ is used to insert a slash 

fat_cat = """
I'll do a list.
\t* Cat food        
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat) #prints the string after tab insertion.
print(persian_cat) #prints the string by inserting a new line when \n is found.
print(backslash_cat) #print the string with using a escape sequence to print a slash.
print(fat_cat) #prints the string with insertion of new tab or new line where necessary.