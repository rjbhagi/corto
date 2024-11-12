from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


from .. import (
    VOUCHES, 
    GRABS, 
    SUPPORT_GROUP, 
    UPDATES_CHANNEL,
    BOT_USERNAME,
    UPDATES_ANIMATION,
    BOT_NAME
)
from ..utils.devsonly import is_admin



text = f"{BOT_NAME} OTP Updates 🚀 : Dive into the world of {BOT_NAME} with our channel, where we bring you comprehensive coverage of all updates, features, and news related to this cutting-edge technology. Stay informed and up-to-date with the latest advancements, ensuring you never miss a beat. From new features that enhance your experience to important announcements that shape the future of {BOT_NAME}, we've got you covered. Join our community of enthusiasts and experts to discuss, learn, and explore the endless possibilities of {BOT_NAME}. Experience the future of security with {BOT_NAME} Updates. 🛡"
@Client.on_message(filters.command("promo"))
@is_admin
async def promo(bot, m):
    """"""
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Updates 🚀", url=f"https://t.me/{UPDATES_CHANNEL}"),
                InlineKeyboardButton("Community ✨", url=f"https://t.me/{SUPPORT_GROUP}")
            ],
            [
                InlineKeyboardButton("Otp Grabs 🎁", url=f"https://t.me/{GRABS}"),
                InlineKeyboardButton("Vouches 📦", url=f"https://t.me/{VOUCHES}")
            ],
            [
                InlineKeyboardButton("Bot 👻", url=f"http://t.me/{BOT_USERNAME}"),
            ]
        ]
    )
    await bot.send_video(chat_id=m.chat.id, caption=text, video=UPDATES_ANIMATION, reply_markup=btn)