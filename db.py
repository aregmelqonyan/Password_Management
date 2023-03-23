import sqlite3
from user import User


class Database:
    __instance = None

    def __new__(cls) -> None:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        self.connection = sqlite3.connect("users.db")
        self.cursor = self.connection.cursor()

    def create_table_users(self) -> None:
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                                login text UNIQUE,
                                password text UNIQUE)""")
        self.connection.commit()

    def insert_values(self, user: User) -> None:
        self.cursor.execute(f"""INSERT INTO users(login, password)
                                VALUES('{user.login}', '{user.password}')""")
        self.connection.commit()
        print("Inserted successfully!")


