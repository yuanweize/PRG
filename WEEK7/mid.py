#### PRG - Midterm ####

# This is the assignment for the PRG midterm test. This file is a valid Python module, instructions
# are written in the form of comments. Follow the instructions precisely and do not add any
# additional code to the file as this file will be evaluated automatically.


#### TASK 1 ####

# Fill the body of the function below, so that it corresponds to its docstring.

import random

def random_integers(length, lower_bound, upper_bound):
    """Build a list of randomly chosen integers using the function 'randint' from module 'random'.

    :param length: Length of the resulting list
    :param lower_bound: Lower bound of each random integer (included)
    :param upper_bound: Upper bound of each random integer (excluded)
    :return: List of random integers
    """
    arr = []
    for i in range(length):
        arr.append(random.randint(lower_bound, upper_bound-1))
    return arr


#### TASK 2 ####

# The function below has side-effects, which is something we want to avoid. Correct the code of that
# function, so that it is a fruitful function without side-effects. You do not need to add
# a docstring.

def double_even_elements(array):
    result = []
    for i, el in enumerate(array):
        if el % 2 == 0:
            result.append(el*2)
        else:
            result.append(el)
    return result


#### TASK 3 ####

def rectangular_prism_volume(length, height, width):
    """Return the volume of a rectangular prism given its side length, height and width"""
    volume = length * height * width
    return volume

def cube_volume(length):
    """Return the volume of a cube given its side length"""
    return rectangular_prism_volume(length, length, length)

# With the functions above defined, imagine that we called '>>> cube_volume(3)'. Your task is to
# provide the content of the stack frame corresponding to the 'rectangular_prism_volume' function
# call. In other words, we are interested in what the function adds to the stack. Fill in the
# following dictionary 'stack_frame' where the key is the variable name and the value is the
# variable value.

stack_frame = {"height": 3, "length": 3, "width": 3, "volume": 27}


#### TASK 4 ####

# Fix the function below, so that it follows its docstring.

def exaggerate(text):
    """Makes statements in the text more exaggerating.
    :param text: Text to be exaggerated
    :return: Exaggerated version of the input text

    Examples
    >>> exaggerate("I had to wait for 2 minutes.")
    'I had to wait for 20 minutes!'
    """
    result = []
    for word in text.split():
        if word.isdecimal():
            result.append(str(int(word) * 10))
        elif word[-1] == ".":
            result.append(word[:-1] + "!")
        else:
            result.append(word)
    return " ".join(result)


#### TASK 5 ####

# For the function below, your task is to
# 1. Fill all the question marks in the docstring and rename 'function', 'parameter' and 'result'
# 2. If the function parameter is not int, ensure that the function call ends with an exception

def reverse_number(number):
    """Reverse number digits, so that last digit of the parameter is the first digit of the result
    :param number: int number to reverse
    :return: reversed number

    Examples
    >>> reverse_number(123456789)
    987654321
    """
    assert isinstance(number, int)
    reversed_number = 0
    while number:
        reversed_number = reversed_number * 10 + number % 10
        number //= 10
    return reversed_number


#### EXTRA TASK FOR EXTRA POINTS ####

# In order to obtain extra points, have a close look at the function from the previous task and
# try to figure out a single statement (so-called one-liner) with identical functionality.
# Efficiency does not need to be considered, you don't need to rename anything or to add
# a docstring.

def function_oneliner(parameter):
    # return int("".join(list(reversed(str(parameter)))))
    return int(str(parameter)[::-1])


if __name__ == "__main__":
    print("Runned as a program")