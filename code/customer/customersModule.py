account_num = "0114"
password = "1234"
balance = 5000

transaction = []

# def login():
#     global account_num, password
#     acc = input("Enter your account num: ")
#     pas = input("Enter your password: ")

#     if acc == account_num and pas == password:
#         print("Login successful")
#         customer_menu()
#     else:
#         print("Invalid account or password")


def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    transaction.append(("Deposit", amount))
    print("Deposit successfully")
    print("Current balance:", balance)


def withdraw():
    global balance
    amount = int(input("Enter withdraw amount: "))

    minimum_balance = 1000

    if balance - amount < minimum_balance:
        print("Can't withdraw. Minimum balance should be 1000")
    else:
        balance = balance - amount
        transaction.append(("Withdraw", amount))
        print("Withdraw successfully")
        print("Current balance:", balance)


def change_password():
    global password
    new_pass = input("Enter a new password: ")
    password = new_pass
    print("Password changed successfully")


def statement():
    print("\nTransaction Statement")

    for t in transaction:
        print(t[0], ":", t[1])

    print("Current balance:", balance)


def customer_menu():
    while True:
        print("\nCustomer Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Change password")
        print("4. View statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            change_password()
        elif choice == "4":
            statement()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


# login()