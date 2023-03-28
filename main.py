from db import Database
from user import User
import hashlib
from getpass import getpass

db = Database()
db.create_table_users()
login = input("Create your login: ")
password = getpass("Create your password: ")
user = User(login, password)
db.insert_values(user)

print("Would you like to check your login and password?")
answer = input("yes/no: ")

try:
    if answer.strip().lower() == "yes":
        login = input("Please, etner your login. ")
        password = getpass("Please, enter your password. ").encode()

        pwd = list(db.cursor.execute(f"""SELECT password FROM users
                                   WHERE login == '{login}'"""))[0][0]

        if hashlib.sha3_256(password).hexdigest() == pwd:
            print("Right!")
        else:
            print("Wrong!")

except:
    print("Wrong")

print("Would you like to see all users?(yes/no) ")
answer = input()

try:
    if answer.strip().lower() == "yes":
        print(f"{'Login': <51}Password")
        for i in db.cursor.execute("SELECT * FROM users"):
           print(f"{i[0]: <50}", i[1])
except:
    print("Your login and password saved successfully!")
