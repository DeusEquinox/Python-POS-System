from Classes import tableList
from ItemList import foodList
from ItemList import priceList


dailyTotal = 0


def login_menu():
    print("Welcome to Highlands Cafe")
    print("""
    1. Login
    2. Exit
    """)
    choice = input("Select an option: ")

    while choice != "1" and choice != "2":
        choice = input("Please enter valid input: ")
    else:
        if choice == "1":
            login()
        elif choice == "2":
            exit()


def login():

    credentials = {}
    with open("Login.txt", 'r') as file:
        for line in file:
            (key, val) = line.strip().split(",")
            credentials[key] = val

    global username
    username = input("Please enter username: ")
    password = input("Please enter password: ")

    if username not in credentials.keys():
        print("Username is incorrect")
        login()
    elif password != credentials[username]:
        print("Password is incorrect")
        login()
    else:
        print("\nWelcome", username)
        main_menu()


def main_menu():
    print("""What would you like to do today?
    1. Assign Table
    2. Change customers
    3. Add to Order
    4. Prepare bill
    5. Complete Sale
    6. Cash up
    0. Log Out""")

    choice = input("Select an option (1-6) or 0: ")

    if choice == "1":
        assign_table()
    elif choice == "2":
        change_customers()
    elif choice == "3":
        add_to_order()
    elif choice == "4":
        prepare_bill()
    elif choice == "5":
        complete_sale()
    elif choice == "6":
        cash_up()
    elif choice == "0":
        print("Bye Bye!")
        login_menu()
    else:
        print("Please select a valid option")
        main_menu()


def assign_table():
    print("List of tables")
    for table in tableList:
        print("    " + str(table.tableNo) + ". Table", table.tableNo, "-", table.assignment)

    choice = input("Please select one of the tables or 0 to exit: ")

    if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6":
        if tableList[int(choice)-1].assignment == "assigned":
            print("This table is already assigned to " + tableList[int(choice)-1].waiter)
            assign_table()
        else:
            tableList[int(choice)-1].assign(username)
            print("Table", tableList[int(choice)-1].tableNo, "is assigned to " + tableList[int(choice)-1].waiter)

            changeChoice = input("Do you want to add customers to the table? y/n: ")
            while changeChoice != "y" and changeChoice != "n":
                changeChoice = input("Please enter y or n: ")
            else:
                if changeChoice == "y":
                    change_customers()
                else:
                    assign_table()
    elif choice == "0":
        main_menu()
    else:
        print("Please select a valid option")
        assign_table()


def change_customers():
    count = 1
    waiterTables = []
    for table in tableList:
        if table.waiter == username:
            waiterTables.append(table)
            print("    ", count, ". Table", table.tableNo)
            count = count + 1

    choice = input("Select table 0 to exit: ")

    if choice == "0":
        assign_table()

    while not choice.isdigit():
        choice = input("Must be a number: ")
    else:
        if int(choice)-1 not in range(len(waiterTables)):
            print("Choice not in range")
            change_customers()

    amount = input("How many customers are seated at the table: ")
    while not amount.isdigit():
        amount = input("Try again: ")
    else:
        if int(amount) <= 0:
            print("Amount cant be less than 0")
            change_customers()

    tableList[int(choice) - 1].add_customers(amount)
    print(tableList[int(choice) - 1].customers, "customers have been added to the table")
    assign_table()


