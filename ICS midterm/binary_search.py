# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:06:59 2016

@author: Mebius
"""

def binary_search(my_list, num):
    if len(my_list) == 0:
        return (False,0)
    else:
        my_list.sort()
        found = False
        pos = 0
        upper = len(my_list)-1
        lower = 0
        index = (upper + lower)//2
        while upper - lower != 1:
            if num <= my_list[index]:
                upper = index
            elif num > my_list[index]:
                lower = index
            index = (upper+lower)//2
        if my_list[upper] == num:
            found = True
            pos = upper
        else:
            found = False
            if num > my_list[-1]:
                pos = upper + 1
            else:
                pos = upper
    return found, pos







if __name__ == "__main__":

    my_list_1 = []
    num_1 = 3

    my_list_2 = [1,2,3]
    num_2 = 4

    my_list_3 = [1,2,3]
    num_3 = 2

    my_list_4 = [1,2,5,7,8,10]
    num_4 = 9

    my_list_5 = [1,2,5,7,15,21]
    num_5 = 10

    result_1 = binary_search(my_list_1 , num_1)
    result_2 = binary_search(my_list_2 , num_2)
    result_3 = binary_search(my_list_3 , num_3)
    result_4 = binary_search(my_list_4 , num_4)
    result_5 = binary_search(my_list_5 , num_5)

    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)
