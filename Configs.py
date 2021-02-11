import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    API_HASH = os.environ.get("API_HASH", "hfcdgv3656hshs")
    API_ID = int(os.environ.get("API_ID", 6))
    ACCOUNT_GEN_NAME = os.environ.get("ACCOUNT_GEN_NAME", "Mail access")
    JTU_ENABLE = os.environ.get("JTU_ENABLE", True)
    CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME", None)
    CHANNEL_URL = os.environ.get("CHANNEL_URL", "https://t.me/O1_007")
    DUMB_CHAT = int(os.environ.get("DUMB_CHAT", False))
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    GEN_LIMIT_PERDAY = int(os.environ.get("GEN_LIMIT_PERDAY", 2))
