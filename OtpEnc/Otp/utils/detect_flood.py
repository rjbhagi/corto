import time
import random

from pyrogram import Client
from ..modules.database.main_db import SelfDestruct, Maintenance
from .formatters import get_time
from .. import ADMINS


FLOOD_THRESHOLD = 4
TIME_WINDOW = 10
user_message_counts = {}
warn_msg_count = {}
blocked = {}

def detect_flood(user_id: int) -> str:
    current_time = time.time()
    
    global user_message_counts
    user_message_counts = {user: (timestamp, count) for user, (timestamp, count) in user_message_counts.items() if current_time - timestamp <= TIME_WINDOW}

    user_message_counts[user_id] = user_message_counts.get(user_id, (current_time, 0))
    user_message_counts[user_id] = (user_message_counts[user_id][0], user_message_counts[user_id][1] + 1)

    if user_message_counts[user_id][1] > FLOOD_THRESHOLD:
        blocked[user_id] = time.time()
        return "Blocked"
    else:
        return "Not blocked"

def is_blocked(f):
    async def wrapper(bot: Client, m):
        MAINTAINANCE = Maintenance().get_status()[0]
        if MAINTAINANCE == True and m.from_user.id not in ADMINS:
            rnum = random.randint(10, 28)
            since = get_time(float(time.time())-float(Maintenance().get_since()[0]))
            photo = "https://telegra.ph/file/c3fc0ef2151d0ff5575a0.jpg"
            await m.reply_photo(photo=photo, caption=f"🚫 Bot is under maintenance.\n📅 Since: {since}. Please try again later.\n\nMeanwhile listen ⬇️ and chill 🍀")
            return await bot.forward_messages(m.chat.id, from_chat_id=-1002050961839, message_ids=rnum)
        if SelfDestruct().get_status()[0] == 0:
            await m.reply_text("Bot has self destructed itself. Exiting...")
            exit("Self destructed. Exiting...")
        try:
            user_id = m.from_user.id
        except:
           return
        if user_id in blocked:
            release_time = 600 - (time.time() - blocked[user_id])  # 10 minutes
            global warn_msg_count
            if release_time <= 0:
                del blocked[user_id]
                await f(bot, m)
            else:
                if user_id not in warn_msg_count:
                    warn_msg_count[user_id] = 3
                if warn_msg_count[user_id] <= 0:
                    return
                else:
                    await m.reply(f"You have been blocked due to message flood. You will be released in {int(release_time)} seconds.\n\nThis warning message will be displayed only {warn_msg_count[user_id]} times")
                    warn_msg_count[user_id] -= 1
        else:
            await f(bot, m)
    return wrapper
