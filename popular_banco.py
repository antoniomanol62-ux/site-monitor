import sqlite3

conexao = sqlite3.connect("sites.db")
cursor = conexao.cursor()

cursor.execute("""
INSERT INTO sites (name, url) VALUES ('Example', 'https://example.com');
""")

cursor.execute("""
INSERT INTO sites (name, url) VALUES ('Example Net', 'https://example.net');
""")

conexao.commit()

cursor.execute("SELECT * FROM sites")
print(cursor.fetchall())

conexao.close()
