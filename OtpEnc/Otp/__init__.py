import loguru
import logging
import time

from pyrogram import Client
from pyroaddon import listen



API_ID = 8526499
MAINTAINANCE = False
API_URL = "https://webapi.ai2api.com"
API_HASH = "e760875a258346ca77329636217dd492"
OTP_API = "pumiIglqdNpd1KlXolr2enSzqOX2x4rm"
TOKEN = "7299892981:AAES5EbH6ik2MKuAP2DUJnBuINkt8dHlPqU"
ALIVE = time.time()
SELLIX1D = ""
SELLIX3D = ""
SELLIX7D = ""
SELLIX28D = ""
BOT_USERNAME = ""
BOT_NAME = ""
OWNERID1 = "" # UNAME
OWNERID2 = "" # UNAME
UPDATES_CHANNEL = ""
SUPPORT_GROUP = ""
GRABS = ""
VOUCHES = ""
UPDATES_ANIMATION = ""
PRIVACY_POLICY = "https://abc.com"
TERMS_AND_CONDITIONS = "https://abc.com"
FAQ = "https://abc.com"
START_ANIM = "https://telegra.ph/file/16fc3f5cf4b58158d7ad2.mp4"
AUDIO_SERVER = "http://20.243.83.96:4000/audio"
WEBHOOK_URL = "http://20.243.83.96:4000/webhook"
# AUDIO_SERVER = "http://117.205.178.189:8000/audio"
# WEBHOOK_URL = "http://117.205.178.189:8000/webhook"
CLAIM_LOGS = -1002031180621
START_LOGS = -1002044413420
ADMINS = [5749343005, 2142595466, 1476937429]
LOGGER = loguru.logger

logging.basicConfig(
     level=logging.INFO, 
     format= '\033[32m%(asctime)s\033[0m |\033[36;1m %(levelname)s \033[0m| \033[31m%(module)s.%(funcName)s:\033[0m\033[35m%(lineno)d | \033[0m - \033[1m%(message)s\033[0m',
     datefmt='%H:%M:%S',
)

otpbot = Client(
    "my_account", 
    api_id=API_ID, 
    api_hash=API_HASH,
    bot_token=TOKEN,
    plugins={"root": "Otp.modules"},
)
helper = Client(
    "helper",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token="7071679215:AAEMaOquFJq_kYhITkbhGmda6xFNfiC1EVQ",
)