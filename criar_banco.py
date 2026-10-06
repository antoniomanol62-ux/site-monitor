import sqlite3

conexao = sqlite3.connect("sites.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sites (
    id INTERGER PRIMARY KEY,
    name TEXT,
    url TEXT
    
);
""")
conexao.commit()
conexao.commit()
