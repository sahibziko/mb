from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="𝄞 ʙᴀğʟᴀʏıʀ 𝄞", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="✙ Qʀᴜᴘᴀ ƏʟᴀᴠƏ ᴇᴛ ✙",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="⚙️ ᴋÖᴍƏᴋʟƏʀ ᴠƏ ƏᴍʀʟƏʀ ⚙️", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="🗣 ᴋᴀɴᴀʟ", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="🔧 ᴅƏꜱᴛƏᴋ", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="💡 ᴍƏɴʙƏ", url="https://t.me/NazSupport"
        ),
        InlineKeyboardButton(text=" İɴᴋɪŞᴀꜰ ᴇᴛᴅɪʀɪᴄɪ ", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="✙ Qʀᴜᴘᴀ ƏʟᴀᴠƏ ᴇᴛ ✙",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="🗣 ᴋᴀɴᴀʟ", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="🔧 ᴅƏꜱᴛƏᴋ", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="💡 ᴍƏɴʙƏ", url="https://t.me/NazSupport"
        ),
        InlineKeyboardButton(text="☠ İɴᴋɪŞᴀꜰ ᴇᴛᴅɪʀɪᴄɪ", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="👥 ʜƏʀ ᴋƏꜱ",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="📑 ꜱᴜᴅᴏ", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="👨‍💻 ꜱᴀʜɪʙɪ", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="◅ ɢᴇʀɪ", callback_data="fallen_home"),
        InlineKeyboardButton(text="✘ ʙᴀğʟᴀʏıʀ", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="🔧 ᴅƏꜱᴛƏᴋ", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="◅ Geri", callback_data="fallen_help"),
        InlineKeyboardButton(text="✘ Bağlayır", callback_data="close"),
    ],
]
