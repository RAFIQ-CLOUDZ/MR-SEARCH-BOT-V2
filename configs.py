# (c) @AM_ROBOTS

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is @MROTTTamilOffl Search Bot.
    
    
    
🤖 My Name: <a href='https://t.me/MROTTTamilOffl'>MROTTTamilOffl Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/MROTTTamilOffl'>MROTTTAMILOFFL</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/MR_X_MIRROR'>𝙰𝚗𝚘𝚗𝚢𝚖𝚘𝚞𝚜</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm @MROTTTamilOffl Search Bot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤️‍🔥 By @MROTTTamilOffl</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm @MROTTTamilOffl Search Bot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤️‍🔥 By @MROTTTamilOffl</a></b>
"""
