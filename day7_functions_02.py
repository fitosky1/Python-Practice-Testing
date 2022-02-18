"""
Simple
Functions with lists
"""
#
import random

#
# list to work with
test_int_list = list(random.sample(range(10, 100), 5))
print("initial list:",test_int_list)
#
def globalsum(list1):
    sigma = 0
    for i in list1:
        sigma += i
    return sigma


#
print("Sigma:", globalsum(test_int_list))
#
def reverse_list(list1):
    lght = len(list1)
    new_list = []
    for i in range(1, lght + 1):
        new_list.append(list1[-i])
    return new_list


#
print("Reversed:", reverse_list(test_int_list))
