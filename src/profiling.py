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
    avg = 0
    n = len(num_list)
    for num in num_list:
        avg = mathlib.add(int(num), avg)
    avg = mathlib.div(avg, n)
    result = 0
    for num in num_list:
        result = mathlib.add(mathlib.prw(mathlib.sub(int(num), avg), 2), result)
    s = mathlib.root(mathlib.mul(result, mathlib.div(1, n - 1)), 2)
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
        # maybe add rounding
        num = str(random.randint(1, amount))
        f.write(num + " ")
    f.close()


if __name__ == "__main__":
    numbers = []
    generate_numbers(1000)
    # read redirected stdin
    for line in sys.stdin:
        numbers.extend(line.split())
        if not numbers:
            break

    standard_deviation(numbers)
