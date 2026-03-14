from loginf.login import login
# create main function
def main():
    print("----- Banking Role System -----")
    roles = ['1. Admin','2. Staff','3. Customer']
    # list roles 
    for item in roles:
        print(item)
    print('-'*30)
    # choose user role by users
    choice = input("Choose your role: ")
    return choice
# execuite the program while user choose invalide number. 
while True:
    choose = main()
    # checking the user choosen number and role based number.
    if choose == "1":
        login('admin')
        
    elif choose == "2":
        login('staff')
        
    elif choose == "3":
        login('customer')
        
    # if the user choose  out of the role then show this message.
    else:
        print("Invalide choice!")
