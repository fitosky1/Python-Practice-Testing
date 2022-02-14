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
# print(type(weekdays[1]))
# print(type(letters))
# print(type(List_nr1[2]))

# get slice ranges
print("weekdays", weekdays)
weekdays.remove("Monday")
print(weekdays)

# to delete ranges
del weekdays[0:1]
print(weekdays)
