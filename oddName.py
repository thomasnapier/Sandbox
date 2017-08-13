"""
Thomas Napier
"""

name = input("Enter name: ")
while name == "":
    print("Invalid name")
    name = input("Enter name:")
print(name[1:len(name):2])