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

List_nr1 = [1, 2, 3, 4, 5, 6, 7]
List_nr2 = [10, 20, 30, 40, 50, 60, 70]

list_mixed = [8, "Do", 9, "Re", 10, "Mi", 11, "Fa", 12]

# Tests
w_ind = int(input("which number day of the week are you interested in?\n"))
print(weekdays[w_ind - 1])
print(type(weekdays[1]))
print(type(letters))
print(type(List_nr1[2]))

# combine Lists
# with (list(zip())
listW_and_L = list(zip(List_nr1, list_mixed))
print(listW_and_L)

# create list with range()
integers = list(range(0, 16, 2))
print(integers)
print(len(integers))
