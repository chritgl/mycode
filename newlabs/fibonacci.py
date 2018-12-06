#!/usr/bin/env python3

###############################
# Calculating Fibonacci numbers
# This is a famous mathematical series.
#
# 1 1 2 3 5 8 13 21 34
#
# The first two numbers in the series are 1.
# The third number is assigned to the sum of the previous two numbers.
#################################


################################
# The traditional way to program the Fibonacci series
##################################
def trad_fib(n):
    a = 1     # The first number in the series
    b = 1     # The second number in the series

    while b < n:
        print(a, end=" ")
        old_b = b    # Keep the original value of b
        b = a = b    # The new value of b
        a = old_b    # The new value of a
    print(a, end=
