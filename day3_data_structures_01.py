"""
Data structures
"""
# Lists or also arrays in python
weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

# Tests
w_ind = int(input("which number day of the week are you interested in?\n"))
print(weekdays[w_ind - 1])
