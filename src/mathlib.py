#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# @file mathlip.py
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
    return x + y


##
# @brief Subtraction of two numbers
#
# @param x First number
# @param y Second number
#
# @return Difference of two numbers x, y
def sub(x, y):
    return x - y


##
# @brief Multiplication of two numbers
#
# @param x First number
# @param y Second number
#
# @return Multiplication of two numbers x, y
def mul(x, y):
    return x * y


##
# @brief Division of two numbers
#
# @param x First number
# @param y Second number
#
# @exception Division by Zero
#
# @return Division of two numbers x, y with 10 decimal digits accuracy
#
# @todo change division by zero to exception
def div(x, y):
    if y == 0:
        return 0
    else:
        return round(x / y, 10)


##
# @brief Factorial of a positive integer
#
# @param n
#
# @exception Input number is not an integer
# @exception Input number is lesser than zero
#
# @return Factorial of a positive integer n
def fact(n):
    pass


##
# @brief Natural exponentiation of x to the power of n
#
# @param x Base number
# @param n Exponent
#
# @return x to the power of n
def prw(x, n):
    pass


##
# @brief Nth root of a number
#
# @param x
# @param n Root exponent
#
# @return Nth root of a positive integer x
def root(x, n):
    pass


##
# @brief Extra function TBD
#
