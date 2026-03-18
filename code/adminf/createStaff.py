import os

# Get the directory (folder) where this current Python file is located
path = os.path.dirname(__file__)

# Build the full path to the staff_list.txt file
actualPath = os.path.join(path, '..', 'textfolder', 'staff_list.txt')

# Function used to create a new staff account
def create_staff_account():
    # Take input from admin for staff account details
    username = input("Enter staff username: ")
    password = input("Enter staff password: ")
    role = input("Enter your role: ")
    email = input("Enter staff email: ")
    staffId = int(input("Enter staff ID: "))

    # Open the staff file in append mode ('a')
    with open(actualPath, 'a') as f:

        # Write the staff information into the file separated by commas
        # This format makes it easy to read and split later
        f.write(f'{username},{password},{role},{email},{staffId} \n')
    
    # Inform the admin that the staff account was created successfully
    print("Staff account created successfully!")

# Function used to display all staff records stored in the file
def view_staffs():
    # Open the staff list file in read mode
    with open(actualPath, 'r') as file:

        # Loop through each line in the file
        for data in file:
            # Print the staff record
            print(data)

# This block runs only if this file is executed directly
# It will not run automatically if the file is imported by another module
if __name__ == "__main__":
    view_staffs()