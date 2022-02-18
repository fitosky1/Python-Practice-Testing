"""
Simple
Functions
"""
#
def sum3(a, b, c):
    addition = a + b + c
    return addition


#
def substr(a, b):
    substraction = a - b
    return substraction


#
def multipl(factor1, factor2):
    mult = factor1 * factor2
    return mult


#
def divis(numerand, denom):
    if denom == 0:
        print("not possible")
        return
    else:
        div = numerand / denom
    return div


#
# Tests
# i = 0
# # sum3(a, b, c)
# while i < 3:
#     num1, num2, num3 = map(int, input("three numbers:\n").split())
#     print("iteration", i, ", sum3 is ", sum3(num1, num2, num3))
#     i += 1
# #
# # substr(a, b)
# i = 0
# while i < 3:
#     num1, num2 = map(int, input("2 numbers:\n").split())
#     print("iteration", i, ", substr is: ", substr(num1, num2))
#     i += 1
# #
# # multipl(factor1, factor2)
# i = 0
# while i < 3:
#     num1, num2 = map(int, input("2 numbers:\n").split())
#     print("iteration", i, ", multipl is: ", multipl(num1, num2))
#     i += 1
# #
# divis(numerand, denom)
i = 0
while i < 3:
    num1, num2 = map(int, input("2 numbers:\n").split())
    print("iteration", i, ", divis is: ", divis(num1, num2))
    i += 1
