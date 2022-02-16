"""
Data structures
Nested Dictionaries
"""
addr_bk1 = {}
#
# dictionary = {"key1": value1, "key2": value2}
# nested_dict[key][nested_key] = "nested_value"
addr_bk1["Mr._A"] = {}  # New dict in A
addr_bk1["Mr._A"]["Addr"] = "Astr._1"
addr_bk1["Mr._A"]["Numb"] = 111111
addr_bk1["Mr._A"]["BDay"] = "01.01"
addr_bk1["Mr._A"]["Emai"] = "a-a@com"
#
addr_bk1["Mrs._B"] = {}  # New dict in A
addr_bk1["Mrs._B"]["Addr"] = "Bstr._2"
addr_bk1["Mrs._B"]["Numb"] = 222222
addr_bk1["Mrs._B"]["BDay"] = "02.02"
addr_bk1["Mrs._B"]["Emai"] = "b-b@com"
#
addr_bk1["Ms._C"] = {}  # New dict in A
addr_bk1["Ms._C"]["Addr"] = "Cstr._3"
addr_bk1["Ms._C"]["Numb"] = 333333
addr_bk1["Ms._C"]["BDay"] = "03.03"
addr_bk1["Ms._C"]["Emai"] = "c-c@com"
#
addr_bk1["Mr._D"] = {}  # New dict in A
addr_bk1["Mr._D"]["Addr"] = "Dstr._4"
addr_bk1["Mr._D"]["Numb"] = 444444
addr_bk1["Mr._D"]["BDay"] = "04.04"
addr_bk1["Mr._D"]["Emai"] = "d-d@com"
#
print("Whole Nested Dictionary: ", addr_bk1)
print(type(addr_bk1))
#
# Add / Change / Delete Operations
# Testing multiple input and split()
# "Very" synthetic example to minimize the inputs calls and the use of split() function
# In this case the new entry is "Sr._F Fstr_7 777777 07.07 f-f.com"
#
question1 = int(input("do you want to add (1), change(2) or delete(3) an entry?\n"))
if question1 == 1:
    key1, addr, numb, bday, emai = input(
        "input new entry (space separated): key1(Name) addr numb bday email:"
    ).split()
    addr_bk1[key1] = {}
    addr_bk1[key1].update({"Addr": addr})
    addr_bk1[key1].update({"Numb": numb})
    addr_bk1[key1].update({"BDay": bday})
    addr_bk1[key1].update({"Emai": emai})
    print("New Nested Dictionary: ", addr_bk1)
elif question1 == 2:
    what_change = input("What key to change?\n")
    if what_change in addr_bk1:
        addr, numb, bday, emai = input("input: addr numb bday email:").split()
        addr_bk1[what_change].update({"Addr": addr})
        addr_bk1[what_change].update({"Numb": numb})
        addr_bk1[what_change].update({"BDay": bday})
        addr_bk1[what_change].update({"Emai": emai})
        print("New Nested Dictionary: ", addr_bk1)
    else:
        print("not in address book")
elif question1 == 3:
    what_delete = input("What key to delete?\n")
    if what_delete in addr_bk1:
        del addr_bk1[what_delete]
        print("New Nested Dictionary: ", addr_bk1)
    else:
        print("Not in address book")
