from pyrogram import Client, filters

from .database.main_db import (
    LicenseKeys,
    Subscription,
    LoadLicenseKeys,
    PayAsYouGo,
    HandleDateTime
)
from ..utils.decorators import blacklist
from ..utils.detect_flood import is_blocked
from .. import helper, CLAIM_LOGS, LOGGER


@Client.on_message(filters.command("redeem") & filters.private)
@blacklist
@is_blocked
async def claim(bot, m):
    key = m.text[len("/redeem ") :]
    if key == "":
        return await m.reply_text("Please enter a key to claim")
    valid = LicenseKeys().get_key(key)
    existing_plan = Subscription().get_plan(m.from_user.id)
    user_id = m.from_user.id
    # if not key.endswith(f"_{m.from_user.username}"):
    #     return await m.reply_text("You are not the user meant to claim this key")
    if valid == None: 
        return await m.reply_text("Invalid key")
    elif valid[-1] == True:
        return await m.reply_text("Key already claimed")
    elif existing_plan != None:
        expired = HandleDateTime().verify_expiry_date(user_id)
        # LOGGER.info(f"Expired: {expired}")
        if expired == False:
            Subscription().delete_subscription(user_id)
            expiry_date = HandleDateTime().get_expiry_date(days=valid[1])
            plan = valid[2]
            LicenseKeys().claim_key(key)
            Subscription().add_subscription(m.from_user.id, plan, HandleDateTime().current_date_time(), expiry_date)
            validity = Subscription().get_plan(m.from_user.id)
            await helper.send_message(chat_id=CLAIM_LOGS, text=f"‼️ **--ATTENTION--** ‼️ \n\nEvent: **New subscription claimed**\n\n**🍀 --User details-- 🍀**\n\n> 1: Name: {m.from_user.first_name}\n> 2: Username: @{m.from_user.username}\n> 3: User id: ** [{m.from_user.id}](tg://user?id={m.from_user.id})**\n\n**💠 --Key details-- 💠**\n\n> 1: Key: **{key}** 🌱\n> 2: Plan: **{plan}** 💰\n\n**⏰ Date and time of activation ⏰**\n> **{HandleDateTime().current_date_time()}**\n\n**Expiry date 👻 **\n> **{expiry_date}**")
            return await m.reply_text(f"🍀 **Key claim successful** 🍀\n\n> 1: plan: {validity[0]}\n>2:  Activation time: {HandleDateTime().current_date_time()}\n> 3: Expiry date: {expiry_date}")
        else:
            # LOGGER.info(f"User already has a plan: {existing_plan}")
            return await m.reply_text("You already have a plan, can't claim key.")
    else:
        expiry_date = HandleDateTime().get_expiry_date(days=valid[1])
        plan = valid[2]
        LicenseKeys().claim_key(key)
        Subscription().add_subscription(m.from_user.id, plan, HandleDateTime().current_date_time(), expiry_date)
        validity = Subscription().get_plan(m.from_user.id)
        await helper.send_message(chat_id=CLAIM_LOGS, text=f"‼️ **--ATTENTION--** ‼️ \n\nEvent: **New subscription claimed**\n\n**🍀 --User details-- 🍀**\n\n> 1: Name: {m.from_user.first_name}\n> 2: Username: @{m.from_user.username}\n> 3: User id: ** [{m.from_user.id}](tg://user?id={m.from_user.id})**\n\n**💠 --Key details-- 💠**\n\n> 1: Key: **{key}** 🌱\n> 2: Plan: **{plan}** 💰\n\n**⏰ Date and time of activation ⏰**\n> **{HandleDateTime().current_date_time()}**\n\n**Expiry date 👻 **\n> **{expiry_date}**")
        return await m.reply_text(f"🍀 **Key claim successful** 🍀\n\n> 1: plan: {validity[0]}\n>2:  Activation time: {HandleDateTime().current_date_time()}\n> 3: Expiry date: {expiry_date}")


@Client.on_message(filters.command("load") & filters.private)
@blacklist
@is_blocked
async def load_balance(bot, m):
    user_id = m.from_user.id
    key = m.text[len("/load ") :]
    if key == "":
        key = await m.reply_text("Please enter the key to load balance: ")
    valid = LoadLicenseKeys().get_key(key)
    # if not key.endswith(f"_{m.from_user.username}"):
    #     return await m.reply_text("You are not the user meant to claim this key")
    if valid == None: 
        return await m.reply_text("Invalid key")
    elif valid[2] == True:
        return await m.reply_text("Key already claimed")
    else:
        try:
            current_plan = Subscription().get_plan(user_id)[0]
        except:
            current_plan = None
        if current_plan != "pay_as_you_go" and current_plan != None:
            validd = HandleDateTime().verify_expiry_date(user_id)
            if validd == False:
                Subscription().remove_user(user_id)
                LoadLicenseKeys().claim_key(key)
                Subscription().add_subscription(user_id, "pay_as_you_go", HandleDateTime().current_date_time(), HandleDateTime().get_expiry_date(300))
                PayAsYouGo().add_user(user_id)
                PayAsYouGo().load_balance(user_id, valid[1])
                return await m.reply_text(f"💠 Loaded balance with amount ${valid[1]} 💠")
            return await m.reply_text("You already have a plan, can't load balance.")
        LoadLicenseKeys().claim_key(key)
        Subscription().add_subscription(user_id, "pay_as_you_go", HandleDateTime().current_date_time(), HandleDateTime().get_expiry_date(300))
        PayAsYouGo().add_user(user_id)
        PayAsYouGo().load_balance(user_id, valid[1])
        try:
            await helper.send_message(CLAIM_LOGS, f"‼️ **--ATTENTION--** ‼️ \n\nEvent: **New balance loaded**\n\n**🍀 --User details-- 🍀**\n\n> 1: Name: {m.from_user.first_name}\n> 2: Username: @{m.from_user.username}\n> 3: User id: ** [{m.from_user.id}](tg://user?id={m.from_user.id})**\n\n**💠 --Key details-- 💠**\n\n> 1: Key: **{key}** 🌱\n> 2: Plan: **pay_as_you_go** 💰\n> 3: Load amnount: **{valid[1]}** ☠️\n\n**⏰ Date and time of activation ⏰**\n> **{HandleDateTime().current_date_time()}**\n\n**Expiry date 👻 **\n> **{HandleDateTime().get_expiry_date(300)}**")
        except Exception as e:
            LOGGER.error(f"Error in sending message to logs: {e}")
        return await m.reply_text(f"💠 Loaded balance with amount ${valid[1]} 💠")