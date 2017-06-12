# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

bill = float(input('Please input the charge of the meal\n'))
tip = float(0.15*bill)
tax = float(0.07*bill)
total = float(bill + tip + tax)
print("bill:", bill)
print("tip:", tip)
print("tax:", tax)
print("total:", total)