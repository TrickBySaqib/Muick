from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from BABYMUSIC import app

#--------------------------
# MUST_JOIN को सही चैट यूजरनेम या आईडी से सेट करें
MUST_JOIN = "example_chat"  # यूजरनेम के लिए (@ के बिना) या चैट आईडी (जैसे -1001234567890)
#------------------------

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:  # यदि MUST_JOIN सेट नहीं है, तो कुछ न करें
        return

    try:
        # यूजर चैट में है या नहीं, यह जांचें
        await app.get_chat_member(MUST_JOIN, msg.from_user.id)
    except UserNotParticipant:
        # यदि यूजर चैट में नहीं है, तो लिंक तैयार करें
        if MUST_JOIN.startswith("@"):  # यदि MUST_JOIN यूजरनेम है
            link = "https://t.me/" + MUST_JOIN[1:]  # @ को हटाकर लिंक बनाएं
        else:  # यदि MUST_JOIN चैट आईडी है
            try:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            except ChatAdminRequired:
                print(f"मुझे {MUST_JOIN} में एडमिन एक्सेस की आवश्यकता है।")
                return

        # यूजर को जॉइन करने के लिए संदेश भेजें
        try:
            await msg.reply_photo(
                photo="https://telegra.ph/file/d24262661dda3f1832290.jpg",
                caption=f"๏ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ [๏sᴜᴘᴘᴏʀᴛ๏]({link}) ʏᴇᴛ, ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛʜᴇɴ ᴊᴏɪɴ [๏sᴜᴘᴘᴏʀᴛ๏]({link}) ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ !",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("๏Jᴏɪɴ๏", url=link),
                        ]
                    ]
                )
            )
            await msg.stop_propagation()
        except ChatWriteForbidden:
            pass  # यदि यूजर ने बॉट को ब्लॉक किया है, तो कुछ न करें
    except ChatAdminRequired:
        print(f"मुझे {MUST_JOIN} में एडमिन एक्सेस की आवश्यकता है।")
    except Exception as e:
        print(f"An error occurred: {e}")
