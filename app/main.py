from fastapi import FastAPI
from sqlalchemy import text
from database import engine
from redis_client import redis_client


app = FastAPI(title="AI Backend API")


@app.get("/")
def home():
    return {"message": "AI Backend is running!"}


@app.get("/health")
def health():

    db_status = "down"
    redis_status = "down"

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception:
        pass

    try:
        redis_client.ping()
        redis_status = "connected"
    except Exception:
        pass

    return {
        "status": "healthy",
        "database": db_status,
        "redis": redis_status,
    }
