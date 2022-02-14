"""
IF statements with numbers
"""
# inputs
nr1 = int(input("First ?\n"))
nr2 = int(input("Second ?\n"))
nr3 = int(input("Third ?\n"))
nr4 = int(input("Fourth ?\n"))

# prints and types
print(nr1, type(nr1))
print(nr2, type(nr2))
print(nr3, type(nr3))
print(nr4, type(nr4))

# Multiple Comparison and conditions
if nr1 > nr2 and nr3 > nr4:
    print(bool(nr1 > nr2 and nr3 > nr4), "first one")
    print("Good for first condition!")
elif nr1 < nr3 and nr2 < nr4:
    print(bool(nr1 < nr3 and nr2 < nr4), "second one")
    print("Good for second condition!")
elif nr1 == nr4 or nr2 >= nr3:
    print(bool(nr1 == nr4 or nr2 >= nr3), "third one")
    print("Good for third condition!")
elif nr1 <= nr4 and nr2 == nr3:
    print(bool(nr1 <= nr4 or nr2 == nr3), "fourth one")
    print("Good for fourth condition!")
else:
    print("None fulfilled!")

# Pay attention that condition 3 and 4 do the same, so when condition 3 is fulfilled the programs stops
# Automatic bool NOT NOW it seem snot to work from the script
#
## also possible in one nested if (nr1 == nr2 and nr3 == nr4) or (nr1 == nr3 and nr2 == nr4)
# also possible to use "if not" or != for "not equal"
