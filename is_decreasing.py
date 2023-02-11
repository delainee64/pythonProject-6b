# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 02/11/2023
# Description: Write a recursive function named is_decreasing that takes
# as its parameter a list of numbers. It should return True if the elements
# of the list are strictly decreasing but return False otherwise. Strictly
# decreasing means that each element is less than the preceding one - not
# less than or equal. You can assume the array contains at least two elements.

def is_decreasing(num_list):
    """Returns a boolean value of True if the values are decreasing
    and returns False otherwise."""
    if len(num_list) == 2:
        if num_list[1] < num_list[0]:   # True if numbers are decreasing.
            return True
        else:
            return False
    else:
        if num_list[0] <= num_list[1]:  # False if numbers are not decreasing.
            return False
        else:
            return is_decreasing(num_list[1:])  # recursive function.


# num_list = [10, 9, 7, 6, 5, 4, 3, 2, 1]
# print(str(is_decreasing(num_list)))
