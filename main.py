"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Přichystal
email: Jiri.Prichystal@seznam.czalan
"""

import random
import time

# úvodní představení hry a vysvětlení pravidel
def welcome_message():
    print("**********")
    print("Hi player!")
    print("**********")
    print("I've generated a random 4 digit number for you. Let's play a bulls and cows game.")
    print("For each correctly guessed digit in the correct place you will get a 'bull', for the correct digit in the wrong place you will get a 'cow'.")
    print("**********")

welcome_message()

# generování a ověření náhodného čísla, které bude následně hádáno
def number_generating():
    digits = [str(i) for i in range(10)]
    
    while True:
        gen_num = random.sample(digits, 4)
        if gen_num[0] != "0":
            return "".join(gen_num)
        
# zadání hádaného čísla uživatelem a jeho kontrola s vygenerovaným číslem
def number_guessing():

    while True:
        gue_num = input("Guess number, please: ")

        if len(gue_num) != 4:
            print("Number must be 4 digits long.")
        elif gue_num.isdigit() == False:
            print("Number must be only digits.")
        elif gue_num[0] == "0":
            print("Number cannot start with 0.")
        elif len(set(gue_num)) != 4:
            print("Digits must be unique.")
        else:
            return gue_num
        
# vyhodnocení tipu uživatele - bull/cow
def evaluate_guess(gen_num, gue_num):
    bulls = 0
    cows = 0

    unmatched_gen_num = []
    unmatched_gue_num = []

    for i in range(4):
        if gen_num[i] == gue_num[i]:
            bulls = bulls + 1
        else:
            unmatched_gen_num.append(gen_num[i])
            unmatched_gue_num.append(gue_num[i])
    
    for digit in unmatched_gue_num:
        if digit in unmatched_gen_num:
            cows = cows + 1

    print(f"You have {bulls} bull{'s' if bulls != 1 else ''} and {cows} cow{'s' if cows != 1 else ''}.")
    return bulls, cows
    
# opakování tipů a vyhodnocení - pokračování ve hře + počítání času stráveného ve hře + nabídka nové hry
def game_playing():
    gen_num = number_generating()
    attempts = 0 # počítají se pouza validní pokusy
    start_time = time.time()

    while True:
        gue_num = number_guessing()
        bulls, cows = evaluate_guess(gen_num, gue_num)
        attempts = attempts + 1

        if bulls == 4:
            print(f"Congratulations! You find the secret number {gen_num} in {attempts} attempts.")
            break

    end_time = time.time()
    game_time = end_time - start_time
    minutes = int(game_time // 60)
    seconds = int(game_time % 60)

    print(f"Game time is {minutes} min and {seconds} sec")

while True: 
    game_playing()
    new_game = input("Do you want to play a new game? (y/n): ").lower()
    if new_game != "y":
        print("Thank you for playing and have a nice day!")
        break