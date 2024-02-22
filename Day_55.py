
#DAY 55: Exercise 5 - Snake Water Gun 

""" Snake Water Gun
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win. """

import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (Snake, Water, Gun): ").strip().lower()
        if user_choice in ["snake", "water", "gun"]:
            return user_choice
        else:
            print("Invalid choice! Please enter Snake, Water, or Gun.")

def get_computer_choice():
    return random.choice(["snake", "water", "gun"])

def determine_winner(player_choice, computer_choice):
    game_matrix = {
        "snake": {"snake": "draw", "water": "win", "gun": "lose"},
        "water": {"snake": "lose", "water": "draw", "gun": "win"},
        "gun": {"snake": "win", "water": "lose", "gun": "draw"}
    }
    return game_matrix[player_choice][computer_choice]

def play_game():
    player_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    if result == "win":
        print("Congratulations! You win.")
    elif result == "lose":
        print("Sorry! You lose.")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()
