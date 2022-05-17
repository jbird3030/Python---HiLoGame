#Author: Jason McGee
#Date: 04.09.2021
#File Name: HiLoGame.py
#Description: Game to try to guess a random number

#!/usr/bin/env python3

#Imports a random integer
from random import randint

#Whether user wishes to continue playing
game = True

while game:
    #User sets highest number in the game
    max_number = int(input('What should the maximum number for this game be? '))

    #Computer selects its number between 1 and the max set by player
    computer_number = randint(1,max_number)

    #Condition determining if game continues
    guess = True

    #Results of the user's input
    while guess:
        player_guess = int(input('Guess my number: '))
        if player_guess > computer_number:
            print('Your guess is too high.')
        elif player_guess < computer_number:
            print('Your guess is too low.')
        else:
            guess = False
            print('You guessed my number!')

    #Player decides if they wish to pay again or not
    again = input('Do you wish to play again?  (Y/N) : ')
    if again.lower()=='n':
        print('Thank you for playing!')
        game = False
   

