from db import Database
from user import User
import hashlib

db = Database()
db.create_table_users()
login = input("Create your login: ")
password = input("Create your password: ")
user = User(login, password)
db.insert_values(user)

for i in db.cursor.execute("SELECT * FROM users"):
    print(i)

print("Would you like to check your login and password?")
answer = input("yes/no: ")

if answer == "yes":
    login = input("Please, enter your login. ")
    password = input("Please, enter your password. ").encode()

    for i in db.cursor.execute(f"""SELECT password FROM users
            WHERE login == '{login}'"""):

        if hashlib.sha3_256(password).hexdigest() == i[0]:
            print("It is okay.")
        else:
            print("It is not okay.")
