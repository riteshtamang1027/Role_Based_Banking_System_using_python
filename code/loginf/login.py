import os
from adminf.admin import admin_menuList
# Login system section
def login (role):
    # Initilize attempt
    attempt = 0
    while attempt < 3:
      # user input their username and password.
      username = input("Enter username: ")
      password = input("Enter password: ")

      # path directery
      base_dir = os.path.dirname(__file__)
      actualPath = os.path.join(base_dir,'..','textfolder','main_menu.txt')
      # open the file
      with open(actualPath,'r') as f:
        users = f.readlines()

  # variable to track if login is successful
      login_success = False

      for user in  users:
        # strip remove the new line and split by coma 
        data = user.strip().split(",")
        file_username= data[0]
        file_password= data[1]
        file_role = data[2]
      
      # compare the user input data and file data
        if username == file_username and password == file_password and role == file_role:
          login_success = True
          break
      # if the logi is successfull
      if login_success:
        print("Login successfull")
        
        #  check the role,if role is equal to admin then run admin function
        if role == 'admin':
            admin_menuList()
           
        
        elif role == 'staff':
            print ("This is staff dashboard")
           
        elif role == 'customer':
            print ("This is customer dashboard")
            
        
        else:
           return
      
      # if the login is failed then run this
      else:
        attempt +=1
        print("Incorrect username or password")
        print(f"You have left attempt {3-attempt}")
    print("You attempt more than 3 times, Now the system is terminated.")

        











