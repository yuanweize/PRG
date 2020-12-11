#### PRG - End-of-term Test ####

# This is the assignment for the PRG end-of-term test. This file is a valid Python module,
# instructions are written in the form of comments. Follow the instructions precisely and do not add
# any additional code to the file (not even print statements) as this file will be evaluated
# automatically.

import unittest


#### TASK 1 [1p] ####

# Consider the following function definition

def abs(num):
    abs = num
    if abs < 0:
        abs = -abs
    return abs

# In which scope is the variable 'abs' defined inside the function? Uncomment the correct answer:

# scope = "local"
scope = "global"
# scope = "functions"
# scope = "built-in"
# scope = "variables"


#### TASK 2 [4p] ####

# Implement the following function according to its docstring

def first_line(path):
    """Read the first line of a text file under given path

    :param path: Path to a text file
    :return: The first line from the file (without the trailing newline character) or None (only if
        the file is not found)
    """
    try:
        f=open(path,'r')
    except IOError:
        return None
    else:
        with open( path,'r') as f:
            return f.readline()


#### TASK 3 [5p] ####

# Implement four methods (__init__, __str__, __eq__, __add__) for the following class according to
# their tests. You do not need to add docstring to any implemented method.

class PersonAge:
    """The age of a person in years"""
    def __init__(self,age):
        self.age=age
    def __str__(self):
        return 'PersonAge('+str(self.age)+')'
    def __eq__(self,other):
        return self.age==other.age
    def __add__(self,other):
        return PersonAge(self.age+other)

# Below are unit tests for class PersonAge - you do not need to edit that code. Remember that
# the test self.assertEqual(target, output) passes if 'target == output'; otherwise, it fails.

class TestPersonAge(unittest.TestCase):
    """Test PersonAge methods"""

    def test_init(self):
        """Test that the initializer method __init__ takes a parameter"""
        PersonAge(35)

    def test_str(self):
        """Test string conversion"""
        self.assertEqual("PersonAge(35)", str(PersonAge(35)))

    def test_eq(self):
        """Test deep equality for two PersonAge instances"""
        self.assertEqual(PersonAge(45), PersonAge(45))

    def test_add(self):
        """Test the plus operator when the second operand is an integer"""
        orig_age = PersonAge(35)
        self.assertEqual(PersonAge(45), orig_age + 10)
        self.assertEqual(PersonAge(35), orig_age)


if __name__ == "__main__":
    # Execute all unit tests
    # unittest.main()
    # print(PersonAge(35)+10)
    # print(abs(-2))
    # print(first_line('a.log'))
