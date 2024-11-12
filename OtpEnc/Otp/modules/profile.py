from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from .database.main_db import PayAsYouGo, Subscription, CallLogs, HandleDateTime
from ..utils.decorators import blacklist
from ..utils.detect_flood import is_blocked




@Client.on_message(filters.command("plan"))
@blacklist
@is_blocked
async def iplan_(bot, m: Message):
    user_id = m.from_user.id
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🔱 Plan 🔱", callback_data="main_profile"),
            ],
        ]
    )
    await m.reply_text("Hey there, which one would you like to get? ✨ ✨", reply_markup=btn)


@Client.on_message(filters.command("profile"))
@blacklist
@is_blocked
async def profile_(bot, m: Message):
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🔱 Main Profile 🔱", callback_data="main_profile"),
            ],
            [
                InlineKeyboardButton("🛡️ Pay as you go 🛡️", callback_data="profile_r2")
            ]
        ]
    )
    await m.reply_text("Hey there, which one would you like to get? ✨? ✨", reply_markup=btn)


@Client.on_callback_query(filters.regex("^profile_back$"))
async def profile_back(bot, q: Message):
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🔱 Main Profile 🔱", callback_data="main_profile"),
            ],
            [
                InlineKeyboardButton("🛡️ Pay as you go 🛡️", callback_data="profile_r2")
            ]
        ]
    )
    await q.message.edit_text("Hey there, which one would you like to get? ✨", reply_markup=btn)


@Client.on_callback_query(filters.regex("^profile_r2$"))
async def profile_r2(bot, q):
    user_id = q.from_user.id
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Load Balance 💳", callback_data="load_balance")
            ],
            [
                InlineKeyboardButton("Back 🔙", callback_data="profile_back")
            ]
        ]
    )
    try:
        balance = round(PayAsYouGo().get_user(user_id)[1], 2)
    except:
        balance = 0
    try:
        usage = PayAsYouGo().get_user_usage(user_id)
    except:
        usage = 0
    try:
        total_calls = PayAsYouGo().get_user_total_calls(user_id)
    except:
        total_calls = 0
    
    if usage == None:
        usage = 0
    if total_calls == None:
        total_calls = 0
    try:
        otp_captured = CallLogs().get_otp(user_id)[0]
    except:
        otp_captured = 0
    text = f"""🍀 --**Your details**-- 🍀
👤 Username: {q.from_user.mention}
🆔 Userid: {q.from_user.id}

--**📅 Subscription details**--: 
📆 Plan: Pay as You Go
💳 Remaining Credits: {balance}

📞 --**Calling details**--:
📞 Total Calls: {total_calls}
📱 OTP Captured: {otp_captured}"""
    # text = f"🍀 Your details: 🍀\n\n> **Name**: {q.from_user.first_name}\n> **ID**: {q.from_user.id}\n> **Balance**: {balance}\n> **Total credit usage**: {usage:.2f}\n> **Total calls**: {total_calls} \n\nClick on button below to load balance."
    await q.message.edit_text(text, reply_markup=btn)


@Client.on_callback_query(filters.regex("^main_profile$"))
async def main_prof(bot, q):
    user_id = q.from_user.id
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Back 🔙", callback_data="profile_back")
            ]
        ]
    )
    try:
        plan = Subscription().get_plan(user_id)[0]
    except:
        plan = "You don't have any active plans\n\nuse /purchase to get one."
    # if plan != "Expired" or plan != "You don't have any active plans\n\nuse /purchase to get one.":
    #     expiry = HandleDateTime().get_expiry_date_from_db(user_id)
    # else:
    #     expiry = "Null"
    try:
        calls = CallLogs().get_calls(user_id)[0]
    except:
        calls = 0
    try:
        otp_captured = CallLogs().get_otp(user_id)[0]
    except:
        otp_captured = 0
    print(plan, calls, otp_captured)
    # await q.message.edit_text(f"Your profile 🍀\n\n> Name: {q.from_user.mention}\n> ID: {q.from_user.id}\n> Subscription: {plan}\n> Total calls: \n> Otp captured: {otp_captured}", reply_markup=btn)
    msg = f"--**Profile Details**--🍀\n📛 **UserName**: {q.from_user.mention}\n🪪 **ID**: {q.from_user.id}\n\n📅 --**Subscription Details**--\n📅 **Plan**: {plan}\n🗝️ **Key**: {otp_captured}\n🔃 **Redemption Date:** {HandleDateTime().get_activation_date_from_db(user_id)}\n⌛ **Expiry date**: {HandleDateTime().get_expiry_date_from_db(user_id)}\n\n📞 --**Calling Details**--:\n📞 **Total Calls:** {calls}\n📱**Otps Captured:** {otp_captured}"
    await q.message.edit_text(msg, reply_markup=btn)