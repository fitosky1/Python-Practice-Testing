"""
IF statements with numbers
"""
# inputs
nr1 = int(input("First ?\n"))
nr2 = int(input("Second ?\n"))

# prints and types
print(nr1, type(nr1))
print(nr2, type(nr2))
# sum
sumnr = nr1 + nr2
print("The sum is " + str(sumnr))
print("and... ")

# Comparison and conditions
if sumnr > 100:
    print("it's a big number!")
elif 10 <= sumnr <= 100:
    print("it's a mediocre number")
elif 5 <= sumnr < 10:
    print("it's a small number")
else:
    print("it's a very small number")
