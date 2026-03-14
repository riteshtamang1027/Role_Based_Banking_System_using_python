import os
def create_staff_account():

    # User input section
    username = input("Enter staff username: ")
    password = input("Enter staff password: ")
    role = input("Enter your role: ")
    email = input("Enter staff email: ")
    staffId = int(input("Enter staff ID: "))

    path = os.path.dirname(__file__)
    actualPath = os.path.join(path,'..','textfolder','staf_list.txt')
    with open(actualPath,'a') as f:
        f.write(f'{username},{password},{role},{email},{staffId} \n')
    
    print("Staff account Creat successfully!")

    # with open(actualPath,'r') as f:
    #     for items in f:
    #         print(items)

# create_staff_account()
