# By @TroJanzHEX
import os
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.photo & filters.private)
async def photo(client, message):
       await client.send_message(
            chat_id=message.chat.id,
            text="select a method",
            reply_markup = InlineKeyboardMarkup(
 [
    [
        InlineKeyboardButton(text = "BRIGHT",callback_data="bright"),
        InlineKeyboardButton(text = "MIXED", callback_data = "mix"),
        InlineKeyboardButton(text = "B&W",callback_data = "b|w"),
    ],
    [
        InlineKeyboardButton(text = "CIRCLE", callback_data = "circle"),
        InlineKeyboardButton(text = "BLUR", callback_data="blur"),
        InlineKeyboardButton(text = "Border", callback_data="border"),
    ],
    [
        InlineKeyboardButton(text = "STICKER", callback_data = "stick"),
        InlineKeyboardButton(text = "ROTATE",callback_data = "rotate"),
        InlineKeyboardButton(text = "CONTRAST",callback_data = "contrast"),
    ],
    [
        InlineKeyboardButton(text = "SEPIA",callback_data = "sepia"),
        InlineKeyboardButton(text = "PENCIL", callback_data = "pencil"),
        InlineKeyboardButton(text = "CARTOON" , callback_data = "cartoon"),
    ],
    [
        InlineKeyboardButton(text = "CLOSE", callback_data = "close_e"),
     
    ]
  ]
),
            reply_to_message_id=message.message_id
        )

