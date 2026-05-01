import time
from db import SessionLocal, engine
from models import Video, Base
from youtube_api import fetch

Base.metadata.create_all(bind=engine)

VIDEO_IDS = [
    "UZKjfwD8dkw"
]

def run():
    db = SessionLocal()

    for vid in VIDEO_IDS:
        exists = db.query(Video).filter(Video.video_id == vid).first()
        if exists:
            continue

        meta = fetch(vid)
        if not meta:
            continue

        db.add(Video(
            video_id=vid,
            title=meta["title"],
            channel=meta["channel"],
            thumbnail=meta["thumbnail"]
        ))

    db.commit()
    db.close()

while True:
    run()
    time.sleep(60)