from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = "mongodb+srv://sumitsajwan135:<gameno01>@cluster0.ja0i0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" [str, ""]
        API_HASH = "ccbc3f662735abfa604ef6309ba76e67" [str, "abcdedf......"]
        API_ID =22403100 [int, 1234567]
        BOT_TOKEN = "7893557735:AAGCyD-fn7wquISaOKYuAuxZdgFEu1HIhmY" [str, "bot:token here"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE =True [bool, False]
        AUTH_USERS = [list,[123456789]]
        OWNER_ID =6894836133 [int, 0]

        # Public username url or invite link of private chat
        FORCEJOIN = "https://t.me/Anime_Piras" [str,""]
        FORCEJOIN_ID =-1002138894327 [int,-100123465978]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
