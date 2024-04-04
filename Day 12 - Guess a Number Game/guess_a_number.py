from random import randint
from guess_number_art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def make_a_guess(guess, answer, turns):
    if guess == answer:
        print("\nYour guess was right. YOU WIN!!")
    elif guess < answer:
        print("\nYour guess was too low!")
        turns -= 1
    elif guess > answer:
        print("\nYour guess was too high!")
        turns -= 1
    return turns

def set_difficulty():
    level = input("Choose the game dificulty typing (easy or hard): ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")

    turns = set_difficulty()

    print("\nI'm thinking in a number between 1 and 100. Can you guess the number?")

    answer = randint(1, 100)
    print(f'*************answer: {answer}')


    guess = 0
    while guess != answer: 
        print(f'\nNumber of turns: {turns}')   
        guess = int(input("Make a guess: "))
        turns = make_a_guess(guess, answer, turns)
        if turns == 0:
            print("\nyou have run out of guesses, you lose.")
            return
        
game()