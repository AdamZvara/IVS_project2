#!/usr/bin/python


#need to have test and matlib in the same file
#to test your program just type: python3 -m unittest matlib
#if you want more specific output type: python3 -m unittest -v matlib

import unittest

from mathlib import *

#Tests for adding function (add two numbers)
class TestAdd(unittest.TestCase):

    def test_add_two_positive_intiger_num(self):
        self.assertEqual(add(2,2), 4)
        self.assertEqual(add(2,0),2)
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(13459,0),13459)
        self.assertEqual(add(2451253,100),2451353)
    
    def test_add_two_negative_integer_num(self):
        self.assertEqual(add(-1,0),-1)
        self.assertEqual(add(-12345678,12345678),0)
        self.assertEqual(add(-5,-2),-7)
        self.assertEqual(add(-4502,-456),-4958)
        self.assertEqual(add(-30918347,-12048421),-42966768)

    def test_add_two_positive_float_num(self):
        self.assertEqual(add(2.0,9.0),11.0)
        self.assertEqual(add(4.2,0.0),4.2)
        self.assertEqual(add(0.0,0.0),0.0)
        self.assertEqual(add(13459.0,1001.0),14460.0)
        self.assertEqual(add(2451253.9,100.1),2451354.0)

    def test_add_two_negative_float_num(self):
        self.assertEqual(add(-1.7,-8.3),-10.0)
        self.assertEqual(add(-5.3,2.0),-3.3)
        self.assertEqual(add(-12345678.2,0.0),-12345678.2)
        self.assertEqual(add(-4502.4,-456.5),-4958.9)
        self.assertEqual(add(-30918347.3,-12048421.8),-42966769.1)

    def test_add_one_intiger_one_float_positive_num(self):
        self.assertEqual(add(9.8,1),10.8)
        self.assertEqual(add(24.3,2),26.3)
        self.assertEqual(add(12.0,12),24.0)
        self.assertEqual(add(2402.3,102),2504.3)
        self.assertEqual(add(0.0,0),0.0)
    
    def test_add_one_intiger_one_float_negative_num(self):
        self.assertEqual(add(-9.2,-1.9),-11.1)
        self.assertAlmostEqual(add(-9,8.1),-0.9, 5)
        self.assertEqual(add(-124124,-124124.0),-248248)
        self.assertEqual(add(-1209,-800.1),-2009.1)
        self.assertEqual(add(-100002.9,-900000),-1000002.9)

#Tests for subract function (substrac two numbers)
class TestSub(unittest.TestCase):

    def test_sub_two_positive_intiger_num(self):
        self.assertEqual(sub(6, 2), 4)
        self.assertEqual(sub(2, 0), 2)
        self.assertEqual(sub(0, 0), 0)
        self.assertEqual(sub(2412253, 2004), 2410249)
        self.assertEqual(sub(13459, 0), 13459)
    
    def test_sub_two_negative_integer_num(self):
        self.assertEqual(sub(-1, 0), -1)
        self.assertEqual(sub(-12345678, -12345678), 0)
        self.assertEqual(sub(-5, 2), -7)
        self.assertEqual(sub(-4602, -44), -4558)
        self.assertEqual(sub(0, -0), 0)
    
    def test_sub_two_positive_float_num(self):
        self.assertEqual(sub(2.0, 9.0), -7.0)
        self.assertEqual(sub(4.2, 0.0), 4.2)
        self.assertEqual(sub(2451253.0, 100.1), 2451152.9)
        self.assertEqual(sub(0.2, 14891.2), -14891.0)
        self.assertLessEqual(sub(12.9, 13.2), -0.29)

    def test_sub_two_negative_float_num(self):
        self.assertAlmostEqual(sub(-1.7, -8.3), 6.6, 2)
        self.assertEqual(sub(-5.3, 2), -7.3)
        self.assertEqual(sub(-12345678.2, 0.0), -12345678.2)
        self.assertAlmostEqual(sub(-4502.4, -456.5), -4045.89, 1)
        self.assertEqual(sub(-30918347.3, -12048421.8), -18869925.5)

    def test_sub_one_intiger_one_float_positive_num(self):
        self.assertEqual(sub(9.8, 1), 8.8)
        self.assertEqual(sub(24.3, 1), 23.3)
        self.assertEqual(sub(13.0, 13), 0.0)
        self.assertEqual(sub(2402.3, 102), 2300.3)
        self.assertEqual(sub(0.0, 0), 0.0)

    def test_sub_one_intiger_one_float_negative_num(self):
        self.assertAlmostEqual(sub(-8.2, -9), 0.8)
        self.assertAlmostEqual(sub(-13, -4.1), -8.9)
        self.assertEqual(sub(-642156, -124124.0), -518032.0)
        self.assertEqual(sub(-1209, 408.1), -1617.1)
        self.assertEqual(sub(-100002.9, -900000), 799997.1)

