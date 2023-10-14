"""
Exercise 23 : 99 Bottles of Beer on the Wall
"""


def bottles_of_beer(num):
    """
    Calculate the number of bottles of beer on the wall.
    And print out like this :

    99 bottles of beer on the wall,
    99 bottles of beer.
    Take one down, pass it around,
    98 bottles of beer on the wall.
    ...
    1 bottle of beer on the wall,
    1 bottle of beer.
    Take one down, pass it around,
    No more bottles of beer on the wall!

    Returns:
        str: The repeated lyrics of bottles of beer on the wall.
    """
    # fix : complete this
    text = ''
    for numberOfBottles in range(num, num-1, -1):
        if numberOfBottles == 1:
            text += f'1 bottle of beer on the wall,\n'
            text += f'1 bottle of beer.\n'
        else:
            text += f'{numberOfBottles} bottles of beer on the wall,\n'
            text += f'{numberOfBottles} bottles of beer.\n'
        text += f'Take one down, pass it around,\n'
        if numberOfBottles-1 == 0:
            text += f'No more bottles of beer on the wall!\n'
        else:
            text += f'{num-1} bottles of beer on the wall.\n'
    return text


