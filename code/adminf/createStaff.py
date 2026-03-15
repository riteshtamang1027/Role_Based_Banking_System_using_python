import os
path = os.path.dirname(__file__)
actualPath = os.path.join(path,'..','textfolder','staff_list.txt')
def create_staff_account():
    # User input section
    username = input("Enter staff username: ")
    password = input("Enter staff password: ")
    role = input("Enter your role: ")
    email = input("Enter staff email: ")
    staffId = int(input("Enter staff ID: "))

    with open(actualPath,'a') as f:
        f.write(f'{username},{password},{role},{email},{staffId} \n')
    
    print("Staff account Creat successfully!")

def view_staffs():
    with open(actualPath,'r')as file:
        for data in file:
            print(data)
    
# if __name__ == "__main__":
#     view_staffs()