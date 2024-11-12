from pyrogram import Client, filters

from .database.main_db import TTS
from ..utils.devsonly import is_admin


@Client.on_message(filters.command("tits"))
@is_admin
async def add_tts(bot: Client, m):
    key = m.text[len("/tits ") :]
    if key == "":
        await m.reply("format is /tits key")
    TTS().add_key(key)
    await m.reply("Insert successful.")
