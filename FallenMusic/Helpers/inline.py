from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="𝄞 ʙᴀğʟᴀʏıʀ 𝄞", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▶️", callback_data="resume_cb"),
            InlineKeyboardButton(text="⏸", callback_data="pause_cb"),
            InlineKeyboardButton(text="⏭", callback_data="skip_cb"),
            InlineKeyboardButton(text="⏹", callback_data="end_cb"),
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
    [InlineKeyboardButton(text="ℹ️ Botun Əmrləri", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="📢 Kanal", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="💻 Dəstək", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="💡 Mənbə", url="https://t.me/AzeBots"
        ),
        InlineKeyboardButton(text="👑 Sahib  ", user_id=config.OWNER_ID),
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
        InlineKeyboardButton(text="📢 Kanal", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="💻 Dəstək", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="💡 Mənbə", url="https://t.me/AzeBots"
        ),
        InlineKeyboardButton(text="👑 Sahib", user_id=config.OWNER_ID),
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
        InlineKeyboardButton(text="📑 Sudo", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="👑 Sahib", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="🔸 geri", callback_data="fallen_home"),
        InlineKeyboardButton(text="🔻 çıx", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="💻 dəstək", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="🔸 geri", callback_data="fallen_help"),
        InlineKeyboardButton(text="🔻 çıx", callback_data="close"),
    ],
]
