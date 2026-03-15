from .createStaff import create_staff_account,view_staffs
from .searchStaff import search_staff

# admin menu list function 
def admin_menuList():
   while True:
        print("----- Admin Menu List -----")
        menu = ['1. Create Staff Account','2. View Staff','3. View Customers','4. Generate Customer Report','5. Search User (ID/Email)','6. Logout']
        for menuList in menu:
            print(menuList)
        print("-"*30)
        choice = input("Choose the number: ")
          
        if choice == "1":
            create_staff_account()
        elif choice == "2":
            print("----- Here is the Staffs ----- ")
            view_staffs()
            print("-"*30)
        elif choice == "3":
            print("")
        elif choice == "4":
            print
        elif choice == "5":
            search_staff()
        elif choice == "6": 
            print("Logout successful!")
            break
        else:
            print("Invalide number choosen.")


if __name__== "__main__":
    admin_menuList()








    