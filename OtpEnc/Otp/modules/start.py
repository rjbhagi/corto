from pyrogram import Client, filters
from pyrogram.types import (
    Message, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    CallbackQuery, 
    InputMediaPhoto,
    InputMediaVideo
)
from .. import (
    helper, 
    START_LOGS, 
    BOT_USERNAME, 
    BOT_NAME, 
    UPDATES_ANIMATION, 
    UPDATES_CHANNEL,
    SUPPORT_GROUP,
    GRABS,
    VOUCHES,
    PRIVACY_POLICY,
    TERMS_AND_CONDITIONS,
    FAQ,
    START_ANIM
)
from ..scripts.voices import voices
from .database.main_db import Users
from ..utils.decorators import blacklist
from ..utils.detect_flood import is_blocked



START_MSG = f"""
🌐 Welcome to {BOT_NAME} - The Premier OTP Solution 🌐

**#1 Otp Bot you can rely on for Spoofing and Calling Solutions Including Otp Captures in real time**

🚀 Active | Uptime: 99.99%

**🔑 Key Features:** 
- Dualphishing protection & Spoof Panel
- Validation Systems & customizable call settings
- Tailorable user experience & operational workflows
- High-quality AI voices in multiple languages
- Create & customize scripts for specific needs
- Advanced encryption & security protocols

**💵 Flexible Pricing:**
- Daily, three-day, weekly, and monthly plans
- Pay as you go starting from $0.14 (Type /payasyougo for details)

🛡️ Trust in {BOT_NAME}'s technology and support to enhance your Spoofing Experience

🔗 Get Started: Choose a plan or enter with an existing license key. 

{BOT_NAME} – Your Partner in Secure Authentication. ⚡
"""

@Client.on_message(filters.command("start"))
@blacklist
@is_blocked
async def start(bot, m: Message):
    user_id = m.from_user.id
    if Users().user_exists(user_id)==None:
        first_name = m.from_user.first_name
        try:
            username = m.from_user.username
        except:
            username = "None"
        Users().add_user(user_id, first_name, username)
        await helper.send_message(START_LOGS, f"🍀 --**New user**-- 🍀\n\n> 1: First name: **{first_name}**\n> 2: user id: **{user_id}**\n> 3: username: **@{username}**")
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🌟 Features 🌟", callback_data="features"),
                InlineKeyboardButton("🤖 Commands 🤖", callback_data="commands")
            ],
            [
                InlineKeyboardButton("🔉 Voices 🔉", callback_data="voiceback"),
                InlineKeyboardButton("☎️ Support ☎️", callback_data="support")
            ],
            [
                InlineKeyboardButton("🔐 Prices 🔐", callback_data="back_btn"),
                InlineKeyboardButton("👥 Community 👥", callback_data="community")
            ],
            [
                InlineKeyboardButton("🛡️ Privacy policy 🛡️", url=PRIVACY_POLICY),
                InlineKeyboardButton("🔒 Terms & Conditions 🔒", url=TERMS_AND_CONDITIONS)
            ],
            [
                InlineKeyboardButton("📚 FAQ(s)", url=FAQ)
            ]
        ]
    )
    await m.reply_video(video=START_ANIM, caption=START_MSG, reply_markup=btn)


@Client.on_callback_query(filters.regex("start_back"))
async def start_back(bot, q: CallbackQuery):
    user_id = q.from_user.id
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🌟 Features 🌟", callback_data="features"),
                InlineKeyboardButton("🤖 Commands 🤖", callback_data="commands")
            ],
            [
                InlineKeyboardButton("🔉 Voices 🔉", callback_data="voiceback"),
                InlineKeyboardButton("☎️ Support ☎️", callback_data="support")
            ],
            [
                InlineKeyboardButton("🔐 Prices 🔐", callback_data="back_btn"),
                InlineKeyboardButton("👥 Community 👥", callback_data="community")
            ],
            [
                InlineKeyboardButton("🛡️ Privacy policy 🛡️", url=PRIVACY_POLICY),
                InlineKeyboardButton("🔒 Terms & Conditions 🔒", url=TERMS_AND_CONDITIONS)
            ],
            [
                InlineKeyboardButton("📚 FAQ(s)", url=FAQ)
            ]
        ]
    )
    await q.edit_message_media(InputMediaVideo(media=START_ANIM, caption=START_MSG), reply_markup=btn)





feature = f"""
📲 {BOT_NAME} 🎯

🌟 Discover {BOT_NAME} for advanced social engineering:
- 🕹 Modes: Banks, Emails, Crypto, and more.
- 🤖 Smart Spoofing: Adopt any caller ID.
- 👁 Privacy: Prioritizes your anonymity.
- ✈️ Global Access: Services worldwide.
- 🤝 Earn: Advanced Affiliate System.
- 📝 Custom Scripts: Tailor your messages.
- 📊 Actions: Customize your panel.
- 📱 Captures: Accept or reject options.
- ⚙️ Workflows: Realistic multiple actions.
- 📡 Monitoring: Live panel view.
- ⚡️ Payments: Automated subscriptions.

🎯 Ready to upgrade? Use /Purchase for your subscription!"""

