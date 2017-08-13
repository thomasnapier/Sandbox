user_name = input("Enter name: ")
print("(G)et new name")
print("(U)pper case")
print("(L)ower case")
print("(Q)uit")
choice = input(">>> ")
while choice != "Q":
    if choice == "G" or choice == "g":
        user_name = input("Enter new name: ")
    elif choice == "U" or choice == "u":
        print(user_name.upper())
    elif choice == "L" or choice == "l":
        print(user_name.lower())
    else:
        print("Invalid choice")
    print("(G)et new name")
    print("(U)pper case")
    print("(L)ower case")
    print("(Q)uit")
    choice = input(">>> ")
print("See ya")
