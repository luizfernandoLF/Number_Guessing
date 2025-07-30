import random

print(
"+------------------------------------------------------------------------------------------------------------------+\n"  
"| Welcome to the Number Guessing Game!                                                                             |\n" \
"| The game rules are:                                                                                              |\n" \
"| The computer will randomly randomly of a number between 1 and 100                                                |\n" \
"| you should guess what that number is                                                                             |\n" \
"| this game has a difficulty selector, which represents the number of chances you have to make the right guess     |\n" \
"| Easy - 10 chances                                                                                                |\n" \
"| Medium - 5 chances                                                                                               |\n" \
"| Hard - 3 chances                                                                                                 |\n" \
"| By: Luiz Fernando. github: https://github.com/luizfernandoLF                                                     |\n"    
"+------------------------------------------------------------------------------------------------------------------+"
)

global_chances_easy = 10
global_chances_medium = 5
global_chances_hard = 3


computer_choice = random.randint(1, 100)

user_difficult = input("Choose the difficult: ")

while user_difficult.capitalize() not in {"Easy", "Medium", "Hard"}:
    user_difficult = input("Sorry, i don't know this difficult, try again: ")
    if user_difficult.capitalize() not in {"Easy", "Medium", "Hard"}:
        print("Invalid Choice, try again: ")
print(f'Ok, you chose {user_difficult.capitalize()}\n')



if user_difficult.capitalize() == 'Easy':
    global_chances_easy=10
    user_guess = int(input("Now, make your guess, what number do you think the computer has in mind?: "))


    while user_guess < 1 or user_guess > 100:
        if user_guess < 1 or user_guess > 100:
            user_guess = int(input("Sorry, this number is out of range (1 - 100). Try again: "))
            
    global_chances_easy-=1
    #in case the user chose the right number in the first attempt
    if computer_choice == user_guess:
        print("Congrats, you won")
        exit()
    else:
        while computer_choice != user_guess:
            user_guess = int(input("Wrong number, try again: "))
            global_chances_easy-=1
            if computer_choice == user_guess:
                print("Congrats, you won")
                print(f'chances remaining {global_chances_easy}')
                exit()

            if global_chances_easy == 0:
                print("Sorry, better luck next time :)")
                exit()

   
            


if user_difficult.capitalize() == 'Medium':
    global_chances_medium=5
    user_guess = int(input("Now, do your guess, what number you think the computer thought?: "))


    while user_guess < 1 or user_guess > 100:
        if user_guess < 1 or user_guess > 100:
            user_guess = int(input("Sorry, this number is out of range (1 - 100). Try again: "))
            
    global_chances_medium-=1
    #in case the user chose the right number in the first attempt
    if computer_choice == user_guess:
        print("Congrats, you won")
        exit()
    else:
        while computer_choice != user_guess:
            user_guess = int(input("Wrong number, try again: "))
            global_chances_medium-=1
            if computer_choice == user_guess:
                print("Congrats, you won")
                print(f'chances remaining {global_chances_medium}')
                exit()

            if global_chances_medium == 0:
                print("Sorry, better luck next time :)")
                exit()



if user_difficult.capitalize() == 'Hard':
    global_chances_medium=3
    user_guess = int(input("Now, do your guess, what number you think the computer thought?: "))


    while user_guess < 1 or user_guess > 100:
        if user_guess < 1 or user_guess > 100:
            user_guess = int(input("Sorry, this number is out of range (1 - 100). Try again: "))
            
    global_chances_medium-=1
    #in case the user chose the right number in the first attempt
    if computer_choice == user_guess:
        print("Congrats, you won")
        exit()
    else:
        while computer_choice != user_guess:
            user_guess = int(input("Wrong number, try again: "))
            global_chances_medium-=1
            if computer_choice == user_guess:
                print("Congrats, you won")
                print(f'chances remaining {global_chances_medium}')
                exit()

            if global_chances_medium == 0:
                print("Sorry, better luck next time :)")
                exit()

 





        


