"""
Loops
Nested Loops 03
"""
#
import random

#
# # Example
# for i in range(5):
#     for j in range(5):
#         print(i, "*", j, "=", i * j)
# print()
# #
#
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
# print(max(rnd_nested_list[0]))
# print(rnd_nested_list[0][0])
print()
#
# sum over list
sum = 0
for i in range(len(rnd_nested_list)):
    for j in range(len(rnd_nested_list[i])):
        sum += rnd_nested_list[i][j]
print("sum is: ", sum)
print()
#
# search within list for maximum value and which are those indices!
max_i = 0
max_j = 0
#
for i in range(len(rnd_nested_list)):
    for j in range(len(rnd_nested_list[i])):
        if rnd_nested_list[i][j] > rnd_nested_list[max_i][max_j]:
            max_i = i
            max_j = j
print("indices are: ", max_i, max_j)
print()
#
# print "matrix multiplication" element by element
#
nested_list_mult = rnd_nested_list  # output matrix of the same dimensions
for i in range(len(rnd_nested_list)):
    for j in range(len(rnd_nested_list[i])):
        nested_list_mult[i][j] = (
            rnd_nested_list[i][j] * rnd_nested_list2[i][j]
        )  # replace in place
print(nested_list_mult)