#Test for multiply function(multiply two numbers)
class TestMul(unittest.TestCase):

    def test_mul_two_positive_intiger_num(self):
        self.assertEqual(mul(6, 2), 12)
        self.assertEqual(mul(2, 0), 0)
        self.assertEqual(mul(0, 0), 0)
        self.assertEqual(mul(242, 100), 24200)
        self.assertEqual(mul(56789, 1234), 70077626)
    
    def test_mul_two_negative_intiger_num(self):
        self.assertEqual(mul(-2, -4), 8)
        self.assertEqual(mul(-3, 9), -27)
        self.assertEqual(mul(-3, 0), 0)
        self.assertEqual(mul(-219, 50), -10950)
        self.assertEqual(mul(-11111, 22222), -246908642)

    def test_mul_two_postive_float_num(self):
        self.assertEqual(mul(3.0, 0.0), 0.0)
        self.assertEqual(mul(2.4, 2.0), 4.8)
        self.assertEqual(mul(0.0, 0.0), 0.0)
        self.assertEqual(mul(125.4, 45.2), 5668.08)
        self.assertEqual(mul(555.5, 222.2), 123432.1)

    def test_mul_two_negative_float_num(self):
        self.assertEqual(mul(-2.0, 4.0), -8.0)
        self.assertEqual(mul(-6.2, -4.4), 27.28)
        self.assertEqual(mul(-789.0, -763.9), 602717.1)
        self.assertEqual(mul(-98.2, 1000.5), -98249.1)
        self.assertEqual(mul(9212.3, 100.2), 923072.46)

    def test_mul_one_intiger_one_float_positive_num(self):
        self.assertEqual(mul(9.8, 1), 9.8)
        self.assertEqual(mul(14.3, 2), 28.6)
        self.assertEqual(mul(13.0, 1.2), 15.6)
        self.assertEqual(mul(123.3, 100), 12330.0)
        self.assertEqual(mul(444.4, 222.2), 98745.68)
    
    def test_mul_one_intiger_one_float_negative_num(self):
        self.assertEqual(mul(-9.1, 1), -9.1)
        self.assertEqual(mul(-4.1, -5), 20.5)
        self.assertEqual(mul(-12412, 0.0), 0.0)
        self.assertEqual(mul(-123.2, -43), 5297.6)
        self.assertEqual(mul(-100.1, -100), 10010.0)


class TestDiv(unittest.TestCase):

    def test_div_with_zero(self):
        self.assertRaises(ValueError, div, 2, 0)
        self.assertRaises(ValueError, div, 10.8, 0)
        self.assertRaises(ValueError, div, -802, 0)
        self.assertRaises(ValueError, div, -123.9, 0)
        self.assertRaises(ValueError, div, 87.9, 0)

    def test_div_two_positive_intiger_num(self):
        self.assertEqual(div(2, 1), 2)
        self.assertEqual(div(5, 5), 1)
        self.assertEqual(div(2, 1), 2)
        self.assertEqual(div(120, 10), 12)
        self.assertEqual(div(15000, 30), 500)
    
    def test_div_two_negative_intiger_num(self):
        self.assertEqual(div(2, -1), -2)
        self.assertEqual(div(-12, 6), -2)
        self.assertEqual(div(-25, -5), 5)
        self.assertEqual(div(-12925, 235), -55)
        self.assertEqual(div(-833040, -3560), 234)

    def test_div_two_positive_float_num(self):
        self.assertEqual(div(3.0, 1.0), 3.0)
        self.assertEqual(div(2.4, 2.0), 1.2)
        self.assertEqual(div(15.2, 10.0), 1.52)
        self.assertEqual(div(125.5, 5.0), 25.1)
        self.assertEqual(div(555.5, 222.2), 123432.1)
        
    def test_div_two_negative_float_num(self):
        self.assertEqual(div(-4.0, 2.0), -2.0)
        self.assertEqual(div(-6.1, -2.1), 3.0)
        self.assertEqual(div(-789.4, -789.4), 1.0)
        self.assertEqual(div(-394.4, 4.0), -394.4)
        self.assertEqual(div(10000.2, -1.2), -8333.5)

    def test_div_one_intiger_one_float_positive_num(self):
        self.assertEqual(div(9.8, 1), 9.8)
        self.assertEqual(div(14.2, 2), 7.1)
        self.assertAlmostEqual(div(33.3, 3.0), 11.1)
        self.assertAlmostEqual(div(123.3, 10), 12.33)
        self.assertAlmostEqual(div(444.4, 222.2), 2.0)
    
    def test_div_one_intiger_one_float_negative_num(self):
        self.assertEqual(div(-9.1, 1), -9.1)
        self.assertEqual(div(20.5, -5), -4.1)
        self.assertAlmostEqual(div(-124.4, 4.0), -31.1)
        self.assertAlmostEqual(div(5297.6, -43), -123.2)
        self.assertAlmostEqual(div(-100.1, -100), 1.001)


