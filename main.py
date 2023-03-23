from db import Database
from user import User
import hashlib

db = Database()
db.create_table_users()
login = input("Create your login: ")
password = input("Create your password: ")
user = User(login, password)
db.insert_values(user)

print("Would you like to check your login and password?")
answer = input("yes/no: ")

if answer.lower() == "yes":
    login = input("Please, enter your login. ")
    password = input("Please, enter your password. ").encode()
    counter = 0

    for i in db.cursor.execute(f"""SELECT password FROM users
                                   WHERE login == '{login}'"""):

        if hashlib.sha3_256(password).hexdigest() == i[0]:
            print("Right!")
        else:
            print("Wrong!")
        counter += 1

    if counter == 0:
        print("Wrong")

print("Would you like to see all users?(yes/no) ")
answer = input()

if answer.lower() == "yes":
    print(f"{'Login': <40}Password")
    for i in db.cursor.execute("SELECT * FROM users"):
        print(f"{i[0]: <39}", i[1])
else:
    print("Your login and password saved successfully!")
