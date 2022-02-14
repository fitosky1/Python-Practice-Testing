"""
day2 with input and if statements
"""
name = input("What's your name?\n")

# Option 1 with an "OR"
# if name == "John Cleese" or name == "Michael Palin":
#     print(name + ", you have a really special name")
# else:
#     print("That's a nice name " + name)

# Option 2 with "elif"
# if name == "John Cleese":
#     print(name + ", you have a really special name")
# elif name == "Michael Palin":
#     print(name + ", you have a really special name")
# else:
#     print("That's a nice name " + name)

# Option 3 with a list decalration statement
# list with valid names
Names = ["John Cleese", "Michael Palin"]
if name in Names:
    # pass
    print(name + ", you have a really special name")
else:
    print("That's a nice name " + name)
