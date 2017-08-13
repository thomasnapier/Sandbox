def main():
    SMALL = float(7.50)
    MEDIUM = float(8.75)
    LARGE = float(10.00)
    print("Which size would you like?")
    print("(S)mall ($7.50)")
    print("(M)edium ($8.75)")
    print("(L)arge ($10.00)")
    size_selection = input()
    if size_selection == "S" or size_selection == "s":
        total = SMALL
    elif size_selection == "M" or size_selection == "m":
        total = MEDIUM
    else:
        total = LARGE
    print("Would you like any toppings? Y/N")
    toppings_selection = input()
    if toppings_selection == "N" or toppings_selection == "n":
        print("Your total is $" + str(total))
    elif toppings_selection == "Y" or toppings_selection == "y":
        print("Please indicate how many toppings you would like *Note that the first two are free any after are 50c "
              "each")
        toppings_count = int(input())
        if 0 < toppings_count <= 2:
            print("Your total is $" + str(total))
        elif toppings_count > 2:
            extra_topping_price = 0.50
            total += toppings_count * extra_topping_price
            print("Your total is $" + str(total))
        else:
            print("Please enter a real value")
    else:
        print("Please use the Y or N key for yes or no")
main()