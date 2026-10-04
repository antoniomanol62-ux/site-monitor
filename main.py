from fastapi import FastAPI

app = FastAPI(title="Site Monitor")

@app.get("/health")
def health():
    return {"status": "ok"}