def add_to_order():
    count = 1
    waiterTables = []
    for table in tableList:
        if table.waiter == username:
            waiterTables.append(table)
            print("    ", count, ". Table", table.tableNo)
            count = count + 1

    choice = input("Select table or 0 to exit: ")

    if choice == "0":
        main_menu()

    while not choice.isdigit():
        choice = input("Must be a number: ")
    else:
        if int(choice) - 1 not in range(len(waiterTables)):
            print("Choice not in range")
            add_to_order()

    print("Select an item from the list to add to order")
    with open("Stock.txt", 'r') as file:
        count = 1
        for line in file:
            itemInfo = line.split(",")
            print(count, ".", itemInfo[0] + "Price: " + itemInfo[1].strip())
            count = count + 1

    orderChoice = input("Choose an item to add: ")
    while not orderChoice.isdigit():
        orderChoice = input("Must be a number: ")

    if int(orderChoice) - 1 not in range(len(foodList)):
        print("Choice not in range")
        add_to_order()

    item = foodList[int(orderChoice)-1]
    price = priceList[int(orderChoice)-1]

    quantity = input("How many items would you like to add?: ")
    while not quantity.isdigit():
        quantity = input("Must be a number: ")

    waiterTables[int(choice)-1].add_order(item, int(quantity), round(float(price), 2))
    add_to_order()


def prepare_bill():
    count = 1
    waiterTables = []
    for table in tableList:
        if table.waiter == username:
            waiterTables.append(table)
            print("    ", count, ". Table", table.tableNo)
            count = count + 1

    if len(waiterTables) == 0:
        print("You're not assigned to a table yet")
        main_menu()

    choice = input("Select table or 0 to exit: ")

    if choice == "0":
        main_menu()

    while not choice.isdigit():
        choice = input("Must be a number: ")
    else:
        if int(choice) - 1 not in range(len(waiterTables)):
            print("Choice not in range")
            prepare_bill()

    print("-" * 50)
    print("The bill for Table", waiterTables[int(choice)-1].tableNo, "\n")
    print("Item" + " " * 14 + "Quantity" + " " * 11 + "Price")
    for order in waiterTables[int(choice)-1].order:
        print(f'{order[0]:20}{order[1]:}              R{order[2]:.2f}')
    total = waiterTables[int(choice)-1].calc_total()
    print("The total of your order was R" + str(total))
    print("You were helped by " + username)
    print("-" * 50)

    main_menu()


def complete_sale():
    count = 1
    waiterTables = []
    for table in tableList:
        if table.waiter == username:
            waiterTables.append(table)
            print("    ", count, ". Table", table.tableNo)
            count = count + 1

    if len(waiterTables) == 0:
        print("You're not assigned to a table yet")
        main_menu()

    choice = input("Select table or 0 to exit: ")

    if choice == "0":
        main_menu()

    while not choice.isdigit():
        choice = input("Must be a number: ")
    else:
        if int(choice) - 1 not in range(len(waiterTables)):
            print("Choice not in range")
            complete_sale()

    if not waiterTables[int(choice)-1].billPrepared:
        print("Please prepare bill before completing sale")
        main_menu()

    fileName = input("Enter a file name: ")
    while len(fileName.strip()) == 0:
        fileName = input("Name can be blank. Enter a new name: ")

    with open(fileName + ".txt", "a+") as file:
        file.write("-" * 50)
        file.write(f"\nThe bill for Table {waiterTables[int(choice) - 1].tableNo}\n")
        file.write("Item" + " " * 14 + "Quantity" + " " * 11 + "Price\n")
        for order in waiterTables[int(choice) - 1].order:
            file.write(f'{order[0]:20}{order[1]:}              R{order[2]:.2f}\n')
        total = waiterTables[int(choice) - 1].calc_total()
        file.write(f"The total of your order was R{total}\n")
        file.write(f"You were helped by {username}\n")
        file.write("-" * 50)

    global dailyTotal
    dailyTotal += total

    waiterTables[int(choice) - 1].unassign()
    main_menu()


def cash_up():
    global dailyTotal
    print(f"Today we made {dailyTotal}")
    clear = input("Do you want to clear the daily total?(y/n) ")

    while not clear == "y" and clear == "n":
        clear = input("Enter y or n: ")
    else:
        if clear == "y":
            for table in tableList:
                table.unassign()
            dailyTotal = 0
            main_menu()
        elif clear == "n":
            main_menu()


login_menu()
