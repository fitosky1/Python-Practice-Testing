"""
Data structures
Tuples and Sets
"""
# Tuples UNCHANGEABLE, indexed, fix order
# within normal brackets "()"
# single entry tuple = (1,) WITH COMMA
tuple_example = (1, 2, "L")
print(tuple_example, type(tuple_example))
# index
print(tuple_example[2])
# user input created tuples
# tu1, tu2, tu3, tu4 = input("four tuple lengths?\n").split()
# #
# tuple1 = tuple(range(int(tu1)))
# tuple2 = tuple(range(int(tu2)))
# tuple3 = tuple(range(int(tu3)))
# tuple4 = tuple(range(int(tu4)))
# #
# print("tuple1", "tuple2", "tuple3", "tuple4")
# print(tuple1, tuple2, tuple3, tuple4)
# # user input for indices within Tuples
# in1, in2, in3, in4 = input("four tuple indices?\n").split()
# print("tuple1[" + in1 + "], entry", tuple1[int(in1)])
# print("tuple2[" + in2 + "], entry", tuple2[int(in2)])
# print("tuple3[" + in3 + "], entry", tuple3[int(in3)])
# print("tuple4[" + in4 + "], entry", tuple4[int(in4)])
# #
# tuple with duplicates
# tuple5 = (1, 1, 2, 3, 4)
# print(tuple5)
#
# SETS: fixed but one can add or remove but none Change
# none duplicated entries
# within curly brackets
# random order, UNINDEXED!!!!
# Simple examples
set_example = {2, 6, 9, 4, 2, 7, 49}
print(set_example)
set2 = set(range(4))
print(set2)
#
# user input created sets
se1, se2, se3, se4 = input("four set lengths?\n").split()
# #
set1 = set(range(int(se1)))
set2 = set(range(int(se2)))
set3 = set(range(int(se3)))
set4 = set(range(int(se4)))
# #
print("{set1}", "{set2}", "{set3}", "{set4}")
print(set1, set2, set3, set4)
# ADD a duplicate to your set
add_str_to_set = input(
    "add str to set1?\n"
)  # this can work beacuse the set elements are integers
set1.add(add_str_to_set)
print(set1)
add_int_to_set = int(
    input("add int to set1?\n")
)  # this can work beacuse the set elements are integers
set1.add(add_int_to_set)
print(set1)
# remove
# with .pop() random element
elem = set1.pop()
# with .remove. If it is in the list does it, if not give an error
set1_bkp = set1.copy()
set1.remove(2)
print(set1)
# with .discard. If it is in the list does it, if DOES NOT give an error
set_example.discard(2)
print(set_example)
