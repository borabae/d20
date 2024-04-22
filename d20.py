import random

def roll_dice():
    """Simulate rolling a 20-sided dice."""
    return random.randint(1, 20)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        user_input = input("Press Enter to roll the dice or 'q' to quit: ").lower()
        if user_input == '':
            roll_result = roll_dice()
            print(f"You rolled: {roll_result}")
        elif user_input == 'q':
            break
        else:
            print("Invalid input! Please press Enter to roll the dice or 'q' to quit.")

        if user_input != 'q':
            user_input = input("Roll again? (y/n): ").lower()
            if user_input == 'n':
                break
            elif user_input != 'y':
                print("Invalid input! Please enter 'y' to roll again or 'n' to quit.")

if __name__ == "__main__":
    main()
