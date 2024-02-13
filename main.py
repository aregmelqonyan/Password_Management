from user import User
from getpass import getpass
from utils import all_users, registered, exit

def main():

    """
    Main function to interact with the user for registration, login, and exiting the program.
    """
    
    while True:
        answer = input("Register, LogIn or Exit? ")

        if answer.strip().lower() == 'exit':
            exit()

        if answer.strip().lower() == "login":
            email = input("Please, etner your email. ")
            password = getpass("Please, enter your password. ").encode()
        
            if registered(email, password):
                print("Loged In successfully! ")
            else:
                print("Invalid mail or password! ")

        if answer.strip().lower() == "register":
            name = input("Create your name: ")
            surname = input("Create your surname: ")
            email = input("Create your email: ")
            password = getpass("Create your password: ")
            try:
                user = User(name, surname, email, password)
            except Exception as e:
                print(e)
                continue
            user.register()

        print("Would you like to see all users?(yes/no) ")
        answer = input("Yes/No")

        try:
            if answer.strip().lower() == "yes":
                print(all_users())
        except:
            print("Your login and password saved successfully!")

if __name__ == "__main__":
    main()
