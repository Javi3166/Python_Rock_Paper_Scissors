import random

def comp_guess():
    guess_num = random.randint(1,3)
    guess_word = ""

    if guess_num == 1:
        guess_word = "scissors"
    elif guess_num == 2:
        guess_word = "rock"
    elif guess_num == 3:
        guess_word = "paper"

    return guess_word