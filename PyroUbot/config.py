import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "48475277").split()))

API_ID = int(os.getenv("API_ID", "25173191"))

API_HASH = os.getenv("API_HASH", "98047b45b5940a7961a5f4dd3a907448")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7048869311:AAFOUDvJhnpMNn7GM4vz35fioWevBot2iaE")

OWNER_ID = int(os.getenv("OWNER_ID", "48475277"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://aldiusulu283:userbot112233@cluster0.6fbhre1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("-1002451288570"))

USER_GROUP = os.getenv("USER_GROUP", "@MonsteryUbot")
