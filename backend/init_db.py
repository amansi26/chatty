import sqlite3

dbs = {'user_creation.sql': 'user_creation.db',
       'msg.sql': 'message_info.db'}

for db, sql in dbs.items():
    connection = sqlite3.connect(sql)

    with open(db) as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()
