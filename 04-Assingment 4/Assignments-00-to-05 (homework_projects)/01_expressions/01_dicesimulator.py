# Import the random library which lets us simulate random things like dice!
import random

NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, 6) # Local variable (only inside this function)
    die2 = random.randint(1, 6) # Local variable (only inside this function)
    total = die1 + die2
    print(f"Total of two dice: {total}")

def main():
    die1 = 10 # Local variable inside main()
    print("die1 in main() starts as " + str(die1)) # Checking the value before function call
    roll_dice()
    roll_dice()
    roll_dice()

    print("die1 in main() after rolling dice is still: " + str(die1)) # Confirming it remains unchanged

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()