from fastapi import FastAPI

app = FastAPI(title="Site Monitor")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("____")
def ____():
    return [
        {"id": 1, "name": "____", "url": "____"},
        {"id": 2, "name": "____", "url": "____"},
    ]