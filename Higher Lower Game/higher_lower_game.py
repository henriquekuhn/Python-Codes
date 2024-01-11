import random
from higher_lower_art import logo
from higher_lower_data import data

print(logo)
print("\nGuess who have more followers!\n")

def update_name(update_one, update_two):
    if update_one['follower_count'] > update_two['follower_count']:       
        dict_exclude = update_two
        update_return = update_one
    else:
        dict_exclude = update_one
        update_return = update_two

    for index, my_dict in enumerate(data):
        if my_dict == dict_exclude:
            del data[index]
    return update_return

def get_names():
    name = random.choice(data)
    return name

def game(choice_one, choice_two, score):
    
    print(f'1. {choice_one['name']}   Vs.   2. {choice_two['name']}')
    guess = int(input('Chose 1 or 2: '))
    if (choice_one['follower_count'] > choice_two['follower_count']
        and guess == 1):
        #
        score+=1
        print(f"\nYou're right! Current score: {score}\n")
        return True, score    

    elif (choice_one['follower_count'] < choice_two['follower_count']
        and guess == 2):
        #
        score+=1
        print(f"\nYou're right! Current score: {score}\n")
        return True, score

    else:
        print(f'\nYou lost! Your final score is: {score}\n')
        return False, score
    
continue_playing = 'y'    
while continue_playing == 'y':
    score = 0            
    game_over = True
    choice_one = get_names()
    while continue_playing:
        choice_two = get_names()
        while choice_two == choice_one:
            choice_two = get_names()
    
        continue_playing, score = game(choice_one, choice_two, score)
        print(f'{choice_one['name']}: {choice_one['follower_count']}')
        print(f'{choice_two['name']}: {choice_two['follower_count']}\n')
        choice_one = update_name(choice_one, choice_two)

        
    continue_playing = input('Would you like to keep playing(y or n)? ')
