# Customer Module

customer_file = "customers.txt" #store customer information
transaction_file = "transactions.txt" #store deposit and withdraw records


# -------- Customer Login --------
def login():
    acc = input("Enter account number: ") #The program ask for customer acc num and pass
    pas = input("Enter password: ")

    with open(customer_file, "r") as f: #open customer.txt in read mode
        for line in f:
            data = line.strip().split(",") #each line from the file is read

            if acc == data[0] and pas == data[3]:#check acc no and pass matches
                print("Login successful")
                customer_menu(data) #login sucessfully customer menu open
                return

    print("Invalid account or password")


# -------- Deposit --------
def deposit(data):#function handles money deposit
    amount = int(input("Enter deposit amount: "))#enter the deposit
    data[5] = str(int(data[5]) + amount)#balance update new balance=old blc + deposit

    update_customer(data)#this update cusyomer.txt new balance

    with open(transaction_file, "a") as f:#open transaction.txt in append mode
        f.write(f"{data[0]},Deposit,{amount}\n")

    print("Deposit successful")
    print("Balance:", data[5])


# -------- Withdraw --------
def withdraw(data):#handless withdrwwal
    amount = int(input("Enter withdraw amount: "))#entr withdraww amt

    min_balance = 1000 if data[4] == "Savings" else 1500 

    if int(data[5]) - amount < min_balance:# check if withdraw break minimum blance rule
        print("Minimum balance rule violated")
    else:
        data[5] = str(int(data[5]) - amount)#if valid balnce becomes new balance = balance-withdrawl
        update_customer(data)#trancasition saved in file

        with open(transaction_file, "a") as f:#open transacition file in append mode
            f.write(f"{data[0]},Withdraw,{amount}\n")

        print("Withdraw successful")
        print("Balance:", data[5])


# -------- Change Password --------
def change_password(data):#customer can chane password
    new_pass = input("Enter new password: ")
    data[3] = new_pass

    update_customer(data)#password save in data[3]

    print("Password changed successfully")


# -------- View Statement --------
def statement(acc):#show customer transacition
    print("\nTransaction Statement")

    with open(transaction_file, "r") as f:#open transacition file in read mode
        for line in f:
            t = line.strip().split(",")#split file line by line

            if t[0] == acc:#show only transacition is belong to login acc or not
                print(t[1], ":", t[2])


# -------- Update Customer File --------
def update_customer(updated):#this update customer.txt after the deposti,chane password and withdraw
    lines = []

    with open(customer_file, "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[0] == updated[0]:
                lines.append(",".join(updated) + "\n")
            else:
                lines.append(line)

    with open(customer_file, "w") as f:
        f.writelines(lines)


# -------- Customer Menu --------
def customer_menu(data):
    while True:
        print("\nCustomer Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Change Password")
        print("4. View Statement")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            deposit(data)
        elif choice == "2":
            withdraw(data)
        elif choice == "3":
            change_password(data)
        elif choice == "4":
            statement(data[0])
        elif choice == "5":
            break
        else:
            print("Invalid choice")


# Start program
login()