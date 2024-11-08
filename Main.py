import Computer_Guess
import Win_Condition

user_choice = input("Please select r for rock, p for paper, and s for scissors: ")

computer_choice = Computer_Guess.comp_guess()

if user_choice == computer_choice:
    print("It's a tie!")

result = Win_Condition.win_Game(user_choice, computer_choice)

#If it's a boolean, it passes if it's true. Having a "not" checks if it's false.
if result:
    print("You win!")
elif not result:
    print("You lose!")

"""
if user_choice == "r":
    if computer_choice == "rock":
        print("It is a tie!")
    elif computer_choice == "paper":
        print("You lose!")
    elif computer_choice == "scissors":
        print("You win!")
elif user_choice == "p":
    if computer_choice == "rock":
        print("You win!")
    elif computer_choice == "paper":
        print("It is a tie!")
    elif computer_choice == "scissors":
        print("You lose!")
elif user_choice == "s":
    if computer_choice == "rock":
        print("You lose!")
    elif computer_choice == "paper":
        print("You win!")
    elif computer_choice == "scissors":
        print("It is a tie!")
"""