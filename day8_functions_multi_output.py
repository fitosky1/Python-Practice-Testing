"""
Functions with multiple outputs
"""
#
import random

#
# list to work with
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


# create new function that output max, sum and multiolication
def max_sum_mult_in_nested(nested_list1, nested_list2):
    # max of both matrices
    max_i1 = 0
    max_j1 = 0
    for i in range(len(nested_list1)):
        for j in range(len(nested_list1[i])):
            if nested_list1[i][j] > nested_list1[max_i1][max_j1]:
                max_i1 = i
                max_j1 = j
    max_i2 = 0
    max_j2 = 0
    for i in range(len(nested_list2)):
        for j in range(len(nested_list2[i])):
            if nested_list2[i][j] > nested_list2[max_i2][max_j2]:
                max_i2 = i
                max_j2 = j
    # mutiplication
    ln1 = len(nested_list1)
    ln2 = len(nested_list1[0])
    tmp_mlist = [[0 for columns in range(ln2)] for rows in range(ln1)]
    for i in range(ln1):
        for j in range(ln2):
            tmp_mlist[i][j] = (
                nested_list1[i][j] * nested_list2[i][j]
            )  # replace in place
    # Global sum
    sum1 = 0
    for i in range(len(nested_list1)):
        for j in range(len(nested_list1[i])):
            sum1 += nested_list1[i][j]
    sum2 = 0
    for i in range(len(nested_list2)):
        for j in range(len(nested_list2[i])):
            sum2 += nested_list2[i][j]
    return (
        (nested_list1[max_i1][max_j1], max_i1, max_j1),
        (nested_list2[max_i2][max_j2], max_i2, max_j2),
        sum1,
        sum2,
        tmp_mlist,
    )  # multiple outputs are a tuple


# print out
print(
    "maxs within (nested list1, max_i, max_j),(nested list1, max_i, max_j), sum_list1, sum_list2, [mult_list]:\n",
    max_sum_mult_in_nested(rnd_nested_list, rnd_nested_list2),
)

# list for exercise 2
# test_int_list = list(random.sample(range(10, 100), 5))
# print(test_int_list)

## sum and reversed(
# def sum_and_reversed(list1):
#     sigma = 0
#     lght = len(list1)
#     new_list = []
#     for i in list1:
#         sigma += i
#         new_list.append(list1[-i])  # don't know how to do it with the same index i
#     return sigma, new_list
#
#
# # print out
# print("Sum and reversed:", sum_and_reversed(test_int_list))
