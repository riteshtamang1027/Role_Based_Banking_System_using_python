# Import functions from other files inside the same folder
# create_staff_account() → used to add new staff
# view_staffs() → used to display the list of staff members
from .createStaff import create_staff_account, view_staffs

# Import search function to find staff by ID or email
from .searchStaff import search_staff

# Function that displays the admin menu and handles admin operations
def admin_menuList():

   # Loop keeps running until the admin chooses to logout
   while True:
        # Display the admin menu title
        print("----- Admin Menu List -----")
        # List containing all admin menu options
        menu = [
            '1. Create Staff Account',
            '2. View Staff',
            '3. View Customers',
            '4. Generate Customer Report',
            '5. Search User (ID/Email)',
            '6. Logout'
        ]

        # Loop through the menu list and print each option
        for menuList in menu:
            print(menuList)

        # Print a line separator for better display
        print("-"*30)

        # Ask the admin to choose an option
        choice = input("Choose the number to take a action: ")
          
        # If admin chooses option 1, create a new staff account
        if choice == "1":
            create_staff_account()

        # If admin chooses option 2, display the staff list
        elif choice == "2":
            print("----- Here is the Staffs ----- ")
            view_staffs()
            print("-"*30)

        # Option 3 placeholder for viewing customers
        elif choice == "3":
            print("")

        # Option 4 placeholder for generating customer reports
        elif choice == "4":
            print

        # If admin chooses option 5, search staff by ID or email
        elif choice == "5":
            search_staff()

        # If admin chooses option 6, logout from admin menu
        elif choice == "6": 
            print("Logout successful!")
            break  # Exit the loop and return to the previous menu

        # If the admin enters an invalid number
        else:
            print("Invalid number chosen.")

# This condition ensures the admin menu runs only when this file is executed directly
# It prevents the menu from running automatically when the file is imported by another module
if __name__ == "__main__":
    admin_menuList()