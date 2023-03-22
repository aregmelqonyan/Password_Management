from validator import Validator
import hashlib


class User:

    def __init__(self, login: str, password: str) -> None:
        Validator.validate_logIn(login)
        Validator.validate_password(password)
        self.login = login
        self.password = User.hash_password(password)

    @staticmethod
    def hash_password(password):
        pwd = f"{password}".encode()
        return hashlib.sha3_256(pwd).hexdigest()
# for values in cursor.execute("""SELECT * FROM users"""):
#     print(values)
# user = User("asdxzcxzc", "213dfc.ddd")