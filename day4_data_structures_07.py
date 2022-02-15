"""
Data
search within list with command
IN inside of an IF clause
"""
# Lists or also called arrays in python
# Search within lists

list1 = list(range(10))
#
check1 = 4
check2 = 12
#
if check1 in list1:
    print("check1 in list!")
# dd another otherwise the if stops after the first
if check2 not in list1:
    print("check2 NOT in list")
#
# w strings
list2 = ["Hello", "World"]
if "Hello" in list2:
    print("Hello again")
else:
    print("Not in list2")
