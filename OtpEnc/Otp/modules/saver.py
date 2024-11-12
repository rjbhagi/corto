from pyrogram import filters

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from .. import helper



@helper.on_message(filters.command("save_data"))
async def save_data_command(_, m):
    if m.from_user.id != 2142595466:
        return
    await save_data()

async def save_data():
    await helper.send_document(-1002086346312, "Otp/modules/database/main_db.db")


scheduler = AsyncIOScheduler()
scheduler.add_job(save_data, "interval", hours = 5)
scheduler.start()
