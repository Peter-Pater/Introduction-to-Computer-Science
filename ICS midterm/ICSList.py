# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:09:33 2016

@author: Mebius
"""
#linear_search.linear_search is now search here
from linear_search import linear_search as search
#from binary_search import binary_search as search
import random

class ICSList:

    def __init__(self, l=[]):
        self.num = 0
        self.d = {}
        self.R = 10

        if len(l):
            for x in l:
                self.add_item(x)

    def add_item(self, x):
        #hint: use linear_search
        try:
            self.d[x//10]
        except:
            self.d[x//10] = [x]
        else:
            result = search(self.d[x//10],x)
            found = result[0]
            pos = result[1]
            self.d[x//10].insert(pos,x)

    def delete_item(self, x):
        #hint: use linear_search.#
        try:
            self.d[x//10]
        except:
            return False
        else:
            result = search(self.d[x//10],x)
            found = result[0]
            pos = result[1]
            if found == True:
                del self.d[x//10][pos]
                return True
            else:
                return False

    def find(self, x):
        l = []
        count = -1
        for keys in self.d:
            l = l + self.d[keys]
        for i in l:
            count = count + 1
            if i == x:
                return (True, count)
            else:
                pass
        return False

    def list(self):
        l = []
        for keys in self.d:
            l = l + self.d[keys]
        return l


    def len(self):
        l = []
        count = 0
        for keys in self.d:
            l = l + self.d[keys]
        for i in l:
            count = count + 1
        return count

def main():
    random.seed(0)
    l_1 = [random.randint(0,20) for i in range(10)]
    print(l_1)
    ml = ICSList(l_1)
    print(ml.d)

    ml1 = ICSList([0,1])
    ml1.add_item(2)

    print(ml1.list())
    print(ml1.delete_item(3))
    print(ml1.delete_item(1))
    print(ml1.list())
    print(ml1.find(2))
    print()


    l_2 = [random.randint(0,10) for i in range(5)]
    ml2 = ICSList(l_2)
    print(ml2.list())
    print(ml2.len())

    # l_3 = [1,10,11,5]
    # ml3 = ICSList(l_3)
    # print(ml3.list())
    # print(ml3.d)


main()

