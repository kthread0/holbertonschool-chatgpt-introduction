#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.
    
    The factorial of a non-negative integer n is the product of all positive 
    integers less than or equal to n. For example, factorial(5) = 5! = 5×4×3×2×1 = 120.
    This function uses recursive approach where factorial(n) = n × factorial(n-1).
    
    Parameters:
    n (int): A non-negative integer for which to calculate the factorial.
             Must be >= 0. The function assumes valid input.
    
    Returns:
    int: The factorial of n. Returns 1 for n=0 (by mathematical definition).
         For n>0, returns n × (n-1) × (n-2) × ... × 2 × 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
