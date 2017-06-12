# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:45:53 2016

@author: Mebius
"""

def linear_search(my_list, num):
    found = False
    pos = 0
    list1 = my_list[:]
    for item in list1:
        if item == num:
            found = True
            pos = list1.index(item)
    if found == False:
        list1.append(num)
        list1.sort()
        pos = list1.index(num)
    return found, pos



if __name__ == "__main__":

    my_list_1 = []
    num_1 = 3

    my_list_2 = [1,2,3]
    num_2 = 4

    my_list_3 = [1,2,3]
    num_3 = 2

    my_list_4 = [1,2,5,7]
    num_4 = 3

    result_1 = linear_search(my_list_1 , num_1)
    result_2 = linear_search(my_list_2 , num_2)
    result_3 = linear_search(my_list_3 , num_3)
    result_4 = linear_search(my_list_4 , num_4)


    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
