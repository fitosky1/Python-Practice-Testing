"""
Loops
For Loops
"""
# FOR loops
#
# Example 1: Factorials
factorial = 1  # initial value
for i in range(1, 11):
    print("i = ", i)
    factorial = factorial * i
    print("factorial = ", factorial)
#
print("")
# Example 2: sums
sum1 = 0
for i in range(21):
    print("i = ", i)
    sum1 = sum1 + i
    print("sum1 = ", sum1)
#
print("")
# Example 3: sums of even numbers
sum2 = 0
for i in range(0, 21, 2):
    print("i = ", i)
    sum2 = sum2 + i
    print("sum2 = ", sum2)
#
# Example 4 reverse list numbers
print()
list_r = []
for i in range(20, -1, -1):
    print("element = ", i)
    list_r.append(i)
print("list = ", list_r)
#
print()
print("SUM1: ", sum1)
print("SUM2: ", sum2)
print("Reverse list: ", list_r)
