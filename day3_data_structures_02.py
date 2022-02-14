"""
Data structures
"""

# IMPORTS
# import random
import random

# Lists or also called arrays in python
# weekdays = [
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
#     "Saturday",
#     "Sunday",
# ]
#
# letters = [
#     "A",
#     "B",
#     "C",
#     "D",
#     "E",
#     "F",
#     "G",
# ]
#
# List_nr1 = [1, 2, 3, 4, 5, 6, 7]
# List_nr2 = [10, 20, 30, 40, 50, 60, 70]
#
# list_mixed = [8, "Do", 9, "Re", 10, "Mi", 11, "Fa", 12]
#
# # Tests
# w_ind = int(input("which number day of the week are you interested in?\n"))
# print(weekdays[w_ind - 1])
# print(type(weekdays[1]))
# print(type(letters))
# print(type(List_nr1[2]))
#
# # combine Lists
# # with (list(zip())
# listW_and_L = list(zip(List_nr1, list_mixed))
# print(listW_and_L)

# create list with range()
# get lengths
rg1 = int(input("range 1?\n"))
rg2 = int(input("range 2?\n"))
rg3 = int(input("range 3?\n"))
rg4 = int(input("range 4?\n"))

# create Lists
list1 = list(range(rg1))
list2 = list(range(20, rg2 + 20))
list3 = list(range(100, (rg3 * 2 + 100), 2))
# testing random list
# for a desired amount of random
list4 = []
for i in range(rg4):
    n = random.randint(1, 30)
    list4.append(n)


print("list1\n", list1)
print(len(list1))
#
print("list2\n", list2)
print(len(list2))
#
print("list3\n", list3)
print(len(list3))
#
print("list4\n", list4)
print(len(list4))

# list extensions
# .append = add entry (element or another list) after "list" (ARRAY!!)
# .extend = add elements of a list to the "list"
# only work in place !!!!
# to create new a new one list1 + list2

list1.append(list4)
list3.extend(list4)
list5 = list2 + list4
#
# prints to see differences
print("new appended list1")
print(list1)
#
print("new extended list3")
print(list3)
#
print("list5")
print(list5)

# # print("list_count\n", len(list_append()))
# # #
# # print("list_extend\n", list_extend)
# print("list_count\n", len(list_extend()))
