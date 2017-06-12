# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:39:25 2016

@author: Peterhuang
"""

n = int(input("Please input n:"))
i = 1
factorial = 1
while i <= n:
    factorial = factorial * i
    i = i + 1
print(factorial)