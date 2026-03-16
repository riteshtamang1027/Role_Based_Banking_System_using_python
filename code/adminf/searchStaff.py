import os
def search_staff():
   
    print("----- You can search your staff and customer -----")
    search_user= input("Enter user email or user_id: ")

    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir,"..","textfolder",'staff_list.txt')
    with open(path,'r') as f:
        users = f.readlines()
        for user in users:
            item = user.strip().split(",")

            if len(item) <5:
                continue

            username, password, role, email, user_id = item

            if  search_user == email or search_user == user_id:
                print("----- Here is a user information -----")
                print(f'username: {username}')
                print(f'password: {password}')
                print(f'role: {role}')
                print(f'email_id: {email}')
                print(f'user_id: {user_id}')
                    
            else:
                print("User not found")
    print("-"*30)
        # break




# if __name__ == "__main__":
#     search_staff()