"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

import random

# Number of sides on each die to roll
DICE_SIDES: int = 6

def main():
    die1 : int = random.randint(1,DICE_SIDES)
    die2 : int = random.randint(1,DICE_SIDES)
    total = die1 + die2
    

    print(f"Dice have {DICE_SIDES} sides each.")
    print(f"First Die: {die1}")
    print(f"Second Die: {die2}")
    print(f"Total of two dice: {total}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()