import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(".env")

BASE = Path(__file__).parent

# Credentials
REDDIT = {
    "client_id": os.getenv("REDDIT_CLIENT_ID"),
    "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
    "user_agent": "Hello u/bcnevruz",
}

YOUTUBE = {
	'title': '',
	'description': '',
	'tags': '',
	'category': 23,  # has to be an int, more about category below
	'status': ''  # {public, private, unlisted}
}

YOUTUBE_SECRETS_JSON = "client_secret.json" # Download from https://console.cloud.google.com/apis/api/youtube.googleapis.com/credentials?

# Content
SUBREDDIT = "funny"
VIDEO = {
	'resolution': (1080, 1920),  # (horizontal, vertical), currently set vertically for tiktok
	'blur': True  # blur non-perfect-fit clip
}

# Paths
TEMP_DIR = BASE.joinpath("temp_videos")
OUTPUT_DIR = BASE.joinpath("results")