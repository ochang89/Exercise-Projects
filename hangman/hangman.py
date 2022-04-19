# hangman game
import random
from functions import *
from replit import clear

while True:
    player_lives = 6
    word_to_fill = []
    words = ['smooth', 'shenanigans', 'airplane', 'hippopotamus', 'hangman', 'zodiac', 'aardvark', 'transformation','metamorphosis']
    random_word = random.choice(words)

    if random_word == 'smooth':
        print("Hint: Not rough")
    elif random_word == 'shenanigans':
        print("Hint: tomfoolery; fun")
    elif random_word == 'airplane':
        print("Hint: it flies; made of metal")
    elif random_word == 'hippopotamus':
        print("Hint: big animal")

    while player_lives > 0:
        random_word = list(random_word)
        word_to_fill = []
        for i in range(0,len(random_word)):
            word_to_fill.append("_")
        
        while True:
            print("Guess the word: ", ''.join(word_to_fill))
            guess = input("Guess a letter: ")

            clear()
            word_string = ''.join(random_word)

            # user guess letter
            if len(guess) > 1:
                print("Put in one letter only")
                continue
            if guess not in random_word:
                player_lives -= 1
                print("You guessed wrong!")
                hangman_func(player_lives)
                if player_lives == 0:
                    print("\nYou lose\n")
                    break
            for i in range(0, len(random_word)):
                if random_word[i] == guess:
                    print(f"You guessed '{guess}' correctly")
                    hangman_func(player_lives)
                    word_to_fill[i] = guess
            if "_" not in word_to_fill:
                print(f"\nYou guessed {word_string}.")
                print("\n** You win! **\n")
                break
        break

    if player_lives == 0:
        print("Game Over!")
    play_again = input("Play again? (y/n): ")

    if play_again.lower() == 'y' or play_again.lower() == 'yes':
        continue
    else:
        break





