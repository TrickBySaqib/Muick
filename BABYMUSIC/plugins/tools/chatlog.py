import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from BABYMUSIC import app 
from pyrogram.errors import RPCError, ChatAdminRequired, ChatWriteForbidden
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, aiohttp
from pathlib import Path
from pyrogram.enums import ParseMode

# Log group ID
LOG_GROUP_ID = -1002022622141  # Directly set your log group ID here

# Random photos for messages
photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message: Message):    
    chat = message.chat
    try:
        # Export chat invite link (requires admin privileges)
        link = await app.export_chat_invite_link(chat.id)
    except ChatAdminRequired:
        # If bot is not admin, use a fallback link
        link = "No link available (admin required)"
    
    for member in message.new_chat_members:
        if member.id == app.id:
            try:
                count = await app.get_chat_members_count(chat.id)
                msg = (
                    f"❍ ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ ●\n\n"
                    f"____________________________________\n\n"
                    f"❍ ᴄʜᴀᴛ ɴᴀᴍᴇ: {chat.title} ●\n"
                    f"❍ ᴄʜᴀᴛ ɪᴅ: {chat.id} ●\n"
                    f"❍ ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{chat.username} ●\n"
                    f"❍ ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link}) ●\n"
                    f"❍ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count} ●\n"
                    f"❍ ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention} ●"
                )
                # Send photo with caption to log group
                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=random.choice(photo),
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(f"● sᴇᴇ ɢʀᴏᴜᴘ ●", url=f"{link}")]
                    ])
                )
            except ChatWriteForbidden:
                # If bot can't send messages in the log group
                print(f"Bot can't send messages in the log group (ID: {LOG_GROUP_ID})")
            except RPCError as e:
                # Handle other RPC errors
                print(f"RPCError: {e}")

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
        try:
            # Send photo with caption to log group
            await app.send_photo(
                LOG_GROUP_ID,
                photo=random.choice(photo),
                caption=left
            )
        except ChatWriteForbidden:
            # If bot can't send messages in the log group
            print(f"Bot can't send messages in the log group (ID: {LOG_GROUP_ID})")
        except RPCError as e:
            # Handle other RPC errors
            print(f"RPCError: {e}")
