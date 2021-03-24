#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# @file profiling.py
# @author Adam Zvara - xzvara01
# @brief Program to calculate standard deviation

import sys
import random
import mathlib


##
# @brief Function for calculating sample standard deviation
#
# @param num_list List of numbers to calculate standard deviation
#
def standard_deviation(num_list):
    avg = result = 0
    n = len(num_list)
    for num in num_list:
        result = mathlib.add(mathlib.prw(int(num), 2), result)
        avg = mathlib.add(int(num), avg)
    avg = mathlib.div(avg, n)
    avg = mathlib.mul(n, mathlib.prw(avg, 2))
    s = mathlib.root(mathlib.mul(mathlib.sub(result, avg), mathlib.div(1, n - 1)), 2)
    print(s)


##
# @brief Generate file with input numbers
#
# @param amount How many numbers will be created
#
def generate_numbers(amount):
    f = open("numbers", "w")
    for i in range(1, amount+1):
        random.seed()
        # num = str(random.randint(1, amount))
        num = str(i)
        f.write(num + " ")
    f.close()


if __name__ == "__main__":
    numbers = []
    # generate_numbers(1000)
    # read redirected stdin
    for line in sys.stdin:
        numbers.extend(line.split())
        if not numbers:
            break
    standard_deviation(numbers)
