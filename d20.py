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
        if input("Roll again? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
