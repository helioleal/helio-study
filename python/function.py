# Author: Helio Leal
# This program is a test of calling a function in python.
# Uses a block comment with """

def sum(a, b):
    """
    >>> my_function(2, 3)
    5
    """
    return a + b

result = sum(2,3)
print(result)