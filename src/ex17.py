"""
Exercise 17
"""
import random


def roll_dice(num_of_dice):
    """
    Calculate the total sum of rolling a certain number of dice.

    Parameters:
        num_of_dice (int): The number of dice to roll.

    Returns:
        int: The total sum of the dice rolls.
    """
    total = 0
    if num_of_dice == 0:
        return 0
    else:
        for x in range(0,num_of_dice):
            random_number = random.randint(1,6)
            total = total + random_number
    return total
