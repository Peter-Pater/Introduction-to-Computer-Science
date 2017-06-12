# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 14:12:34 2016

@author: Mebius
"""

import random

class Dice:
    def __init__(self, sides=2):
        self.n_sides = sides
        self.ranges = [x/sides for x in range(0, sides)]
        self.ranges.append(1.0)
        self.point = None


    def set_ranges(self, r):
        assert len(r) == len(self.ranges)
        self.ranges = r

    def get_ranges(self):
        return self.ranges

    def roll(self):
        self.point = random.uniform(0, 1)
        return self.point

    def get_side(self):
        for i in range(self.n_sides):
            if self.point > self.ranges[i] \
            and self.point <= self.ranges[i+1]:
                break
        return i+1

if __name__ == "__main__":
    count = 10000
    count_div_three = 0
    count_nine = 0
    #implement your code here
    #for part 1, you need to roll the die once and keep track of %3 in range(count)
    Dice1 = Dice(10)
    range1 = Dice1.ranges[:]
    point1 = 0
    index1 = 0
    for i in range(count):
        Dice1.roll()
        range1.append(Dice1.point)
        range1.sort()
        index1 = range1.index(Dice1.point)
        point1 = range1[index1+1] * 10
        if point1%3 == 0:
            count_div_three += 1
        range1 = Dice1.ranges

    print("Total number of multiples of 3 out of 10000 trials: ", count_div_three)
    prob_one_die = count_div_three/count
    print("Probability of getting multiples of 3 for one die: ", prob_one_die)

    #implement your code here
    #for part 2, you need to roll 2 dices and get the sum
    #keep track of the count of sum-9 in range(count)
    range1 = Dice1.ranges[:]
    point1 = 0
    index1 = 0

    Dice2 = Dice(10)
    range2 = Dice2.ranges[:]
    point2 = 0
    index2 = 0
    for i in range(count):
        range1.append(Dice1.roll())
        range1.sort()
        index1 = range1.index(Dice1.point)
        point1 = range1[index1+1] * 10

        range2.append(Dice2.roll())
        range2.sort()
        index2 = range2.index(Dice2.point)
        point2 = range2[index2+1] * 10
        point = point1 + point2
        if point == 9:
            count_nine += 1
        range1 = Dice1.ranges
        range2 = Dice2.ranges

    print("Total number of sum of 9 with two dices out of 10000 trials: ", count_nine)
    prob_two_dices = count_nine/count
    print("Probability of getting sum of 9 with two dices: ",prob_two_dices)
