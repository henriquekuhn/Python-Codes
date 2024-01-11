#Jogo da Forca
import random
from hangman_art import *
from hangman_words import word_list

end_of_game = False

print(logo)
print(stages[6])

#Get a random word
def random_word():
    global hangman_word, blank_word
    hangman_word = random.choice(word_list)
    print(f'The solution is:                             {hangman_word}')
    blank_str = ""
    blank_word = []
    for n in range(len(hangman_word)):
        blank_word += "_"

def draw_fork(lives):
    print(f'\nYou lost 1 life. You have now {lives-1} lives!')
    print(stages[lives-1])

def update_blank(search, guess_letter):
    discover_word = ""
    blank_word[search] = guess_letter
    for n in range(len(hangman_word)):
        discover_word += blank_word[n]
    print(discover_word)

def check_letter(guess_letter):
    global search, lives, draw
    if guess_letter in blank_word:
        print(f"You've already guessed {guess_letter}")

    else:    
        for letter in hangman_word:        
            if letter == guess_letter:
                update_blank(search, guess_letter)
            search += 1
        search = 0
        if guess_letter not in blank_word:        
            draw_fork(lives)
            lives -= 1

if __name__ == "__main__":
    global num_error, lives, search
    num_error = 0
    lives = 6
    search = 0

    random_word()

    print(f'You have {lives} lives!')
    while not end_of_game:         
        guess_letter = input("Guess a letter:").lower()
        check_letter(guess_letter)
        if lives == 0:
            print("You lost")
            end_of_game = True
        elif "_" not in blank_word:            
            print("YOU WIN!")
            end_of_game = True
        print("***********************")