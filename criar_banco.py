import sqlite3

conexao = sqlite3.connect("sites.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sites (
    id INTEGER PRIMARY KEY,
    name TEXT,
    url TEXT UNIQUE
    
);
""")
conexao.commit()
conexao.close()

