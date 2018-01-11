# This is a game of python
from random import randint
elements = ['Rock', 'Paper', 'Python']
computer_choice = elements[randint(0,2)]
user_choice = raw_input("Enter Rock, Paper or Python:\n")

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'Rock' and computer_choice == 'Python':
    print("Win", user_choice, "covers", computer_choice)
elif user_choice == 'Paper' and computer_choice == 'Rock':
    print("Win", user_choice, "covers", computer_choice)
elif user_choice == 'Python' and computer_choice == 'Paper':
    print("Win", user_choice, "covers", computer_choice)
else:
    print('You lose :( Computer wins :D')