# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28316155"))
API_HASH = getenv("API_HASH", "e3499ac331a8df93997c1680366f2327")
BOT_TOKEN = getenv("BOT_TOKEN", "7093608856:AAHE86oSFT3jA1JlS7C6z5nUuVtvt9_d7K4")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1970647198").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://janezimpuenio:pPZqoHnziVesiE5X@cluster0.c7e4w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002183779903")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002178727651"))
