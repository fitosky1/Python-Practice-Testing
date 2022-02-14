"""
Data
remove elements from a list
after removing the list is reindexed
"""
# Lists or also called arrays in python

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
#
letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
]
#
numbers = list(range(100, 107))

# get slice ranges
print("l1: weekdays", weekdays)
print("l2: letters", letters)
print("l3: numbers", numbers)

rml1 = input("Day from l1 to remove \n")
rml2 = int(input("index from l2 to remove \n"))
rml3 = int(input("index from 0 to l3 to remove \n"))

# remove by string
weekdays.remove(rml1)
print(weekdays)
# del by index
del letters[rml2]
print(letters)
# remove range
del numbers[0:rml3]
print(numbers)
