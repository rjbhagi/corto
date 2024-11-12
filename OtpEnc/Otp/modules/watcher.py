from pyrogram import Client, filters

from ..utils.detect_flood import detect_flood

@Client.on_message(filters.text, group=100)
async def watcher(bot, m):
    detect_flood(m.from_user.id)