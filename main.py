"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Přichystal
email: Jiri.Prichystal@seznam.czalan
"""

import random
import time


DIGIT_COUNT = 4

def welcome_message() -> None:
    """
    Welcome message for users and game information.
    """
    print(
        "**********\n"
        "Hi player!\n"
        "**********\n"
        f"I've generated a random {DIGIT_COUNT} digit number for you.\n"
        "Let's play a bulls and cows game.\n"
        "For each correctly guessed digit in the correct place you will get a 'bull',\n"
        "for the correct digit in the wrong place you will get a 'cow'.\n"
        "**********"
        )

welcome_message()


def number_generating() -> str:
    """
    Generating a random number so that the first digit is not 0.
    """
    digits = [str(i) for i in range(10)]
    random.shuffle(digits)
    if digits[0] == "0": # if the first digit is zero, it is swapped with the second digit
        digits[0], digits[1] = digits[1], digits[0] 
    return "".join(digits[:DIGIT_COUNT])
    

def number_guessing() -> str:
    """
    Requesting the user to enter a number and verify its correctness.
    """
    while True:
        gue_num = input("Guess number, please: ")

        if len(gue_num) != DIGIT_COUNT:
            print(f"Number must be {DIGIT_COUNT} digits long.")
        elif not gue_num.isdigit():
            print("Number must be only digits.")
        elif gue_num[0] == "0":
            print("Number cannot start with 0.")
        elif len(set(gue_num)) != DIGIT_COUNT:
            print("Digits must be unique.")
        else:
            return gue_num
        

def evaluate_guess(gen_num: str, gue_num: str) -> tuple[int, int]:
    """
    Evaluating the user's tip, comparing it with the secret number, and counting bulls/cows.
    """
    bulls = 0
    cows = 0

    unmatched_gen_num = []
    unmatched_gue_num = []

    for i, digit in enumerate(gue_num):
        if gen_num[i] == digit:
            bulls += 1
        else:
            unmatched_gen_num.append(gen_num[i])
            unmatched_gue_num.append(digit)
    
    cows = sum(d in unmatched_gen_num for d in unmatched_gue_num)

    print(f"You have {bulls} bull{'s' if bulls != 1 else ''} and {cows} cow{'s' if cows != 1 else ''}.")
    return bulls, cows
    

def game_playing() -> None:
    """
    Playing the game, counting attempts, and measuring the duration of the game.
    """
    gen_num = number_generating()
    attempts = 0 # only valid attempts are counted
    start_time = time.time()

    while True:
        gue_num = number_guessing()
        bulls, cows = evaluate_guess(gen_num, gue_num)
        attempts += 1

        if bulls == DIGIT_COUNT:
            print(f"Congratulations! You find the secret number {gen_num} in {attempts} attempts.")
            break

    end_time = time.time()
    game_time = end_time - start_time
    minutes = int(game_time // 60)
    seconds = int(game_time % 60)

    print(f"Game time is {minutes} min and {seconds} sec")


def main() -> None:
    """
    Main function - start the entire game and then ask the user if they want to play again.
    """
    while True: 
        game_playing()
        new_game = input("Do you want to play a new game? (y/n): ").lower()
        if new_game != "y":
            print("Thank you for playing and have a nice day!")
            break


if __name__ == "__main__":
    main()