"""
Data structures
insert in list after checking
"""
# Lists or also called arrays in python
list1 = list(range(15))
list2 = list(range(10, 25))
list3 = list(range(100, 115))
#

print("list1", list1)
print("list2", list2)
print("list3", list3)

# in1 = int(input("in which list do you want to insert? \n"))
in2 = int(input("what number to insert ?\n"))
in3 = int(input("in which position \n"))

# check in3 within list length
if (in3 > len(list1)) and (in3 > len(list2)) and (in3 > len(list3)):
    print("position not within list ranges")
    in3 = int(input("insert valid position \n"))
else:
    print("position valid")

# insertions
list1.insert(in3, in2)
list2.insert(in3, in2)
list3.insert(in3, in2)
# Print new lists
print("new list1 :", list1)
print("new list2 :", list2)
print("new list3 :", list3)
