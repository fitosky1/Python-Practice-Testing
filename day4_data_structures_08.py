"""
Data structures
search within list using IN
"""
# Lists or also called arrays in python

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
# get slice ranges
print("letters", letters)

in1 = input("input a first letter \n")
in2 = input("input a seconf letter \n")
in3 = input("input a third letter \n")

# check by string
if in1 in letters:
    print("in1 is in list")
else:
    print("in1 is not")
#
if in2 in letters:
    print("in2 is in list")
else:
    print("in2 is not")
#
if in3 in letters:
    print("in3 is in list")
else:
    print("in3 is not")
#
# list insert
numbers = list(range(10))
print("number list :", numbers)
numbers.insert(0, 100)
print("second number list :", numbers)
numbers.insert(4, "Hi")
print("third number list :", numbers)
# insert/replace in place
numbers[2] = 1000
print("fourth number list :", numbers)
