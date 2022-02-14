"""
Big comments
"""
name = input("name?\n")
age = input("age (int please)?\n")

print(name, type(name))
print(age, type(age))

# Operations
print("Some basic operations\n")
# change age to int beacause as input is string by default
age = int(age)
# operations
print("age plus (+) ten is: " + str(age + 10))
print("age minus (-) ten is: " + str(age - 10))
print("age times (*) ten is: " + str(age * 10))
print("age to the power (**)of ten is: " + str(age ** 10))
print("age divided (/) by ten is: " + str(age / 10))
print("age int division (//) by ten is: " + str(age // 10))
print("age rest division (%) by ten is: " + str(age % 10))
