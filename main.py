
print(" TODAY'S MENU! ")

print("[1]Chicken Sandwich")
print("[2]Mocha Frappe")
print("[3]Caramel Frappe")
print("[4]French Fries")




option = int(input("Enter the number: "))

if option == 1:
    print("Chicken Sandwich is $4")
    option_1 = 4
    option_1 = int(input("Enter cash: "))
    if option_1 >= 4:
        print("Item purchased")
    else:
        print("Not enough cash")
elif option == 2:
    print("Mocha Frappe is $2")
    option_2 = 2
    option_2 = int(input("Enter cash: "))
    if option_2 >= 2:
        print("Item purchased")
    else:
        print("Not enough cash")
elif option == 3:
    print("Caramel Frappe is $2")
    option_3 = 2
    option_3 = int(input("Enter cash: "))
    if option_3 >= 2:
        print("Item purchased")
    else:
        print("Not enough cash")
elif option == 4:
    print("French Fries is $3")
    option_4 = 3
    option_4 = int(input("Enter cash: "))
    if option_4 >= 3:
        print("Item purchased")
    else:
        print("Not enough cash")
else:
    print("ERROR: Please choose an option")