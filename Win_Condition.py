def win_Game(user_guess, computer_guess):
    win = False

    if ((user_guess == 'r' and computer_guess == 's') or (user_guess == 's' and computer_guess == 'p') or
            (user_guess == 'p' and computer_guess == 'r')):
        win = True

    return win