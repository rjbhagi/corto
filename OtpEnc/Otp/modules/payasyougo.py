import random

from pyrogram import Client, filters
from pyrogram.types import (
    Message, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup
)

from .. import BOT_USERNAME, BOT_NAME, OWNERID1, OWNERID2
from .database.main_db import PayAsYouGo, Login
from ..Email.email import sendEmail
from ..Subscription.prices import prices
from ..utils.decorators import blacklist
from ..utils.detect_flood import is_blocked






text = f"""
🔐 {BOT_NAME} OTP Bot 🤖💬

✨ Pay-as-you-Go! {BOT_NAME} OTP is the #1 OTP Bot that offers a pay-as-you-go option in its OTP bot. - Pay for what you use! 📲

📄 Features:
- 🌐 Global access
- 🕒 Time-based billing
- 🤑 Affordable rates
- Per miniute billing is 0.14 (min starting) and there are also call receive charge (0.05 for all countries), if call was received.
The price list will be displayed on the Pay-As-You-Go profile. ☎️


💳 To Load Balance:
Contact the Bot Admins 📞🔥

Taking otp bots to another level! 🚀🔑

To set up your pay-as-you-go profile, simply tap the button below. 👇"""

@Client.on_message(filters.command("payasyougo"))
@blacklist
@is_blocked
async def payasyougo(bot, m: Message):
    user_id = m.from_user.id
    is_logged = Login().get_user(user_id)
    if is_logged == None:
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔑 sign-up 🔑", callback_data=f"register_{user_id}")
                ]
            ]
        )
        await m.reply_text("Please sign-up using an email to verify yourself.", reply_markup=btn)
        return
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("My Profile 📝", callback_data="profile1")
            ]
        ]
    )
    await m.reply_photo(photo="https://telegra.ph/file/f13cd4ceb591e49393aa1.jpg", caption=text, reply_markup=btn)


@Client.on_callback_query(filters.regex("profile1"))
async def profile(bot, q):
    user_id = q.from_user.id
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Load Balance 💳", callback_data="load_balance")
            ],
            [
                InlineKeyboardButton("Back 🔙", callback_data="start_back")
            ]
        ]
    )
    try:
        balance = round(PayAsYouGo().get_user(user_id)[1], 2)
    except:
        balance = 0
    text = f"Your details:\n\n> **Name**: {q.from_user.first_name}\n> **ID**: {q.from_user.id}\n> **Balance**: {balance}\n\nClick on button below to load balance."
    await q.message.edit_text(text, reply_markup=btn)


ver = """
🔐 {} OTP Bot 🤖💬

Hey {} User,

Thanks for joining the ranks! 🚀 To secure your base and confirm your email, input this top-secret code: 

🔐 Verification Code: {}

This code will self-destruct 🧨 in 30 minutes. Use it on the verification page to proceed.

If this mission wasn't initiated by you, ignore this message or contact support.

Over and out,  
🤖 {} OTP Bot Support Team
"""
verification_done = """
Dear {},

Mission Accomplished! 🎯 Your email has been verified.

If you have any queries, do not hesitate to signal our support team. 📞

Welcome to the squad! We're thrilled to have you on this covert journey with us! 🚀

Signing off,  
**🤖 {BOT_NAME} OTP Bot | {BOT_NAME} OTP Support Team**
"""
@Client.on_callback_query(filters.regex("register_(.*)"))
async def register(bot, q):
    user_id = int(q.data.split("_")[1])
    await q.message.edit_text("Starting verification process...")
    email = await q.message.chat.ask("Please enter your email address to sign-up: ")
    email = email.text
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    n3 = random.randint(0, 9)
    n4 = random.randint(0, 9)
    code = int(f"{n1}{n2}{n3}{n4}")
    success = sendEmail(ver.format(BOT_NAME, BOT_NAME, code), "Email Verification 👻", email)
    if success  == True:
        vcode = await q.message.chat.ask("🔐 A secret code 🕵️‍♂️ has been Sent to your email 📧. \nKindly enter it below to unlock full access 🔓 **(Please check spam box)**")
    else:
        return await q.message.reply("An error occurred while sending the email 🥲. Please inform developer..")
    try:
        vcode = int(vcode.text)
    except:
        return await q.message.reply("The verification code you entered is incorrect. Please try again later. ❌")
    if code == vcode:
        Login().add_user(user_id, email)
        await q.message.reply_photo(photo="https://telegra.ph/file/a432cbd01cb18d8ba74ba.jpg", caption=verification_done.format(q.from_user.first_name, BOT_NAME))
    else:
        await q.message.chat.ask("The verification code you entered is incorrect. Please send the correct code: ❌")
        if code == vcode:
            Login().add_user(user_id, email)
            await q.message.reply_photo(photo="https://telegra.ph/file/a432cbd01cb18d8ba74ba.jpg", caption=verification_done.format(q.from_user.first_name, BOT_NAME))
        else:
            await q.message.reply("The verification code you entered is incorrect. Please try again later. ❌")



text = f"""
- ${prices['INDIA']} per minute for INDIA 🇮🇳
- ${prices['USA']} per minute for USA 🇺🇲
- ${prices['BRAZIL']} per minute for Brazil & Italy 🇧🇷🇮🇹
- ${prices['FINLAND']} per minute for Finland 🇫🇮
- ${prices['FRANCE']} per minute for France 🇫🇷
- ${prices['SPAIN']} per minute for Spain 🇪🇦
- ${prices['SWEDEN']} per minute for Sweden 🇸🇪


    🍁 Minimum Load - $5 🍁
"""

@Client.on_callback_query(filters.regex("load_balance"))
async def load_balance(bot, q):
    user_id = q.from_user.id
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Inbox owner", url=f"https://t.me/{OWNERID1}?text=I%20want%20to%20load%20balance%20on%20{BOT_NAME}%20otp%20bot")
            ],
            [
                InlineKeyboardButton("Inbox owner1", url=f"https://t.me/{OWNERID2}?text=I%20want%20to%20load%20balance%20on%20{BOT_NAME}%20otp%20bot")
            ],
            [
                InlineKeyboardButton("back", callback_data="profile1")
            ]
        ]
    )
    await q.message.edit_text(text, reply_markup=btn)