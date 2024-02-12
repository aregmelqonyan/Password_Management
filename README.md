# User Registration and Login System

This is a simple command-line program for user registration and login. It allows users to register with their name, surname, email, and password, and then log in using their registered email and password.

## Features

- Register: Users can register by providing their name, surname, email, and password.
- Login: Users can log in using their registered email and password.
- Exit: Users can exit the program at any time.

## Installation

1. Clone this repository to your local machine.
2. Make sure you have Python installed.

## Usage

1.```bash
  cd Password_Management
  ```
2. Run the program by executing `python main.py` in your terminal.
3. Follow the prompts to register, login, or exit the program.
4. When registering, you will be asked to provide your name, surname, email, and password.
5. When logging in, you will be prompted to enter your email and password.

## Files

- `main.py`: Contains the main functionality for user interaction.
- `user.py`: Defines the `User` class for user registration and login.
- `descriptors.py`: Contains descriptor classes for validating user inputs (e.g., NameValidator, SurnameValidator, EmailValidator, PasswordValidator).
- `utils.py`: Contains utility functions for file operations and user validation.

## Descriptors

- `NameValidator`: Validates the format of a user's name.
- `SurnameValidator`: Validates the format of a user's surname.
- `EmailValidator`: Validates the format of a user's email address and checks for duplicates.
- `PasswordValidator`: Validates the format of a user's password and checks for duplicates.

## Dependencies

- Python 3.x
- `getpass`: A Python library for getting passwords from the user without displaying them on the screen.
- `hashlib`: A Python library for secure hash and message digest algorithms.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
