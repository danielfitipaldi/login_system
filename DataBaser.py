import sqlite3

conn = sqlite3.connect('user_data.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    user VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL

)
""")

print('Conectado ao banco de dados')
