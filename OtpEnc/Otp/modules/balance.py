from pyrogram import Client, filters

from pyrogram.types import Message

from .database.main_db import Subscription, PayAsYouGo
from ..utils.decorators import blacklist
from ..utils.detect_flood import is_blocked



@Client.on_message(filters.command("balance"))
@blacklist
@is_blocked
async def balance(bot, m: Message):
    user_id = m.from_user.id
    try:
        sub = Subscription().get_plan(user_id)[0]
    except:
        return await m.reply_text("You are not subscribed to any plan")
    if sub != "pay_as_you_go":
        return await m.reply_text("You are not subscribed to pay as you go plan")
    else:
        balance = PayAsYouGo().get_user(user_id)[1]
        await m.reply_text(f"Your balance is: ${balance} 💰")