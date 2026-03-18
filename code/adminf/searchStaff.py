import os  # Import the os module to work with file paths
# Function to search for staff or customer by email or ID
def search_staff():
    # Display a title for the search operation
    print("----- You can search your staff and customer -----")
    # Ask the admin to enter an email or staff ID to search
    search_user = input("Enter user email or user_id: ")
    # Get the folder where this Python file is located
    base_dir = os.path.dirname(__file__)
    # Build the path to the staff_list.txt file
    path = os.path.join(base_dir, "..", "textfolder", 'staff_list.txt')
    # Open the staff list file in read mode
    with open(path, 'r') as f:
        users = f.readlines()  # Read all lines into a list
        # Loop through each user record in the file
        for user in users:
            # Remove extra spaces/newline and split the record by comma
            item = user.strip().split(",")
            # Check if the line has enough values
            # If not, skip this line and continue to the next
            if len(item) < 5:
                continue
            # Unpack the data into separate variables
            username, password, role, email, user_id = item
            # Check if the entered search term matches email or user ID
            if search_user == email or search_user == user_id:
                # Display the information of the matching user
                print("----- Here is a user information -----")
                print(f'username: {username}')
                print(f'password: {password}')
                print(f'role: {role}')
                print(f'email_id: {email}')
                print(f'user_id: {user_id}')    
            else:
                # This prints "User not found" for each non-matching line
                print("User not found")
    # Print a separator line at the end of the search output
    print("-"*30)

# This block runs the search only if the file is executed directly
# Currently commented out to allow import without running automatically
# if __name__ == "__main__":
#     search_staff()