import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials
API_ID = int(getenv("API_ID", "16457832"))
API_HASH = getenv("API_HASH", "3030874d0befdb5d05597deacc3e83ab")
BOT_TOKEN = getenv("BOT_TOKEN", "7453423431:AAEP3MUFCKyyCzIgRowY_9MQdaiY82JHBCk")

# MongoDB URI for storing data
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://TrickBy:TrickBy87554412@cluster0.hev6dq9.mongodb.net/")

# Maximum song duration limit in minutes
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Logging configuration
LOGGER_ID = int(getenv("LOGGER_ID", "-1002022622141"))
OWNER_ID = int(getenv("OWNER_ID", "6625936112"))

# Bot and user settings
BOT_USERNAME = getenv("BOT_USERNAME", "BABY_MUSIC09_BOT")
BOT_NAME = getenv("BOT_NAME", "╼⃝𖠁 𝐁ʌʙʏ ꭙ 𝐌ᴜsɪᴄ 𖠁⃝╾")

# Deployment configurations (Heroku)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# GitHub repository details for updates
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TrickBySaqib/Muick")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support information
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ll_Bot_Promotion_ll")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+aTJJeCRGKac0MTU1")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@ll_Oye_Zayn_ll")

# Spotify API credentials (optional)
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")

# Limit for fetching playlist tracks
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", 25))

# File size limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))  # 100 MB
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))  # 1 GB

# String sessions for managing multiple sessions
STRING1 = getenv("STRING_SESSION", "BQD7IGgAfbOuET-vlHNxqHy9SI1ViB06CSVFeOrDbXJ6Pl3HXWJGeOJFhHzDw1vCPEk6a2pc7bD_4PL_ZGGqWPSrm_DdkAqE0GKtA7uhqFQYEJUxiXLcGxd0bMDqrj-9HnySbYiQ1f_rAmx4ABO8hvAJPAkURnfKCmnwC4S53wGitiopSgT8G5-6XmVde24Q_JPnHcoyjzeofNCQxRN4aW17zuY4KNsZ7_Lk0SRQwaq8eAz8k5aqlgmtWpFgzxTp1yFY6OZDS143HVEg7jr-SyTM2sU5_tSx2HdQfc2g51nulydk2xORxTfv0CfaZoeY1zO4B-5icw2TPwcZOe9DCDOKlpavFgAAAAGugN_jAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Image URLs for various bot functions
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/219efba204a59b20c3acf.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/4fd3faf29006ff3153d39.jpg")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "https://telegra.ph/file/f4edfbd83ec3150284aae.jpg")
GLOBAL_IMG_URL = getenv("GLOBAL_IMG_URL", "https://telegra.ph/file/de1db74efac1770b1e8e9.jpg")
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://telegra.ph/file/4dd9e2c231eaf7c290404.jpg")
YOUTUBE_IMG_URL = "https://telegra.ph/file/76d29aa31c40a7f026d7e.jpg"


# Duration limits for songs in seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Ensure correct URL formats for support channels and chat
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong. It must start with https://")

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is wrong. It must start with https://")

# Bot user and session management
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Additional settings for bot behavior
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Debugging helpers and logging
print("Configuration loaded successfully.")

