import asyncio


from pyrogram import Client, filters
from pyrogram.types import Message

from .database.main_db import Users
from ..utils.devsonly import is_admin


@Client.on_message(filters.command("broadcast"))
@is_admin
async def broadcast(bot: Client, m: Message):
    if len(m.text[len("/broadcast ") :]) < 10 and not m.reply_to_message:
        await m.reply_text("Usage: /broadcast message")
        return
    msg = m.text[len("/broadcast ") :]
    if m.reply_to_message:
        users = Users().get_all_users()
        count = 1
        for user in users:
            try:
                await bot.forward_messages(user[0], m.chat.id, m.reply_to_message.id)
            except Exception as e:
                print(f"An error occurred while sending message to {user[0]}. Error: {e}")
            else:
                count += 1
            await asyncio.sleep(3)
        await m.reply_text(f"Broadcast completed to {count} users.")
    else:
        users = Users().get_all_users()
        count = 1
        for user in users:
            try:
                await bot.send_message(user[0], msg)
            except Exception as e:
                print(f"An error occurred while sending message to {user[0]}. Error: {e}")
            else:
                count += 1

            await asyncio.sleep(3)
        await m.reply_text(f"Broadcast completed to {count} users.")

