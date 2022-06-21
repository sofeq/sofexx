## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu0vM09BIzT9ZHwGADBrgjg7HfrftZJToNsmnqN0vYIPXarmM50a52pSJ8r5nz9IyCfBFdBec7GIZE_qJhh0-nEzsQj7b_ETmciW4vy4HGPGj5LZPYVtJBBgWmr9T5gOVjMtvQ0Ub_RpxTKwX91u4C5lKK_SLn22z5LCKqrM6R_6VfT1XuVregH4GYVoSOV10NRs7dSJURolr-NgiUXBn0JWgNdAM5B2zLQV-JZppLIiAB4IrFDHLJHWtO5r8R6DeddyxubnwvSlZp0W6VZvFQ6oJD9GDrtTfmpK18x_CU9Tj2UqYw3Pwmq6TnooKoTbaRfx97oBNXmHZIP5JCY-7oE8=")
BOT_TOKEN = getenv("BOT_TOKEN", "5344782186:AAE4VW_FqunLfu5NDBNV3mBJuUobuQdPt_E")
BOT_NAME = getenv("BOT_NAME", "ميوزك")
API_ID = int(getenv("API_ID", "6440669"))
API_HASH = getenv("API_HASH", "fec788c7d1ccdfc9ec507b63818d0970")
OWNER_NAME = getenv("OWNER_NAME", "sofe")
OWNER_USERNAME = getenv("OWNER_USERNAME", "no_nn")
ALIVE_NAME = getenv("ALIVE_NAME", "sofe")
BOT_USERNAME = getenv("BOT_USERNAME", "music7sbot")
OWNER_ID = getenv("OWNER_ID", "1686444936")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "no_nn")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "bc_cb")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "bc_cb")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1686444936").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
