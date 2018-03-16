from sys import argv

script, filename = argv
print(f"We're going to erase {filename}.")
print("If you dont want that, hit C.")
print("If you do want that, hit RETURN.")

cmd = input("?")
if cmd == "c":
   print(f"Closing the file {filename}.")
else:
    print("Opening the file...")
    target = open(filename, 'w')
    print("Truncating the file. GOODBBYE!")
    target.truncate()

    print("Now I'm going to ask you three lines.")

    line1 = input("line 1 : ")
    line2 = input("line 2 : ")
    line3 = input("line 3 : ")

    cumlines = line1 + "\n" + line2 +"\n" + line3

    print("I'm going to write these to the file.")

    target.write(cumlines)

    print("And finally, we close it.")
    target.close()
