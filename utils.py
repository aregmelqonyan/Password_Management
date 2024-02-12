import sys
import hashlib

def write_into_file(name: str, surname: str, email: str, password: str) -> None:
    """
    Appends user data to the password.txt file.

    Args:
    name (str): The user's name.
    surname (str): The user's surname.
    email (str): The user's email address.
    password (str): The user's password.

    Returns:
    None
    """
    with open("password.txt", "a") as file:
        file.write(f"{name},{surname},{email},{password}\n")


def exit() -> None:
    """
    Exits the program.

    Returns:
    None
    """
    print("Program finished! ")
    sys.exit()


def email_exists(email: str) -> bool:
    """
    Checks if the given email exists in the password.txt file.

    Args:
    email (str): The email address to check.

    Returns:
    bool: True if the email exists, False otherwise.
    """
    with open('password.txt') as file:
        file = file.read()

    return email in file


def password_exists(password: str) -> bool:
    """
    Checks if the given password exists in the password.txt file.

    Args:
    password (str): The password to check.

    Returns:
    bool: True if the password exists, False otherwise.
    """
    with open('password.txt') as file:
        file = file.read()
    
    return password in file

def registered(email: str, password: str) -> bool:
    """
    Checks if the given email and password combination is registered.

    Args:
    email (str): The user's email address.
    password (str): The user's password.

    Returns:
    bool: True if the email and password combination is registered, False otherwise.
    """
    with open('/Users/aregmelqonyan/Desktop/tasks/Password_managemnet/password.txt') as file:
        file = file.read().splitlines()
    for i in range(len(file)):
        splitted_row = file[i].split(',')
        if splitted_row[-2] == email and splitted_row[-1] == hashlib.sha3_256(password).hexdigest():
            return True
    
    return False

def all_users() -> str:
    """
    Returns all users stored in the password.txt file.

    Returns:
    str: A string containing all user data.
    """
    with open("password.txt") as file:
        file = file.read()
    
    return file


