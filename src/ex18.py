"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(cups, unit_per_cup):
    total = 0
    if cups > 0:
        if cups != 8:
            total = (cups - (cups // 8)) * unit_per_cup
        else:
            total = cups * unit_per_cup
    else:
        return 0
    return total