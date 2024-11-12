from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from .. import SELLIX1D, SELLIX3D, SELLIX7D, SELLIX28D
from ..Subscription.prices import keyprices
from ..utils.decorators import blacklist
from ..utils.detect_flood import is_blocked




@Client.on_message(filters.command(["buy", "purchase"]))
@blacklist
@is_blocked
async def buy_plan(bot: Client, m: Message):
    user_id = m.from_user.id
    # btn = InlineKeyboardMarkup(
    #     [
    #         [
    #             InlineKeyboardButton("1 day", callback_data=f"BuyKey_1day_{user_id}"),
    #             InlineKeyboardButton("3 days", callback_data=f"BuyKey_3days_{user_id}")
    #         ],
    #         [
    #             InlineKeyboardButton("7 days", callback_data=f"BuyKey_7days_{user_id}"),
    #             InlineKeyboardButton("28 days", callback_data=f"BuyKey_28days_{user_id}")
    #         ],
    #         [InlineKeyboardButton("👻 Back 👻", callback_data="start_back")]
    #     ]
    # )
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(f"1 day (${keyprices['1day']})", url=SELLIX1D),
                InlineKeyboardButton(f"3 days (${keyprices['3days']})", url=SELLIX3D)
            ],
            [
                InlineKeyboardButton(f"7 days (${keyprices['7days']}) ", url=SELLIX7D),
                InlineKeyboardButton(f"28 days (${keyprices['28days']})", url=SELLIX28D)
            ],
            [
                InlineKeyboardButton("Back", callback_data="start_back")
            ]
        ]
    )

    await m.reply_text("**Ready to upgrade?**\n 🚀 Click below to select and purchase your plan via Sellix. 🛒💳", reply_markup=btn)



@Client.on_callback_query(filters.regex(r"back_btn"))
async def buy_plan_back(bot: Client, q: Message):
    user_id = q.from_user.id
    if int(user_id) != q.from_user.id:
        return await q.answer("**Ready to upgrade?**\n 🚀 Click below to select and purchase your plan via Sellix. 🛒💳", show_alert=1)
    # btn = InlineKeyboardMarkup(
    #     [
    #         [
    #             InlineKeyboardButton("1 day", callback_data=f"BuyKey_1day_{user_id}"),
    #             InlineKeyboardButton("3 days", callback_data=f"BuyKey_3days_{user_id}")
    #         ],
    #         [
    #             InlineKeyboardButton("7 days", callback_data=f"BuyKey_7days_{user_id}"),
    #             InlineKeyboardButton("28 days", callback_data=f"BuyKey_28days_{user_id}")
    #         ],
    #         [
    #             InlineKeyboardButton("👻 Back 👻", callback_data="start_back")
    #         ]
    #     ]
    # )
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(f"1 day (${keyprices['1day']})", url=SELLIX1D),
                InlineKeyboardButton(f"3 days (${keyprices['3days']})", url=SELLIX3D)
            ],
            [
                InlineKeyboardButton(f"7 days (${keyprices['7days']})", url=SELLIX7D),
                InlineKeyboardButton(f"28 days (${keyprices['28days']})", url=SELLIX28D)
            ],
            [
                InlineKeyboardButton("Back", callback_data="start_back")
            ]
        ]
    )

    await q.message.edit_text("**Ready to upgrade?**\n 🚀 Click below to select and purchase your plan via Sellix. 🛒💳", reply_markup=btn)



@Client.on_callback_query(filters.regex(r"BuyKey_"))
async def buy_plan_q(bot: Client, q: CallbackQuery):
    plan = q.data.split("_")[1]
    user_id = q.data.split("_")[2]
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Inbox owner", url="https://t.me/MinxDev?text=I%20want%20to%20buy%20Otp%20Bot%20plan%20for%20myself")
            ],
            [
                InlineKeyboardButton("Inbox owner1", url="https://t.me/ThtQuiet?text=I%20want%20to%20buy%20Otp%20Bot%20plan%20for%20myself")
            ],
            [
                InlineKeyboardButton("Back", callback_data="back_btn")
            ]
        ]
    )
    if int(user_id) != q.from_user.id:
        return await q.answer("You are not allowed to buy plan for others", show_alert=1)
        
    if plan == "1day":
        btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Inbox owner", url="https://t.me/MinxDev?text=I%20want%20to%20buy%20Otp%20Bot%20plan%20for%20myself")
            ],
            [
                InlineKeyboardButton("Inbox owner1", url="https://t.me/ThtQuiet?text=I%20want%20to%20buy%20Otp%20Bot%20plan%20for%20myself")
            ],
            [
                InlineKeyboardButton("From Sellix (Instant)", url=SELLIX1D)
            
            ],
            [
                InlineKeyboardButton("Back", callback_data="back_btn")
            ]
        ]
    )
        await q.message.edit_text("Subscription Details❓:\n\n1 day subscription price is: 25$\n\nInbox owner to get key", reply_markup=btn)
    elif plan == "3days":
        btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Inbox owner", url="https://t.me/MinxDev?text=I%20want%20to%20buy%20Otp%20Bot%20plan%20for%20myself")
            ],
            [
                InlineKeyboardButton("Inbox owner1", url="https://t.me/ThtQuiet?text=I%20want%20to%20buy%20Otp%20Bot%20plan%20for%20myself")
            ],
            [
                InlineKeyboardButton("From Sellix (Instant)", url=SELLIX3D)
            
            ],
            [
                InlineKeyboardButton("Back", callback_data="back_btn")
            ]
        ]
    )
        await q.message.edit_text("Subscription Details❓:\n\n3 days subscription price is: 60$\n\nInbox owner to get key", reply_markup=btn)
    elif plan == "7days":
        btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Inbox owner", url="https://t.me/MinxDev?text=I%20want%20to%20buy%20Otp%20Bot%20plan%20for%20myself")
            ],
            [
                InlineKeyboardButton("Inbox owner1", url="https://t.me/ThtQuiet?text=I%20want%20to%20buy%20Otp%20Bot%20plan%20for%20myself")
            ],
            [
                InlineKeyboardButton("From Sellix (Instant)", url=SELLIX7D)
            
            ],
            [
                InlineKeyboardButton("Back", callback_data="back_btn")
            ]
        ]
    )
        await q.message.edit_text("Subscription Details❓:\n\n7 days subscription price is: 128$\n\nInbox owner to get key", reply_markup=btn)
    elif plan == "28days":
        btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Inbox owner", url="https://t.me/MinxDev?text=I%20want%20to%20buy%20Otp%20Bot%20plan%20for%20myself")
            ],
            [
                InlineKeyboardButton("Inbox owner1", url="https://t.me/ThtQuiet?text=I%20want%20to%20buy%20Otp%20Bot%20plan%20for%20myself")
            ],
            [
                InlineKeyboardButton("From Sellix (Instant)", url=SELLIX28D)
            
            ],
            [
                InlineKeyboardButton("Back", callback_data="back_btn")
            ]
        ]
    )
        await q.message.edit_text("Subscription Details❓:\n\n28 days subscription price is: 500$\n\nInbox owner to get key", reply_markup=btn)