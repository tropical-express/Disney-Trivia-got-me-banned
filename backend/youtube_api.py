import requests
import os

API_KEY = os.getenv("YOUTUBE_API_KEY")

def fetch(video_id):
    url = "https://www.googleapis.com/youtube/v3/videos"

    r = requests.get(url, params={
        "part": "snippet",
        "id": video_id,
        "key": API_KEY
    }).json()

    if not r.get("items"):
        return None

    s = r["items"][0]["snippet"]

    return {
        "title": s["title"],
        "channel": s["channelTitle"],
        "thumbnail": s["thumbnails"]["high"]["url"]
    }