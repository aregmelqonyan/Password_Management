import re
from utils import password_exists, email_exists

class NameValidator:

    """
    Validates a name based on the specified criteria.
    """

    def __init__(self, min_length=4, max_length=20):
        """
        Initializes the NameValidator object.

        Args:
            min_length (int): Minimum length of the name (default is 4).
            max_length (int): Maximum length of the name (default is 20).
        """

        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):

        """
        Sets the value of the name attribute after validation.

        Args:
            instance: The instance of the class the descriptor is attached to.
            value (str): The value to be assigned to the name attribute.

        Raises:
            TypeError: If the value is not a string.
            ValueError: If the value does not meet the validation criteria.
        """

        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not self._validate_name(value):
            raise ValueError("Invalid name")
        instance.__dict__[self.name] = value

    def _validate_name(self, name):

        """
        Validates the name against the specified criteria.

        Args:
            name (str): The name to be validated.

        Returns:
            bool: True if the name is valid, False otherwise.
        """

        pattern = r'^[a-zA-Z][a-zA-Z0-9]{%d,%d}$' % (self.min_length - 1, self.max_length - 1)
        return re.match(pattern, name) is not None
    

class SurnameValidator:

    """
    Validates a surname based on the specified criteria.
    """
     
    def __init__(self, min_length=4, max_length=30):

        """
        Initializes the SurnameValidator object.

        Args:
            min_length (int): Minimum length of the surname (default is 4).
            max_length (int): Maximum length of the surname (default is 30).
        """

        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):

        """
        Sets the value of the surname attribute after validation.

        Args:
            instance: The instance of the class the descriptor is attached to.
            value (str): The value to be assigned to the surname attribute.

        Raises:
            TypeError: If the value is not a string.
            ValueError: If the value does not meet the validation criteria.
        """

        if not isinstance(value, str):
            raise TypeError("Surname must be a string")
        if not self._validate_surname(value):
            raise ValueError("Invalid surname")
        instance.__dict__[self.name] = value

    def _validate_surname(self, surname):

        """
        Validates the surname against the specified criteria.

        Args:
            surname (str): The surname to be validated.

        Returns:
            bool: True if the surname is valid, False otherwise.
        """

        pattern = r'^[a-zA-Z ]{%d,%d}$' % (self.min_length, self.max_length)
        return re.match(pattern, surname) is not None


class EmailValidator:

    """
    Validates an email address based on the specified criteria.
    """

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):

        """
        Sets the value of the email attribute after validation.

        Args:
            instance: The instance of the class the descriptor is attached to.
            value (str): The value to be assigned to the email attribute.

        Raises:
            TypeError: If the value is not a string.
            ValueError: If the value does not meet the validation criteria or if the email already exists.
        """

        if not isinstance(value, str):
            raise TypeError("Email address must be a string")
        if not self._validate_email(value):
            raise ValueError("Invalid email address")
        if self._is_duplicate(value):
            raise ValueError("Mail already exists! ")
        instance.__dict__[self.name] = value

    def _validate_email(self, email):

        """
        Validates the email address against the specified criteria.

        Args:
            email (str): The email address to be validated.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def _is_duplicate(self, email: str) -> bool:

        """
        Checks if the email address already exists in the database.

        Args:
            email (str): The email address to check.

        Returns:
            bool: True if the email address already exists, False otherwise.
        """
        
        return email_exists(email)
    

class PasswordValidator:

    """
    Validates a password based on the specified criteria.
    """

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):

        """
        Sets the value of the password attribute after validation.

        Args:
            instance: The instance of the class the descriptor is attached to.
            value (str): The value to be assigned to the password attribute.

        Raises:
            TypeError: If the value is not a string.
            ValueError: If the value does not meet the validation criteria or if the password already exists.
        """
         
        if not isinstance(value, str):
            raise TypeError("Password must be a string")
        if not self._validate_password(value):
            raise ValueError("Invalid password")
        if self._is_duplicate(value):
            raise ValueError("Password is already in use")
        instance.__dict__[self.name] = value

    def _validate_password(self, password):

        """
        Validates the password against the specified criteria.

        Args:
            password (str): The password to be validated.

        Returns:
            bool: True if the password is valid, False otherwise.
        """

        if not re.match(r'^[A-Za-z0-9._\-/\\;]{8,12}$', password):
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[._\-/\\;]', password):
            return False
        if len([c for c in password if c.isalpha()]) < 4:
            return False
        return True

    def _is_duplicate(self, password: str) -> bool:

        """
        Checks if the password already exists in the database.

        Args:
            password (str): The password to check.

        Returns:
            bool: True if the password already exists, False otherwise.
        """
         
        return password_exists(password)
