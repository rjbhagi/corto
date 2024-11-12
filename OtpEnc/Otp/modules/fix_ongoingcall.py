from pyrogram import Client, filters

from .database.main_db import Verification, ConcurrentCalls

from ..utils.devsonly import is_admin



@Client.on_message(filters.command("fix"))
@is_admin
async def fix_(bot, m):
    user_id = await m.chat.ask("Enter the user id: ")
    try:
        user_id = int(user_id.text)
    except ValueError:
        await m.reply("Invalid user id, please try again.")
        return
    try:
        user = Verification().update_status(user_id, 0)
    except Exception as e:
        await m.reply(f"An error occurred: {e}")
        return
    try:
        xd1 = ConcurrentCalls().update_calls(user_id, 0)
    except Exception as e:
        await m.reply(f"An error occurred: {e}")
        return
    await m.reply(f"User status has been reset successfully, with status: \n\n> {user}\n> {xd1}")