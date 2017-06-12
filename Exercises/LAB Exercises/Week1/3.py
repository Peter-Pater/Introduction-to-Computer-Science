# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:22:18 2016

@author: Peterhuang
"""

amount = int(input("Please input the number purchased:"))
total= amount * 99
if 10 <= amount <= 19:
    total = 0.9 * total
    discount = 0.1
elif 20 <= amount <= 49:
    total = 0.8 * total
    discount = 0.2
elif 50 <= amount <= 99:
    total = 0.7 * total
    discount = 0.3
elif 100 <= amount:
    total = 0.6 * total
    discount = 0.4
    
print(discount)
print(total)
    
