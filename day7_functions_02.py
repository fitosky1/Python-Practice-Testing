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
print(rnd_nested_list)
print(rnd_nested_list2)


def find_max_in_nested(nested_list):
    max_i = 0
    max_j = 0
    for i in range(len(nested_list)):
        for j in range(len(nested_list[i])):
            if nested_list[i][j] > nested_list[max_i][max_j]:
                max_i = i
                max_j = j
    return nested_list[max_i][max_j], max_i, max_j  # multiple outputs are a tuple


print("max within nested list, max_i, max_j", find_max_in_nested(rnd_nested_list))

# matrix multiplication
def multilist_mult(list1, list2):
    tmp_list = list1
    ln = len(list1)
    for i in range(ln):
        for j in range(len(list1[i])):
            tmp_list[i][j] = list1[i][j] * list2[i][j]  # replace in place
    return tmp_list


print(
    "multiplied lists",
    multilist_mult(rnd_nested_list, rnd_nested_list2),
)
