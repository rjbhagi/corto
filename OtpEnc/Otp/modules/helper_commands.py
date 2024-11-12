import time
import random
import requests


from pyrogram import filters
from pyrogram.types import Message

from ..utils.decorators import blacklist
from ..utils.devsonly import is_admin
from ..utils.formatters import get_time
from .database.main_db import Maintenance
from .. import helper, ALIVE, API_URL, BOT_USERNAME



@helper.on_message(filters.command("test"))
@blacklist
@is_admin
async def maintenance(bot, m: Message):
    try:
        m.text.split()[1]
    except:
        return await m.reply("Invalid argument. Please use 'on' or 'off'.")
    if m.text.split()[1].lower() == "on":
        await m.reply("Maintenance mode is now enabled.")
        Maintenance().update_status(1)
        Maintenance().update_since(time.time())
    elif m.text.split()[1].lower() == "off":
        await m.reply("Maintenance mode is now disabled.")
        Maintenance().update_status(0)
        Maintenance().update_since(0)
    else:
        await m.reply("Invalid argument. Please use 'on' or 'off'.")

@helper.on_message(filters.command("start"))
async def start(bot, m):
    await m.reply(f"I am a helper bot for @{BOT_USERNAME}, designed solely for backend operations. For inquiries, please reach out to the bot's owner/developer.")


@helper.on_message(filters.command("id"))
@blacklist
async def id(bot, m):
    if m.reply_to_message:
       return await m.reply(f"**User ID:** `{m.reply_to_message.from_user.id}`\n**Chat ID:** `{m.chat.id}`")
    await m.reply(f"**Your ID is**: `{m.from_user.id}`\n**Chat ID:** `{m.chat.id}`")


@helper.on_message(filters.command("alive"))
async def alive(bot, m: Message):
    t1 = time.time()
    data = {
            "call_id": "tghgfyh45545",
            "callbackurl": f"https://google.com",
    }
    response = requests.post(f"{API_URL}/v2/hangup", json=data)
    status_code = response.status_code
    t2 = time.time() - t1
    response_time = f"{t2:.2}s"
    if status_code == 200 or response.json()["success"] == False:
        api_status = f"--**Api status:**--\n• **Status:** Online 🍏\n• **Response time:** {response_time} 👾\n> A response time greater than 1s means Api might be facing some issues. 🙊"
    else:
        api_status = f"--**Api status:**--\n• **Status:** Down 🍎\n• **Response time:** {response_time} 👾\n> Dekh Bhai bkc Mt kr Api down h toh mai kya kru!? 🤚"
    uptime = get_time(time.time() - ALIVE)
    photo = random.choice(["https://telegra.ph/file/8e2f25582f9f88ebff372.jpg", "https://telegra.ph/file/135aed648af99d06d468c.jpg", "https://telegra.ph/file/816b5bd0464b901353b22.jpg", "https://telegra.ph/file/8a8a9b876fc69221494d1.jpg", "https://telegra.ph/file/fcea3b3deb354ddd3928a.jpg", "https://telegra.ph/file/9902e77a41c570ed650cb.jpg"])
    await m.reply_photo(photo=photo, caption=f"**Yep @{BOT_USERNAME} Alive since {uptime}!!** 👻\n\n{api_status}")
