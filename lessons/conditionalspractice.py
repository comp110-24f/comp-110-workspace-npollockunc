"""Practicing my conditionals."""

import random

# def less_than_10(num: int) -> bool:
# """Tell us if num < 10"""
# if num < 10:  # check if this is true
# return True  # "then" block
# else:
# print("Big number!")
# print("This is the end of the function!")


# print(less_than_10(num=2))


# def wake_up(alarm: bool) -> str:
# """Return a message based on if alarm is going off."""
# if alarm is True:
# return "Wake up! Go to Comp110!"
# else:
# return "Keep sleeping. You deserve it."

# print(wake_up(alarm=False))


def check_first_letter(word: str, letter: str) -> str:
    """conditional to decide if first letter of word is equal to letter"""
    if word[0] == letter:  # checks if this is True
        return "match!"  # (then block) displays that conditional is True within printed statement
    else:
        return "no match!"  # displays statement for if conditional is False


word = random.choice("dog" or "cat")
print(check_first_letter(word, letter="d"))
