"""
Simple
Functions with lists
"""
#
import random

#
# list to work with
test_int_list = list(random.sample(range(10, 100), 5))
print("initial list:", test_int_list)
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

# Operate in multidimensional lists
# generate multilist
rnd_nested_list = [
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
]
rnd_nested_list2 = [
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
]
print("list1", rnd_nested_list)
print("list2", rnd_nested_list2)

# find maximum value and indices within a nested list
def find_max_in_nested(nested_list):
    max_i = 0
    max_j = 0
    for i in range(len(nested_list)):
        for j in range(len(nested_list[i])):
            if nested_list[i][j] > nested_list[max_i][max_j]:
                max_i = i
                max_j = j
    return nested_list[max_i][max_j], max_i, max_j  # multiple outputs are a tuple


print("max within nested list1, max_i, max_j", find_max_in_nested(rnd_nested_list))

# matrix multiplication
def multilist_mult(list1, list2):
    ln1 = len(list1)
    ln2 = len(list1[0])
    tmp_mlist = [[0 for columns in range(ln2)] for rows in range(ln1)]
    for i in range(ln1):
        for j in range(ln2):
            tmp_mlist[i][j] = list1[i][j] * list2[i][j]  # replace in place
    return tmp_mlist


# print out
print(
    "multiplied lists", multilist_mult(rnd_nested_list, rnd_nested_list2),
)

# matrix total sum
def multilist_sum(list1):
    sum = 0
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            sum += list1[i][j]
    return sum


# print out
print(
    "total sum list1", multilist_sum(rnd_nested_list),
)
print(
    "total sum list2", multilist_sum(rnd_nested_list2),
)
