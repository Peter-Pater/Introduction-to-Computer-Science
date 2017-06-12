from copy import deepcopy

import time
import random
import matplotlib.pyplot as plt


# Global variable that controls max size of the lists
LIMIT = 2000

# Optimized bubble sort function
def bubble_sort(my_list):
    for i in range(len(my_list)-1):

        for j in range(len(my_list)-1):
            if my_list[j] > my_list[j+1]:
                swap = my_list[j+1]
                my_list[j+1] = my_list[j]
                my_list[j] = swap

    return my_list


# Merge sort definition
def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = bubble_sort(left)
    right = bubble_sort(right)
    return merge(left, right)


# Merge function definition
def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right[0])
            right.remove(right[0])
        elif left[0] <= right[0]:
            result.append(left[0])
            left.remove(left[0])
    if len(left)>0:
        result = result + left
    if len(right)>0:
        result = result + right
    # result = left + right

    return result


# Function runtime timer
def check_func_time(func, N):
    start_time = time.time()
    func(N)
    end_time = time.time()
    return end_time - start_time


def main():
    random.seed(0)

    randomized_lists_merge = []
    randomized_lists_bubble = []

    print("Generating randomized lists for sorting...")
    LIMIT = 10
    randomized_lists_merge = [random.randint(0, i + 1) for i in range(LIMIT)]
    randomized_lists_bubble = deepcopy(randomized_lists_merge)

    print("Sorting")
#    merge_sorted_list = []
    merge_sorted_list = merge_sort(randomized_lists_merge)
    bubble_sorted_list = bubble_sort(randomized_lists_bubble)
    print(merge_sorted_list)
    print(bubble_sorted_list)


main()
