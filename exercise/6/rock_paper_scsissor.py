# Lucas wants to create a rock, paper, and scissors game to play against the computer. He needs a program that allows the user to choose an option and then displays the result of the match.

# Create a program that allows the user to choose between rock, paper, or scissors. The computer will randomly choose an option. The program should display who won the match. Remember that:

#     Rock beats Scissors (Rock crushes Scissors);
#     Scissors beats Paper (Scissors cuts Paper);
#     Paper beats Rock (Paper covers Rock);
#     If both choose the same option, it's a tie.

import random


def show_result(player_choice):
    try:
        options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'scissors' and computer_choice == 'paper') or (player_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "Computer wins!"
    except Exception as e:
        return f"An error occurred: {e}"


while True:
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    if player_choice in ['rock', 'paper', 'scissors']:
        result = show_result(player_choice)
        print(result)
        break
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")
