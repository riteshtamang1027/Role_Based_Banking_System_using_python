from .createStaff import create_staff_account

# admin menu list function 
def admin_menuList():
    while True:
        print("----- Admin Menu List -----")
        menu = ['1. Create Staff Account','2. View Staff','3. View Customers','4. Generate Customer Report','5. Search User (ID/Email)','6. Logout']
        for menuList in menu:
            print(menuList)
        print("-"*30)
        choice = int(input("Choose the number: "))
       
        # if __name__ == "__main__":
        
        if choice == 1:
            create_staff_account()
            # break








    