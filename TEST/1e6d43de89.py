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
    l=[]
    count = 0
    while (count<length):
        a=random.randint(lower_bound,upper_bound)
        l.append(a)
        count = count + 1
    return l



#### TASK 2 ####

# The function below has side-effects, which is something we want to avoid. Correct the code of that
# function, so that it is a fruitful function without side-effects. You do not need to add
# a docstring.

def double_even_elements(array):
    for i, el in enumerate(array):
        if el % 2 == 0:
            array[i] *= 2
    even = [i for i in array if i%2 == 0]
    return even



#### TASK 3 ####

def rectangular_prism_volume(length, height, width):
    """Return the volume of a rectangular prism given its side length, height and width
    :param length: float  The length of the rectangular
    :param height: float The height of the rectangular
    :param width: float The width of the rectangular
    :return: volume of a rectangular
    """
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

stack_frame = {}


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
            result.append(word * 10)
        if word[-1] == ".":
            result.append("!")
        else:
            result.append(word)
    return "".join(result)


#### TASK 5 ####

# For the function below, your task is to
# 1. Fill all the question marks in the docstring and rename 'function', 'parameter' and 'result'
# 2. If the function parameter is not int, ensure that the function call ends with an exception

def function(parameter):
    """???
    :param paramter: ???
    :return: ???

    Examples
    >>> function(???)
    ???
    """
    result = 0
    while parameter:
        result = result * 10 + parameter % 10
        parameter //= 10
    return result


#### EXTRA TASK FOR EXTRA POINTS ####

# In order to obtain extra points, have a close look at the function from the previous task and
# try to figure out a single statement (so-called one-liner) with identical functionality.
# Efficiency does not need to be considered, you don't need to rename anything or to add
# a docstring.

def function_oneliner(parameter):
    pass
