"""
Data structures
Dictionaries
"""
dict1 = {}
#
# dictionary = {"key1": value1, "key2": value2}
dict1["A"] = "a_string"  # string
dict1["B"] = True  # bool
dict1["C"] = 321  # int
dict1["D"] = ["alpha", "beta"]  # list
dict1["E"] = ""  # alias 'None' # Nothing
dict1["F"] = 3.14  # float
dict1["G"] = 123  # int
dict1["H"] = ["gamma", "delta"]  # list
dict1["I"] = ""  # alias 'None' # Nothing
dict1["J"] = 2.18  # float
#
print("whole Dictionary: ", dict1)
print(type(dict1))
#
# Simple opperations
#
# User input string
# req_entry1 = input("Input key \n")
#
# dict1["G"] = req1
# print("new whole dict1:", dict1)
# # delete last item
# dict1.popitem()
# print("new whole dict1 after popitem:", dict1)
# # delete with specific key
# del dict1["A"]
# print("new whole dict1 after 'del':", dict1)
# #
# req2 = input("which 'key' to delete ?\n")
# dict1.pop(req2)
# print("new whole dict1 after 'del':", dict1)
# if "key1" in dict1:
#     print("key1 is there")
# else:
#     print("Not there")
req_entry1 = input("Input key \n")
print(type(req_entry1))
#
# check for presence ask 3 times
# counter
i = 1
while i < 3:
    if req_entry1 in dict1:
        print("key present")
        req_entry1 = input("Input another key \n")
    else:
        dict1[req_entry1] = "new_entry"
    i += 1

print("three attempts")
print(dict1)
