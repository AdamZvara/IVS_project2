#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# @file mathlib.py
# @brief Mathematic library with basic operations
#

##
# @brief Sum of two numbers
#
# @param x First number
# @param y Second number
#
# @return Sum of two numbers x, y
def add(x, y):
    return round(x + y, 9)


##
# @brief Subtraction of two numbers
#
# @param x First number
# @param y Second number
#
# @return Difference of two numbers x, y
def sub(x, y):
    return round(x - y, 9)


##
# @brief Multiplication of two numbers
#
# @param x First number
# @param y Second number
#
# @return Multiplication of two numbers x, y
def mul(x, y):
    return round(x * y, 9)


##
# @brief Division of two numbers
#
# @param x First number
# @param y Second number
#
# @exception Division by Zero
#
# @return Division of two numbers x, y with 9 decimal digits accuracy
def div(x, y):
    if y == 0:
        raise ValueError('Math Error')
    else:
        return round(x / y, 9)


##
# @brief Factorial of a positive integer
#
# @param n
#
# @exception Input number is not an integer
# @exception Input number is lesser than 0
#
# @return Factorial of a positive integer n
def fact(n):
    if isinstance(n, int) and n >= 0:
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1

        return factorial
    else:
        raise ValueError('Math Error')


##
# @brief Natural exponentiation of x to the power of n
#
# @param x Base number
# @param n Exponent
#
# @return x to the power of n
def prw(x, n):
    if isinstance(n, int) and n >= 0:
        return round(x ** n, 7)
    else:
        raise ValueError('Exponent is not a positive integer')


##
# @brief Nth root of a number
#
# @param x The base of root
# @param n Root exponent
#
# @exception Input number x is lesser than 0
#
# @return Nth root of an integer x
def root(x, n):
    if n == 0 or (n % 2 == 0 and x < 0) or (x == 0 and n <= 0):
        raise ValueError('Math Error')
    elif x > 0:
        return round(x ** (1/n), 9)
    else:
        return round(-(-x)**(1/n), 9)


##
# @brief Combination of n things taken k at a time without repetition
#
# @param n How many things we work with
# @param k How many things we take to one group
#
# @exception Math error if k is greater than n
# @exception Math error if k or n is lesser than 0
#
# @return Amount of possible combinations without repetition
#
def comb(n, k):
    if (isinstance(n, int) and n >= 0) and (isinstance(k, int) and k >= 0) and (n >= k):
        return fact(n)/(fact(n-k) * fact(k))
    else:
        raise ValueError('Math Error')
