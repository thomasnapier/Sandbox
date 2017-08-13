MENU = """(I)nches to Centimetres
(C)entimetres to Inches
(M)iles to Kilometres
(K)ilometres to Miles
(Q)uit"""
print('Please select an option')
print(MENU)
selection = input(">>> ").upper()
while selection != "Q":
    if selection == "I":
        print("Please enter the inches")
        inches = input(">>> ")
        inches_to_centimetres = float(inches) * 2.54
        print("{:.2f}cm".format(inches_to_centimetres))
    elif selection == "C":
        print("Please enter the centimetres")
        centimetres = input(">>> ")
        centimetres_to_inches = float(centimetres) / 2.54
        print("{:.2f}inches".format(centimetres_to_inches))
    elif selection == "M":
        print("Please enter the miles")
        miles = input(">>> ")
        miles_to_kilometres = float(miles) / 0.62
        print("{:.2f}km".format(miles_to_kilometres))
    elif selection == "K":
        print("Please enter the kilometres")
        kilometres = input(">>> ")
        kilometres_to_miles = float(kilometres) * 0.62
        print("{:.2f}miles".format(kilometres_to_miles))
    else:
        print("Please select a real option")
    print('Please select an option')
    print(MENU)
    selection = input(">>> ").upper()
print("Bye")