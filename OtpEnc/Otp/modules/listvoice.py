from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


from ..scripts.voices import voices
from ..utils.formatters import get_flag
from ..utils.decorators import blacklist
from ..utils.detect_flood import is_blocked





@Client.on_message(filters.command(["listvoices", "voices"]))
@blacklist
@is_blocked
async def voicesa(bot, m):
    btn = [[]]
    count = 0
    cr = 0
    for i in voices.keys():
        if count%3==0:
            btn.append([])
            cr+=1
            btn[cr].append(InlineKeyboardButton(f"{i} {get_flag(i)}", callback_data=f"voice_{i}"))
        else:
            btn[cr].append(InlineKeyboardButton(f"{i} {get_flag(i)}", callback_data=f"voice_{i}"))
        count += 1
    btn.append([InlineKeyboardButton("Back", callback_data="start_back")])
    await m.reply("Available voices:", reply_markup=InlineKeyboardMarkup(btn))



@Client.on_callback_query(filters.regex(r"^voice_"))
async def help_callback(bot, q):
    back = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Back", callback_data = "voiceback")
            ]
        ]
    )
    data = q.data.split("_")[1]
    txt = f"🍀 List of {data} voices 🍀\n\n"
    vcs = ""
    c = 1
    for i in voices[data]:
        vcs += f"> {c}: `{i}`\n"
        c+=1
    await q.message.edit_text(f"{txt}{vcs}", reply_markup=back)


@Client.on_callback_query(filters.regex(r"^voiceback"))
async def help_callbacl_back(bot, q: CallbackQuery):
    btn = [[]]
    count = 0
    cr = 0
    for i in voices.keys():
        if count%3==0:
            btn.append([])
            cr+=1
            btn[cr].append(InlineKeyboardButton(f"{i} {get_flag(i)}", callback_data=f"voice_{i}"))
        else:
            btn[cr].append(InlineKeyboardButton(f"{i} {get_flag(i)}", callback_data=f"voice_{i}"))
        count += 1
    btn.append([InlineKeyboardButton("Back", callback_data="start_back")])
    await q.edit_message_caption("Available voices:", reply_markup=InlineKeyboardMarkup(btn))