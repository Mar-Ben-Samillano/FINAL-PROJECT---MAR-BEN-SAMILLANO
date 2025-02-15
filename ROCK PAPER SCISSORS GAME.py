import random

def get_user_choice():
    user_choice = input("Choose one: Rock, Paper, or Scissors : ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        user_choice = input("Choose one: Rock, Paper, or Scissors : ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

play_game()