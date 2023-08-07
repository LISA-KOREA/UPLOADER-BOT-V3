import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = "6324971780:AAG4-mSR0OH7L3_lfKabflLtzDiekV0wGQ4"

    API_ID = "26489380"

    API_HASH = "4167d8b8779aab33b73810feb3c77021"

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @UploadLinkToFileBot"

    DATABASE_URL = "mongodb+srv://UploadBot:Aail7172@cluster0.bjeypjj.mongodb.net/?retryWrites=true&w=majority"

    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")

    LOG_CHANNEL = "1472839541"

    LOGGER = logging

    OWNER_ID = "932420516"

    UPDATES_CHANNEL = "Al_Noor_TV"
    
    BOT_USERNAME = "Urxxrufjxtxjrudrsybot"
