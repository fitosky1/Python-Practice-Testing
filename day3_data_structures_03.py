"""
Data structures
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
sl11 = int(input("start slice 1?\n"))
sl12 = int(input("end slice 1?\n"))
sl21 = int(input("start slice 2?\n"))
sl22 = int(input("end slice 2?\n"))

# slice lists
# list 1
if sl11 > len(weekdays) and sl12 > len(weekdays):
    print("range out list weekdays!")
    sl11 = int(input("new start slice 1?\n"))
    sl12 = int(input("new end slice 1?\n"))
    print("list 'weekdays' within corrected range " + str(sl11) + " and " + str(sl12))
    print(weekdays[sl11:sl12])
else:
    print("list 'weekdays' within range " + str(sl11) + " and " + str(sl12))
    print(weekdays[sl11:sl12])
# second list
if sl21 > len(letters) and sl22 > len(letters):
    print("range out list letters!")
    sl21 = int(input("new start slice 2?\n"))
    sl22 = int(input("new end slice 2?\n"))
    print("list 'weekdays' within corrected range " + str(sl11) + " and " + str(sl12))
    print(letters[sl21:sl22])
else:
    print("list 'letters' within range " + str(sl21) + " and " + str(sl22))
    print(letters[sl21:sl22])
