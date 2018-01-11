formatter = "{} {} {} {}" # formatter is defined with four variables.

print(formatter.format(1,2,3,4)) #places the 1st variable in first {} , seperates the variables
print(formatter.format("one", "two", "three", "four")) #places the 1st string in the first{} , seperates the variables.

print(formatter.format(True, False, False, True)) #place the 1st boolean value in first{} , seperates the variables.

print(formatter.format(formatter, formatter, formatter, formatter)) #just prints formatter four times , used for concatenation.

print(formatter.format(
"Try your",
"Own text here",
"maybe a poem",
"or a song about fear"
)) # places the first string in first {} , used for concatenation. 