import os
# import the admin_menulist function from adminf folder of admin file
from adminf.admin import admin_menuList
from customer.customersModule import customer_menu

# Login system section
def login (role):
    # Initilize attempt
    attempt = 0
    while attempt < 3:
      # user input their username and password.
      username = input("Enter username: ")
      password = input("Enter password: ")

      # path directery current path detector
      base_dir = os.path.dirname(__file__)
      # provides the path
      actualPath = os.path.join(base_dir,'..','textfolder','main_menu.txt')
      # open the file
      with open(actualPath,'r') as f:
        users = f.readlines()

  # variable to track if login is successful
      login_success = False

      for user in  users:
        # strip remove the new line and split by coma 
        data = user.strip().split(",")
        # check the value is enough or not, if not then skip that file and move another line
        if len(data) < 3:
           continue
        # unpacking the values from data 
        file_username,file_password,file_role = data
        # file_username= data[0]
        # file_password= data[1]
        # file_role = data[2]
      
      # compare the user input data and file data
        if username == file_username and password == file_password and role == file_role:
          login_success = True
          break
      # if the logi is successfull
      if login_success:
        print("Login successful")
        
        #  check the role,if role is equal to admin then run admin function
        if role == 'admin':
            admin_menuList()
      
        #  check the role,if role is equal to staff then run staff function      
        elif role == 'staff':
            print ("This is staff dashboard")
          
        #  check the role,if role is equal to customer then run customer function
        elif role == 'customer':
             customer_menu()
            
        
        else:
           return
      
      # if the login is failed then run this
      else:
        attempt +=1
        print("Incorrect username or password")
        print(f"You have left attempt {3-attempt}")
    print("You attempt more than 3 times, Now the system is terminated.")

        











