import sqlite3

from fastapi import FastAPI

app = FastAPI(title="Site Monitor")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/sites")
def listar_sites():
    conexao = sqlite3.connect("sites.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id, name, url FROM sites")
    linhas = cursor.fetchall()
    conexao.close()

    resultado = []
    for linha in linhas:
        resultado.append({"id": linha[0], "name": linha[1], "url": linha[2]})
    return resultado
