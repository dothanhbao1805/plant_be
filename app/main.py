from fastapi import FastAPI
from app.routers import users

app = FastAPI(title="My App", version="0.1.0")
app.include_router(users.router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok"}
