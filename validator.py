class Validator:

    @staticmethod
    def validate_logIn(login: str) -> None:
        seps: str = " .-_@"

        if not(6 < len(login) < 50):
            raise Exception(f'LogIn {login} not valid, it must \
                            contain 6-50 characters.')

        for character in login:
            if not character.isalnum() and character not in seps:
                raise Exception(f"LogIn {login} not valid, it must \
                            not contain {character} character")

    @staticmethod
    def validate_password(password: str) -> None:
        seps: str = " .-_@"
        characters = 0
        numbers = 0
        sep_counter = 0
        if not 8 <= len(password) <= 32:
            raise Exception(f'Password {password} not valid, it must \
                               contain 8-32 characters.')

        for character in password:
            if character.isdigit():
                numbers += 1
            elif character.isascii() and character.isalpha():
                characters += 1
            elif character in seps[1:]:
                sep_counter += 1
            else:
                raise Exception(f"Password can not contain {character}")

        if not numbers or not characters or not sep_counter:
            raise Exception("Password must contain at least one number \
                            and special character and one letter.")
