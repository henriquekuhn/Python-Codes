import random
from higher_lower_art import logo
from higher_lower_data import data

print(logo)
print("\nGuess who have more followers!\n")

def get_names(data):
    name = random.choice(data)
    return name

def check_follower(guess, choice_one, choice_two):
    
    if (choice_one['follower_count'] > choice_two['follower_count']):
        return guess == 1    
    else:
        return guess == 2

def game():    
    continue_playing = 'y'    
    while continue_playing == 'y':
        score = 0            
        game_over = True
        choice_one = get_names(data)
        while game_over:
            choice_two = get_names(data)
            while choice_two == choice_one:
                choice_two = get_names(data)

            print(f'1. {choice_one['name']}   Vs.   2. {choice_two['name']}')
            guess = int(input('Chose 1 or 2: '))
            game_over = check_follower(guess, choice_one, choice_two)
            if game_over:
                score+=1
                print(f"\nYou're right! Current score: {score}\n")
            else:
                print(f'\nYou lost! Your final score is: {score}\n')

            print(f'{choice_one['name']}: {choice_one['follower_count']}')
            print(f'{choice_two['name']}: {choice_two['follower_count']}\n')

            choice_one = choice_two
            
        continue_playing = input('Would you like to keep playing(y or n)? ')

game()