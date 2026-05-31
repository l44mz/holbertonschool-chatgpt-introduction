#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculates the factorial of a non-negative integer using recursion.
        The factorial of a number n is the product of all positive integers
        less than or equal to n. By definition, factorial(0) = 1.

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
