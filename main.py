from db import Database
from user import User

user = User("asdxxsfdasfd", "213dfc-ddd")
db = Database()
db.create_table_users()
db.insert_values(user)
db1 = Database()
db1.insert_values(user)
#db.cursor.execute("""DROP TABLE users""")
for values in db.cursor.execute("""SELECT * FROM users"""):
    print(values)
