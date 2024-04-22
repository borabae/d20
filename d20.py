import random

def roll_dice():
    """Simulate rolling a 20-sided dice."""
    return random.randint(1, 20)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        input("Press Enter to roll the dice or 'q' to quit: ")
        roll_result = roll_dice()
        print(f"You rolled: {roll_result}")
        user_input = input("Roll again? (y/n): ").lower()
        if user_input == 'y':
            continue
        elif user_input == 'n':
            break
        else:
            print("Invalid input! Please enter 'y' to roll again or 'n' to quit.")

if __name__ == "__main__":
    main()
