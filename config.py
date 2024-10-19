import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()
# ________________________________________________________________________________#
# Get this value from my.telegram.org/apps

API_ID = int(getenv("API_ID","16457832"))
# ________________________________________________________________________________#
API_HASH = getenv("API_HASH","3030874d0befdb5d05597deacc3e83ab")
# Get your token from @BotFather on Telegram.
# ________________________________________________________________________________#
BOT_TOKEN = getenv("BOT_TOKEN", "7614791434:AAEXPgusVY6LT-_TT1Wz9A8ociMGrTXP6so")
# ________________________________________________________________________________#
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# ________________________________________________________________________________#
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ________________________________________________________________________________#
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID","-1002043570167"))
# ________________________________________________________________________________#
# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID","7400383704"))
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "BABY_MUSIC09_BOT")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "╼⃝𖠁 𝐁ʌʙʏ ꭙ 𝐌ᴜsɪᴄ 𖠁⃝╾")
# ________________________________________________________________________________#
# Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ________________________________________________________________________________#
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/TrickBySaqib/Muick",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private
# ________________________________________________________________________________#
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/BABY09_WORLD")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+j6FO8pK8IIkxZDU1")
OWNER_USERNAME = getenv("OWNER_USERNAME", "UTTAM470")
# ________________________________________________________________________________#
# Set this to True if you want the assistant to automatically leave chats
# after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# ________________________________________________________________________________#
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")


# ________________________________________________________________________________#
# Maximum limit for fetching playlist's track from youtube, spotify, apple
# links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", 25))

# ________________________________________________________________________________#

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @YT_STRING_ROBOT on Telegram
STRING1 = getenv("STRING_SESSION", "BQD7IGgAfbOuET-vlHNxqHy9SI1ViB06CSVFeOrDbXJ6Pl3HXWJGeOJFhHzDw1vCPEk6a2pc7bD_4PL_ZGGqWPSrm_DdkAqE0GKtA7uhqFQYEJUxiXLcGxd0bMDqrj-9HnySbYiQ1f_rAmx4ABO8hvAJPAkURnfKCmnwC4S53wGitiopSgT8G5-6XmVde24Q_JPnHcoyjzeofNCQxRN4aW17zuY4KNsZ7_Lk0SRQwaq8eAz8k5aqlgmtWpFgzxTp1yFY6OZDS143HVEg7jr-SyTM2sU5_tSx2HdQfc2g51nulydk2xORxTfv0CfaZoeY1zO4B-5icw2TPwcZOe9DCDOKlpavFgAAAAGugN_jAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


#     _    __      _______ _____    ___  __ _    _  _____ _____ _____   __
#    | |  / /     |__   __|  __ \  |__ \/_ | |  | |/ ____|_   _/ ____| |  __ \ / __ \__   __|
#    | | / /         | |  | |__) |    ) || | |  | | (___   | || |      | |__) | |  | | | |
#    | |/ /          | |  |  ___/    / / | | |  | |\___ \  | || |      |  _  /| |  | | | |
#    | |\ \          | |  | |       / /_ | | |__| |____) |_| || |____  | | \ \| |__| | | |
#    |_| \_\         |_|  |_|      |____||_|\____/|_____/|_____\_____| |_|  \_\\____/  |_|


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
# ________________________________________________________________________________#

# images

START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://telegra.ph/file/219efba204a59b20c3acf.jpg",
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/4fd3faf29006ff3153d39.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://telegra.ph/file/f4edfbd83ec3150284aae.jpg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://telegra.ph/file/de1db74efac1770b1e8e9.jpg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://telegra.ph/file/4dd9e2c231eaf7c290404.jpg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://telegra.ph/file/8234d704952738ebcda7f.jpg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://telegra.ph/file/8d02ff3bde400e465219a.jpg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://telegra.ph/file/e24f4a5f695ec5576a8f3.jpg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://telegra.ph/file/7645d1e04021323c21db9.jpg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://telegra.ph/file/76d29aa31c40a7f026d7e.jpg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://telegra.ph/file/b7758d4e1bc32aa9fb6ec.jpg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://telegra.ph/file/60ed85638e00df10985db.jpg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://telegra.ph/file/f4edfbd83ec3150284aae.jpg",
)

# ________________________________________________________________________________#


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
