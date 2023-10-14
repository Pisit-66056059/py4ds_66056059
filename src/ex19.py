"""
Exercise 19 : Password Generator
"""
import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'    # 26
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 26
NUMBERS = '1234567890'                          # 10
SPECIAL = '~!@#$%^&*()_+'                       # 13

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def gen_password(length):
    # Fix : complete this
    if length < 12:
        length = 12
    password = []
    password.append(LOWER_LETTERS[random.randint(0,25)])
    password.append(UPPER_LETTERS[random.randint(0,25)])
    password.append(NUMBERS[random.randint(0,10)])
    password.append(SPECIAL[random.randint(0,13)])
    print(password)
    while len(password) < length:
        password.append(ALL_CHARS[random.randint(0,74)])
    return ''.join(password)


