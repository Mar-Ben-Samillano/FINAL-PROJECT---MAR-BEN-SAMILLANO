import random


def roll_dice():
    return random.randint(1, 6)


def main():
    print("Welcome to the Dice Rolling Simulator!")

    
    while True:
        input("Press Enter to roll the dice...")

        
        dice_result = roll_dice()
        print(f"You rolled: {dice_result}")

        
        play_again = input("Do you want to roll again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for playing! Goodbye!")
            break
        

if __name__ == "__main__":
    main()