#
# Student Name - George Veney
# Date - Sep 11 2026
# Special Die Simulator
#
# 20 = "Critical Hit!"
# remainder 1 = Shield
# remainder 2 = Spell
# remainder 3 = Potion

import random  # Random used to generate random number for die

# Global Constants
FACES = 20  # Total faces on die
MIN_ROLLS = 5  # Minimum number of rolls
MAX_ROLLS = 10  # Maximum number of rolls

# main module
def main():
    # Ask user for the number of times to roll the die.
    total_rolls = int(input('How many times do you want to roll the die? '))

    # Ensure the number of rolls requested is > 5 and < 10
    while total_rolls < MIN_ROLLS or total_rolls > MAX_ROLLS:
        print(f'Enter a number between {MIN_ROLLS} and {MAX_ROLLS}.')
        total_rolls = int(input(f'How many time do you want to roll the die? '))

    roll_die(total_rolls)  # Call the roll_die function

def roll_die(rolls):
    # Generate random value and output results
    count = 1  # Start count at 1 since this is the 1st roll
    for time in range(1, rolls + 1):
        result = random.randint(1, FACES)
        if result == 20:  # Rolled 20 so result is CRITICAL HIT!  Also remainder 0 so entered 1st.
            print(f'Roll {count}:  {result} ==> CRITICAL HIT!')
        elif result % 4 == 0:  # Find the remainder of 0.
            print(f'Roll {count}:  {result} ==> Sword')
        elif result % 4 == 1:  # Find remainder 1
            print(f'Roll {count}:  {result} ==> Shield')
        elif result % 4 == 2:  # Find remainder 2
            print(f'Roll {count}:  {result} ==> Spell')
        elif result % 4 == 3:  # Find remainder 3
            print(f'Roll {count}:  {result} ==> Potion')
        count += 1  # Increase count by 1
    print(f'Thanks for playing!')

# Call main function
main()
