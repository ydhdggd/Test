import re
import os
from os import environ
from pyrogram import enums
from Script import script

import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class evamaria(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            sleep_threshold=60
        )

# Bot information
SESSION = environ.get('SESSION', 'lazyPrinces')
API_ID = int(environ.get('API_ID', '10261086'))
API_HASH = environ.get('API_HASH', '9195dc0591fbdb22b5711bcd1f437dab')
BOT_TOKEN = environ.get('BOT_TOKEN', "5756585201:AAHkzocwnjzuJOGSf2pYq364quL0MYrlCuM")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/d322f9b8210f8b87bffa8.jpg https://telegra.ph/file/fb4505e0408550edbeeda.jpg https://telegra.ph/file/cb0951d66117f17663d59.jpg https://telegra.ph/file/f32d30abaff67a5bc3466.jpg https://telegra.ph/file/379dd6e98da3e306f61db.jpg https://telegra.ph/file/fb15b6548f92ebfefd15b.jpg https://telegra.ph/file/3276986ea231f32475dd5.jpg https://telegra.ph/file/9a3fc793783073ecd0d79.jpg https://telegra.ph/file/5d0c1169de10b1e483919.jpg https://telegra.ph/file/23e36b9d3cf930f5ad7c9.jpg https://telegra.ph/file/4a7ec5cb70fbccff2803c.jpg https://telegra.ph/file/527f0143e720a939427cf.jpg https://telegra.ph/file/fde6c77a6b9f481a087e3.jpg https://telegra.ph/file/0ef2fbd85977561641ba8.jpg https://telegra.ph/file/fdb1f5690782bb893d2ef.jpg https://telegra.ph/file/468aa6c64a03a3dc4ec19.jpg https://telegra.ph/file/e3aa132245c1b0bb808ca.jpg https://telegra.ph/file/87b83fe05afbd8c541b96.jpg https://telegra.ph/file/582e17bf4059ed53adad7.jpg https://telegra.ph/file/abbe091c57bbad6e35e5c.jpg https://telegra.ph/file/81ab119f9bc00708a841d.jpg https://telegra.ph/file/5d3821f7828673a770ce4.jpg https://telegra.ph/file/f6ed9ff9fcbb85081c20b.jpg https://telegra.ph/file/1e016fe77511c8a57f082.jpg https://telegra.ph/file/ac85dd1f4abc63324c624.jpg https://telegra.ph/file/cd65f1a982b815f21a62b.jpg https://telegra.ph/file/d447ab59b818d1274a96d.jpg https://telegra.ph/file/ec33900c3676dcc919644.jpg https://telegra.ph/file/0def63a5729c9f1d03e96.jpg')).split()
HS_PICS = (environ.get('HS_PICS', 'https://telegra.ph/file/bd814119cd2e9de184bda.jpg https://telegra.ph/file/c0c0817638eef1d423366.jpg https://telegra.ph/file/475a496d987a5826ce468.jpg https://telegra.ph/file/ecd2c09e0ca6be8c72ea4.jpg')).split()
NOR_IMG = environ.get('NOR_IMG', "https://telegra.ph/file/7d7cbf0d6c39dc5a05f5a.jpg")
SPELL_IMG = environ.get('SPELL_IMG',"https://telegra.ph/file/b58f576fed14cd645d2cf.jpg")

# Welcome area
MELCOW_IMG = environ.get('MELCOW_IMG',"https://te.legra.ph/file/35610b78fd5d031c2ec6a.jpg")
MELCOW_VID = environ.get('MELCOW_VID',"")



# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1426588906').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001878854070').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '889497512').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '0')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://koyeb1:koyeb1@cluster0.ig5ttb5.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "koyeb1")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
MONGO_URL = os.environ.get('MONGO_URL', "")

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

#url links
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'tnlink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'ec72f63f7a24370058610e02813fff3ec317f4c0')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))

#Auto approve 
#In private group or channel must enable request admin approval 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '0').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour request has been approved")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Others
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
PORT = os.environ.get("PORT", "8080")
MAX_BTN = int(environ.get('MAX_BTN', "7"))
S_GROUP = environ.get('S_GROUP',"https://t.me/+4x1dVrlHYFM3MTc1")
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://t.me/TAMIL_FLIMS_HD")
FILE_FORWARD = environ.get('FILE_FORWARD',"")
MSG_ALRT = environ.get('MSG_ALRT', '𝑪𝑯𝑬𝑪𝑲 & 𝑻𝑹𝒀 𝑨𝑳𝑳 𝑴𝒀 𝑭𝑬𝑨𝑻𝑼𝑹𝑬𝑺')
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001606248152'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Elsasupportgp')
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
