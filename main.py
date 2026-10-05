from fastapi import FastAPI

app = FastAPI(title="Site Monitor")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/sites")
def listar_sites():
    return [
        {"id": 1, "name": "Example", "url": "https://example.com"},
        {"id": 2, "name": "Example Org", "url": "https://example.org"},
    ]