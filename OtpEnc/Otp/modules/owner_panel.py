import random
import string

from pyrogram import Client, filters
from pyrogram.types import Message, KeyboardButton, ReplyKeyboardMarkup



from .. import BOT_USERNAME
from ..utils.devsonly import is_admin
from .database.main_db import (
    Subscription, 
    BlackList, 
    LoadLicenseKeys, 
    SecCounter, 
    BalanceCut
)



def generate_license_key(length, username):
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    key = f"{key}_{username}"
    return key


@Client.on_message(filters.command("admin_panel") & filters.private)
@is_admin
async def admin_panel(bot, m: Message):
    btn = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton("🍀 All users list 🍀"),
            ],
            [
                KeyboardButton("🗑 remove user 🗑"),
                KeyboardButton("‼️ Warn User ‼️")
            ],
            [
                KeyboardButton("🚨 Ban user 🚨"),
                KeyboardButton("🌱 Unban user 🌱"),
            ],
            [
                KeyboardButton("💠 Generate key 💠"),
            ],
            [
                KeyboardButton("💰 Load balance 💰"),
            ]
        ], resize_keyboard=True
    )
    await m.reply_text("Choose an option", reply_markup=btn)
    await m.delete()


@Client.on_message(filters.regex("All users list") & filters.private)
@is_admin
async def all_users(bot, m: Message):
    users = Subscription().all_users()
    if users == []:
        return await m.reply_text("No users found, moi moi!")
    us = "⚡ **Users list:** ⚡\n\n"
    count = 1
    for user in users:
        us += f"{count}: {user[0]}\n"
        count += 1

    await m.reply_text(f"**Total users: {len(users)}**\n\n{us}")


@Client.on_message(filters.regex("remove user") & filters.private)
@is_admin
async def remove_user(bot, m: Message):
    user_id = await m.chat.ask("Enter the user id to remove")
    user_id = int(user_id.text)
    if user_id == "":
        return await m.reply_text("Please enter a user id to remove")
    Subscription().remove_user(user_id)
    await m.reply_text("User removed successfully")


@Client.on_message(filters.regex("Warn User") & filters.private)
@is_admin
async def warn_user(bot, m: Message):
    user_id = await m.chat.ask("Enter the user id to warn 🚨")
    user_id = user_id.text
    reason = await m.chat.ask("Enter the reason for warning ❓")
    reason = reason.text
    if user_id == "":
        return await m.reply_text("Please enter a user id to warn 🥲")
    if reason == "":
        return await m.reply_text("Please enter a reason to warn the user 🥲")
    try:
        await bot.send_message(user_id, f"**🚨 You have been warned 🚨**\n\n reason:\n> {reason}\n\n__🔰 If you continue to do this, you will be banned from using the bot! 🔰__")
    except:
        return await m.reply_text("Couldn't send warn message to user 😔")
    else:
        await m.reply_text("💠 User warned successfully 💠")


@Client.on_message(filters.regex("Ban user") & filters.private)
@is_admin
async def ban_user(bot, m: Message):
    user_id = await m.chat.ask("Enter the user id to ban 🚫")
    user_id = int(user_id.text)
    reason = await m.chat.ask("Enter the reason for banning ❓")
    reason = reason.text
    if user_id == "":
        return await m.reply_text("Please enter a user id to ban 🥲")
    if reason == "":
        return await m.reply_text("Please enter a reason to ban the user 🥲")
    try:
        await bot.send_message(user_id, f"**🚫 You have been banned 🚫**\n\n reason:\n> {reason}\n\n__🔰 Now keep your mouth shut you piece of shit! 🔰__")
    except:
        return await m.reply_text("Couldn't send ban message to user 😔")
    else:
        BlackList().add_user(user_id)
        await m.reply_text("💠 User banned successfully 💠")


@Client.on_message(filters.regex("Unban user") & filters.private)
@is_admin
async def unban_user(bot, m: Message):
    user_id = await m.chat.ask("Enter the user id to unban 🚫")
    user_id = int(user_id.text)
    if user_id == "":
        return await m.reply_text("Please enter a user id to unban 🥲")
    try:
        await bot.send_message(user_id, f"**🍀 You have been unbanned, now you can use bot 🍀**")
    except:
        pass
    BlackList().remove_user(user_id)
    await m.reply_text("💠 User unbanned successfully 💠")


@Client.on_message(filters.regex("Load balance") & filters.private)
@is_admin
async def load_balance(bot, m: Message):
    # user_id = await m.chat.ask("Please send me user id")
    # user_id = int(user_id.text)
    # try:
    #     username = await bot.get_users(user_id)
    #     username = username.username
    # except:
    #     return await m.reply("Invalid user id")
    user_id = m.from_user.id
    load_amount = await m.chat.ask("Load amound? 💰")
    amount = float(load_amount.text)
    # if user_id == "":
    #     return await m.reply_text("Please enter a user id to load balance 🥲")
    if amount == "":
        return await m.reply_text("Please enter a amount to load balance 🥲")
    try:
        current_plan = Subscription().get_plan(user_id)[0]
    except:
        current_plan = None
    # if current_plan != "pay_as_you_go" and current_plan != None:
    #     return await m.reply_text("User already have a plan, can't load balance.")
    key = generate_license_key(20, BOT_USERNAME)
    LoadLicenseKeys().add_key(key, amount)
    await m.reply_text(f"💠 Key Generated 💠\n\n1: Key: `{key}` 🍀\n2: Plan: pay_as_you_go 🌱\n3: Load amount: {amount} 💰")


@Client.on_message(filters.command("stats"))
@is_admin
async def stat(bot: Client, m: Message):
    total_calls = SecCounter().get_total_calls()
    callsec = SecCounter().get_total_seconds_country()
    Text = f"🔰 Stat reports 🔰\n\n🍀 **Total Calls:** {total_calls}\n**📚 Countries with seconds 📚:**\n\n"
    for i in callsec.keys():
        Text += f"    ✨ **{i.title()}**: {callsec[i]}s\n"
    balancecut = BalanceCut().get_balancecut()[0]
    Text+= f"\n☠️ **Expected Balance cut from APi:** ${balancecut} ☠️\n\n"
    await m.reply_text(Text)

@Client.on_message(filters.command("resetall"))
@is_admin
async def reset_all(bot: Client, m: Message):
    SecCounter().delete_all()
    BalanceCut().clear_balancecut()
    await m.reply_text("🔰 All stats reseted 🔰")