#Test class for factorial of positive integer number
class TestFact(unittest.TestCase):

    def test_factorial_error(self):
        self.assertRaises(ValueError, fact, -1)
        self.assertRaises(ValueError, fact, -10)
        self.assertRaises(ValueError, fact, -5.2)
        self.assertRaises(ValueError, fact, 8.2)
        self.assertRaises(ValueError, fact, 19.9)

    def test_factorial_int_num(self):
        self.assertEqual(fact(0), 1)
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(5), 120)
        self.assertEqual(fact(10), 3628800)
        self.assertEqual(fact(13), 6227020800)


#Test class for natural exponentiation of x to the power of n
class TestPower(unittest.TestCase):

    def test_power_errors(self):
        self.assertRaises(ValueError, prw, 2, 0)
        self.assertRaises(ValueError, prw, 2.1, 2.2)
        self.assertRaises(ValueError, prw, -2.1, -9)
        self.assertRaises(ValueError, prw, 89, 1.2)
        self.assertRaises(ValueError, prw, -21, -2.7)

    def test_power_of_positive_int_num(self):
        self.assertEqual(prw(1, 1), 1)
        self.assertEqual(prw(5, 2), 25)
        self.assertEqual(prw(12, 3), 1728)
        self.assertEqual(prw(3, 4), 81)
        self.assertEqual(prw(17, 8), 6975757441)

    def test_power_of_negative_int_num(self):
        self.assertEqual(prw(-2, 2), 4)
        self.assertEqual(prw(-3, 3), -27)
        self.assertEqual(prw(-10, 4), 10000)
        self.assertEqual(prw(-90, 2), 8100)
        self.assertEqual(prw(-89, 5), 5584059449)

    def test_power_of_positive_float_num(self):
        self.assertAlmostEqual(prw(1.0, 1), 1.0, 7)
        self.assertAlmostEqual(prw(5.0, 2), 25.0, 7)
        self.assertAlmostEqual(prw(2.5, 2), 6.25, 7)
        self.assertAlmostEqual(prw(6.5, 3), 274.625, 7)
        self.assertAlmostEqual(prw(15.0, 6), 11390625, 7)

    def test_power_of_negative_float_num(self):
        self.assertAlmostEqual(prw(-1.0, 2), 1.0, 7)
        self.assertAlmostEqual(prw(-3.2, 3), -32,768, 7)
        self.assertAlmostEqual(prw(-0.5, 4), 0.0625, 7)
        self.assertAlmostEqual(prw(-2.0, 8), 256.0, 7)
        self.assertAlmostEqual(prw(-4.5, 5), -1845.28125, 7)


#Test class for Nth root of a number
class TestNRoot(unittest.TestCase):

    def test_root_errors(self):
        self.assertRaises(ValueError, root, -2, 2)
        self.assertRaises(ValueError, root, -3, 4)
        self.assertRaises(ValueError, root, 9, 0)
        self.assertRaises(ValueError, root, 0, -20)
        self.assertRaises(ValueError, root, 0, 0)
        self.assertRaises(ValueError, root, 12.3, 0)
        self.assertRaises(ValueError, root, -12, 4)

    def test_root_of_positive_int_num(self):
        self.assertEqual(root(4, 2), 2)
        self.assertAlmostEqual(root(81, 3), 4.326748711)
        self.assertEqual(root(0, 2), 0)
        self.assertEqual(root(1, 5), 1)
        self.assertAlmostEqual(root(250, 5), 3.017088168)

    def test_root_of_negative_int_num(self):
        self.assertEqual(root(-3, 1), -3)
        self.assertEqual(root(-27, 3), -3)
        self.assertEqual(root(-8, 3), -2)
        self.assertEqual(root(-7776, 5), -6)
        self.assertAlmostEqual(root(4, -2), 0.5)

    def test_root_of_positive_float_num(self):
        self.assertAlmostEqual(root(4.4, 2.0), 2.097617696)
        self.assertAlmostEqual(root(8, 2.2), 2.573329796)
        self.assertAlmostEqual(root(145, 3.2),4.736172379)
        self.assertAlmostEqual(root(169874, 8.9), 3.869498738)
    
    def test_root_of_negative_float_num(self):
        self.assertAlmostEqual(root(-4.4, 3.0), -1.638642541)
        self.assertAlmostEqual(root(16, -2.0), 0.25)
        self.assertAlmostEqual(root(-145, 3.3), 4.518143295)
        self.assertAlmostEqual(root(169874, -8.9), 0.2584314062)


#Test class for combination of n things taken k at a time without repetition
class TestComb(unittest.TestCase):

    def test_comb_errors(self):
        self.assertRaises(ValueError, comb, 5, -1)
        self.assertRaises(ValueError, comb, -5, 1)
        self.assertRaises(ValueError, comb, -5, -3)
        self.assertRaises(ValueError, comb, 2, 4)
        self.assertRaises(ValueError, comb, 5.2, 3)
        self.assertRaises(ValueError, comb, 6, 2.2)

    def test_comb_int_num(self):
        self.assertEqual(comb(5, 3), 10)
        self.assertEqual(comb(0, 0), 1)
        self.assertEqual(comb(1, 0), 1)
        self.assertEqual(comb(2, 2), 1)
        self.assertEqual(comb(10, 5), 252)
        self.assertEqual(comb(12, 2), 66)