from fastapi import FastAPI
from db import SessionLocal
from models import Video

app = FastAPI()

@app.get("/videos")
def get_videos():
    db = SessionLocal()
    try:
        return db.query(Video).all()
    finally:
        db.close()