# functions for hangman game

def hangman_func(player_lives):
    if player_lives == 5:
        print(" _____")
        print(" |   |")
        print(" |   O")
        print(" |    ")
        print(" |    ")
        print("------")
    if player_lives == 4:
        print(" _____")
        print(" |   |")
        print(" |   O")
        print(" |   |")
        print(" |    ")
        print("------")
    if player_lives == 3:
        print(" _____")
        print(" |   |")
        print(" |   O")
        print(" |   |")
        print(" |  / ")
        print("------")
    if player_lives == 2:
        print(" _____")
        print(" |   |")
        print(" |   O")
        print(" |   |")
        print(" |  / \\")
        print("------")
    if player_lives == 1:
        print(" _____")
        print(" |   |")
        print(" |   O")
        print(" |  /|")
        print(" |  / \\")
        print("------")
    if player_lives == 0:
        print(" _____")
        print(" |   |")
        print(" |   O")
        print(" |  /|\\")
        print(" |  / \\")
        print("------")