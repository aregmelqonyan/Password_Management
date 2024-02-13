import hashlib
from .descriptors import NameValidator, SurnameValidator, EmailValidator, PasswordValidator
from .utils import write_into_file, registered


class User:

    """
    Represents a user with attributes such as name, surname, email, and password.
    """

    name = NameValidator()
    surname = SurnameValidator()
    __email = EmailValidator()
    __password = PasswordValidator()

    def __init__(self, name: str, surname: str, email: str,password: str) -> None:

        """
        Initializes a User object.

        Args:
            name (str): The user's name.
            surname (str): The user's surname.
            email (str): The user's email address.
            password (str): The user's password.
        """

        self.name = name
        self.surname = surname
        self.__email = email
        self.__password = password
        self.__hashed = User.hash_password(self.__password)

    @staticmethod
    def hash_password(password) -> str:

        """
        Hashes a password using the SHA-3 (SHA-256) algorithm.

        Args:
            password (str): The password to be hashed.

        Returns:
            str: The hashed password.
        """

        pwd = password.encode()
        return hashlib.sha3_256(pwd).hexdigest()
    
    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def password(self) -> str:
        return self.__password
    
    @email.setter
    def email(self, new_email: str) -> None:
        self.__email = new_email
    
    @password.setter
    def password(self, new_password: str) -> None:
        self.__password = self.hash_password(new_password)

    def register(self) -> None:

        """
        Registers the user by writing their information to a file.

        Returns:
            None
        """

        write_into_file(self.name, self.surname, self.email, self.__hashed)
        print("Registred Successfully! ")

    def login(self) -> None:

        """
        Logs the user in if the provided email and password combination is registered.

        Returns:
            None
        """
        
        if registered(self.email, self.password):
            print("Loged In successfully! ")
        else:
            print("Invalid email or password! ")

