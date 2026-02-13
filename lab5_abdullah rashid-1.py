"""
Program Name: Lab 5 - Dice Rolling Terms
Author: Abdullah Rashid
Purpose: Rolls two dice, displays each die and the total, then prints the correct dice term.
         Keeps rolling until the user decides to quit.
Starter Code: None (written from scratch)
Date: February 10, 2026
"""

import random


def get_roll_term(die1: int, die2: int) -> str:
    """Return the correct term based on the dice values."""
    total = die1 + die2

    # Specific dice value combinations (order doesn't matter)
    if die1 == 1 and die2 == 1:
        return "Snake Eyes"
    elif (die1 == 1 and die2 == 2) or (die1 == 2 and die2 == 1):
        return "Ace Caught a Deuce"
    elif die1 == 2 and die2 == 2:
        return "Little Joe from Kokomo"
    elif total == 5:
        # (1,4) or (4,1) or (2,3) or (3,2)
        return "Little Phoebe"
    elif die1 == 3 and die2 == 3:
        return "Jimmy Hicks from the Sticks"
    elif (die1 == 6 and die2 == 1) or (die1 == 1 and die2 == 6):
        return "Six Ace"
    elif die1 == 4 and die2 == 4:
        return "Eighter from Decatur"
    elif total == 9:
        # (3,6) or (6,3) or (4,5) or (5,4)
        return "Nina from Pasadena"
    elif die1 == 5 and die2 == 5:
        return "Puppy Paws"
    elif (die1 == 6 and die2 == 5) or (die1 == 5 and die2 == 6):
        return "Six Five no Jive"
    elif die1 == 6 and die2 == 6:
        return "Boxcars"
    else:
        # If your table doesn't name a roll, you can still show something reasonable
        return f"No special term for {total}"


def main() -> None:
    print("Welcome to Dice Rolling Terms.\n")
    print("This program rolls two dice and prints the correct term for the roll.")
    print("Type Q to quit, or press Enter to roll.\n")

    while True:
        choice = input("Roll the dice? (Press Enter to roll, or type Q to quit): ").strip().lower()
        if choice == "q":
            break

        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        term = get_roll_term(die1, die2)

        print("\n--- Roll Result ---")
        print(f"Die 1: {die1}")
        print(f"Die 2: {die2}")
        print(f"Total: {total}")
        print(f"Term:  {term}\n")

    input("Press the enter key to exit.")


if __name__ == "__main__":
    main()