# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:54:13 2016

@author: Peterhuang
"""

attend = int(input("Please input the number of people coming:"))
given = int(input("Please input the number of food given per person:"))
total_needed = attend *given
if total_needed % 10 != 0:
    min_hotdogs = total_needed//10 + 1
    hotdogs_left = min_hotdogs * 10 - total_needed
else:
    min_hotdogs = total_needed//10
    hotdogs_left = 0
if total_needed % 8 != 0:
    min_buns = total_needed//8 + 1
    buns_left = min_buns * 8 - total_needed
else:
    min_buns = total_needed//8
    buns_left = 0
    
print(min_hotdogs)
print(min_buns)
print(hotdogs_left)
print(buns_left)

