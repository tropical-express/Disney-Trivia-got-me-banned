import threading
import uvicorn

from scraper import run_scraper
from db import Base, engine
import models

# Create DB tables
Base.metadata.create_all(bind=engine)


def start_scraper():
    run_scraper()


threading.Thread(target=start_scraper, daemon=True).start()

uvicorn.run(
    "api:app",
    host="0.0.0.0",
    port=8000
)