@Client.on_callback_query(filters.regex("features"))
async def features(bot, q: CallbackQuery):
    backbtn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Back", callback_data="start_back")
            ]
        ]
    )
    await q.edit_message_media(InputMediaPhoto("https://telegra.ph/file/176b207861bd2248b9373.jpg", feature), reply_markup=backbtn)

@Client.on_callback_query(filters.regex("voicelist"))
async def voicesa(bot, q: CallbackQuery):
    btn = [[]]
    count = 0
    cr = 0
    for i in voices.keys():
        if count%3==0:
            btn.append([])
            cr+=1
            btn[cr].append(InlineKeyboardButton(i, callback_data=f"voice_{i}"))
        else:
            btn[cr].append(InlineKeyboardButton(i, callback_data=f"voice_{i}"))
        count += 1
    btn.append([InlineKeyboardButton("Back", callback_data="start_back")])
    await q.message.edit_text("Available voices:", reply_markup=InlineKeyboardMarkup(btn))


@Client.on_callback_query(filters.regex(r"support"))
async def support(bot, q: CallbackQuery):
    backbtn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Back", callback_data="start_back")
            ]
        ]
    )
    xc = f"""📲 {BOT_NAME} OTP BOT

🆘 For any assistance or inquiries regarding {BOT_NAME} OTP Bot, our dedicated support team is available around the clock. Don't hesitate to reach out if you need help navigating features, encountering technical issues, or simply have questions about how to maximize the effectiveness of your tool.

✉️ Contact our Support Team:
- You can directly message our support specialists on Telegram:
    - [Click here to message us](https://t.me/{SUPPORT_GROUP})

For a more comprehensive support experience and to engage with a community of users, you are welcome to join our Telegram server. Here, you'll find additional resources, shared experiences, and the opportunity to discuss various topics related to {BOT_NAME} OTP Bot.

🌐 Join our Telegram Community:
- [Click here to join our server](https://t.me/{UPDATES_CHANNEL})

We strive to provide prompt and effective assistance to ensure you have the best experience with our bot. Whether you're a new user or have been with us for a while, we're here to support you every step of the way."""
    await q.message.edit_text(xc, reply_markup=backbtn)


@Client.on_callback_query(filters.regex(r"community"))
async def community(bot, q: CallbackQuery):

    btns = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🏦 Official Channel 🏦", url=f"https://t.me/{UPDATES_CHANNEL}")
            ],
            [
                InlineKeyboardButton("💬 Community 💬", url=f"https://t.me/{SUPPORT_GROUP}"),
                InlineKeyboardButton("🎯 OTP Grabs 🎯", url=F"https://t.me/{GRABS}")
            ],
            [
                InlineKeyboardButton("🤖 Vouches 🤖", url=f"https://t.me/{VOUCHES}")
            ],
            [
                InlineKeyboardButton("👇🏼 Back 👇🏼", callback_data="start_back")
            ]
        ]
    )

    await q.message.edit_text("⚡ Join our community: ⚡", reply_markup=btns)



COMMANDS = f"""
{BOT_NAME} OTP Bot

-> Commands List:

--**Basic Commands:**--

/plan 📄: Check your subscription or plan details  
/redeem 🔑: Redeem a License Key  
/purchase 💳: Purchase a Subscription  

--**Calling Commands [Presets]:**--

**Note: These Call Commands are already set and only formatting can be used.**

/call 📲: To Capture Any OTP  
/paypal 💸: To Capture PayPal OTP  
/venmo 💳: To Capture Venmo OTP  
/cashapp 💰: To Capture CashApp OTP  
/coinbase 🪙: To Capture Coinbase OTP  
/amazon 🛒: To Capture Amazon OTP  
/applepay 🍏: To Capture Apple Pay OTP  
/email 📧: To Capture Email OTP  
/microsoft 🖥: To Capture Microsoft OTP  


--**Pay-As-You-Go Commands:**--

/payasyougo 🔄: To Check Pay-As-You-Go Details  
/profile 📊: To Check Pay-As-You-Go Profile  
/load 💳: To Load Pay-As-You-Go Balance

Script Commands: /scripthelp"""
@Client.on_callback_query(filters.regex(r"commands"))
async def commands(bot, q: CallbackQuery):
    backbtn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Back", callback_data="start_back")
            ]
        ]
    )
    await q.message.edit_media(InputMediaPhoto(caption=COMMANDS, media="https://telegra.ph/file/6530fa7676599d8ff1e6a.jpg"), reply_markup=backbtn)



@Client.on_message(filters.command("scripthelp"))
@blacklist
@is_blocked
async def scripthelp(bot, m: Message):
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📚 Back 📚", callback_data="start_back")
            
            ]
        ]
    )
    text = """**--Available commands--**:\n\n
> /create 🛠: To Create Custom Script  
> /customcall 📞: To Create Custom Call  
> /view_script 📜: To Overview Your Scripts 
> /edit_script 📜 : To edit Your Script 
> /list_script 🗞️: To Show All Your Scripts 
> /delete_script ❌: To Delete Your Script"""
    await m.reply(text, reply_markup=btn)