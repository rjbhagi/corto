import random
import string

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from .. import BOT_USERNAME
from ..utils.devsonly import is_admin
from .database.main_db import LicenseKeys



def generate_license_key(length, username, plan):
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    key = f"{key}_{username}"
    if plan == 0.0071:
        key = f"GIVEAWAY-{key}"
    if plan == 28:
        key = f"SA-{key}"
    elif plan == 7:
        key = f"AA-{key}"
    elif plan == 3:
        key = f"BC-{key}"
    elif plan == 1:
        key = f"CD-{key}"
    return key


@Client.on_message(filters.command("generate_key") & filters.private)
@is_admin
async def generate_key(bot, m: Message):
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Giveaway (10min)", callback_data=f"GenerateKey_10min"),
            ],
            [
                InlineKeyboardButton("1 day", callback_data=f"GenerateKey_1day"),
                InlineKeyboardButton("3 days", callback_data=f"GenerateKey_3days")
            ],
            [
                InlineKeyboardButton("7 days", callback_data=f"GenerateKey_7days"),
                InlineKeyboardButton("28 days", callback_data=f"GenerateKey_28days")
            ]
        ]
    )

    await m.reply_text("Choose a plan to generate key", reply_markup=btn)



@Client.on_message(filters.regex("Generate key") & filters.private)
@is_admin
async def generate_kkey(bot, m: Message):
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Giveaway (10min)", callback_data=f"GenerateKey_10min"),
            ],
            [
                InlineKeyboardButton("1 day", callback_data=f"GenerateKey_1day"),
                InlineKeyboardButton("3 days", callback_data=f"GenerateKey_3days")
            ],
            [
                InlineKeyboardButton("7 days", callback_data=f"GenerateKey_7days"),
                InlineKeyboardButton("28 days", callback_data=f"GenerateKey_28days")
            ]
        ]
    )

    await m.reply_text("Choose a plan to generate key", reply_markup=btn)


@Client.on_callback_query(filters.regex(r"GenerateKey_"))
async def generate_key_q(bot, q: Message):
    plan = q.data.split("_")[1]
    if plan == "10min":
        expiry_date = 0.0071
        key = generate_license_key(20, BOT_USERNAME, expiry_date)
        LicenseKeys().add_key(key, expiry_date, plan)
        await q.message.edit_text(f"**Key generated successfully** ⚡\n\n1: Plan: {plan} 💠\n2: Key: `{key}` 🍀\n\n3: Expiry date: {expiry_date} days 🚨")
    if plan == "1day":
        expiry_date = 1
        key = generate_license_key(20, BOT_USERNAME, expiry_date)
        LicenseKeys().add_key(key, expiry_date, plan)
        await q.message.edit_text(f"**Key generated successfully** ⚡\n\n1: Plan: {plan} 💠\n2: Key: `{key}` 🍀\n\n3: Expiry date: {expiry_date} days 🚨")
    elif plan == "3days":
        expiry_date = 3
        key = generate_license_key(20, BOT_USERNAME, expiry_date)
        LicenseKeys().add_key(key, expiry_date, plan)
        await q.message.edit_text(f"**Key generated successfully** ⚡\n\n1: Plan: {plan} 💠\n2: Key: `{key}` 🍀\n\n3: Expiry date: {expiry_date} days 🚨")
    elif plan == "7days":
        expiry_date = 7
        key = generate_license_key(20, BOT_USERNAME, expiry_date)
        LicenseKeys().add_key(key, expiry_date, plan)
        await q.message.edit_text(f"**Key generated successfully** ⚡\n\n1: Plan: {plan} 💠\n2: Key: `{key}` 🍀\n\n3: Expiry date: {expiry_date} days🚨")
    elif plan == "28days":
        expiry_date = 28
        key = generate_license_key(20, BOT_USERNAME, expiry_date)
        LicenseKeys().add_key(key, expiry_date, plan)
        await q.message.edit_text(f"**Key generated successfully** ⚡\n\n1: Plan: {plan} 💠\n2: Key: `{key}` 🍀\n\n3: Expiry date: {expiry_date} days🚨")

