from sqlalchemy import Column, String, Integer
from db import Base

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)
    video_id = Column(String, unique=True, index=True)

    title = Column(String)
    channel = Column(String)
    thumbnail = Column(String)