from validator import Validator


class User:

    def __init__(self, login: str, password: str) -> None:
        Validator.validate_logIn(login)
        Validator.validate_password(password)
        self.login = login
        self.password = password

# for values in cursor.execute("""SELECT * FROM users"""):
#     print(values)
# user = User("asdxzcxzc", "213dfc.ddd")