"""
Data structures
Slicing
"""

# Lists or also called arrays in python

# get slice ranges
llen = int(input("orig list length?\n"))
sl1 = int(input("end list 1?\n"))
sl2 = int(input("start list 2\n"))
sl3 = int(input("end for list 3?\n"))
sl4 = int(input("skip every nth in list3?\n"))

list_orig = list(range(llen))
print("Original list ", list_orig)
#
print("list w/ ending " + str(sl1))
print(list_orig[:sl1])
print("list w/ begginng " + str(sl2))
print(list_orig[sl2:])
print("list w/ end " + str(sl3) + " and skip every " + str(sl4))
print(list_orig[:sl3:sl4])
