from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from BABYMUSIC import app
from config import BOT_USERNAME
from BABYMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ╼⃝𖠁 𝗦꯭𝘂‌꯭𝐤⃪ꭷ‌⃪꯭꯭꯭꯭꯭ꭷ‌⃪꯭꯭꯭꯭፝֟ؖ۬𝛈꯭ 𝗠⃪꯭ᴜ⃪꯭֟፝ؖ۬s⃪꯭ɪ꯭ᴄ𝄟 𖠁⃝╾ ʙᴏᴛ ✪
 
 ➲ ʙsᴅᴋ ʀᴇᴘᴏ ʟᴇɢᴀ ◉‿◉ ✰
 
 ➲ ᴘᴇʜʟᴇ ᴢᴀʏɴ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ ✰
 
 ➲ ᴄʜᴜᴘ ᴄʜᴜᴘ ʙᴏᴛ ʟᴇᴋᴇ ɴɪᴋᴀʟ ✰
 
 ➲ ʀᴇᴘᴏs ᴛᴏ ɴᴀʜɪ ᴍɪʟᴇɢᴀ ʙᴇᴛᴀ ⊂◉‿◉ ✰
 
 ➲ ᴀɢʀ ᴄʜᴀʜɪʏᴇ ᴛᴏ ᴢᴀʏɴ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟɴᴀ ᴘᴀᴅᴇɢᴀ ✰
 
 ►  ฅ( ̳• ◡ • ̳)ฅ
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("•ᴀᴅᴅ ᴍᴇ•", url=f"https://t.me/Sukoonn_X_music_bot?startgroup=true")
        ],
        [
          InlineKeyboardButton("•sᴜᴘᴘᴏʀᴛ•", url="https://t.me/+C8NQDFeJJwNiNmVl"),
          InlineKeyboardButton("•ᴏᴡɴᴇʀ•", url="https://t.me/ll_Oye_Zayn_ll"),
          ],
               [
                InlineKeyboardButton("•ᴜᴘᴅᴀᴛᴇs•", url="https://t.me/ll_Bot_Promotion_ll"),

],
[
              InlineKeyboardButton("•ʙᴀɴᴀʟʟ•", url=f"https://t.me/SATYABANALL_ROBOT"),
              InlineKeyboardButton("︎•ʏᴛ-ᴍᴜsɪᴄ•", url=f"https://t.me/YOUTUBE_RROBOT"),
              ],
              [
              InlineKeyboardButton("•ᴅᴇᴇᴘ ᴍᴜsɪᴄ•", url=f"https://t.me/DEEP_MUSIC_ROBOT"),
InlineKeyboardButton("•ᴄʜᴀᴛ ʙᴏᴛ•", url=f"https://t.me/RADHIKA_CHAT_RROBOT"),
],
[
InlineKeyboardButton("•sᴛʀɪɴɢ-ɢᴇɴ•", url=f"https://t.me/STRING_BABYGEN_BOT"),
InlineKeyboardButton("•ᴍᴀɴᴀɢᴍᴇɴᴛ•", url=f"https://t.me/SATYA_HELP97_BOT"),
],
[
              InlineKeyboardButton("•sᴘᴀᴍ-ʙᴏᴛ•", url=f"https://t.me/SATYASPAMROBOT"),
              InlineKeyboardButton("•ᴀᴘɴᴀ-ᴍᴜsɪᴄ•︎", url=f"https://t.me/MUSIC_OO_ROBOT"),
              ],
              [
              InlineKeyboardButton("•sᴛʀɪɴɢ ʜᴀᴄᴋ•", url=f"https://t.me/BABYSTRINGROBOT"),
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/a24eaa37b36f38695aba2.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/BABY-MUSIC/BABYTUNE/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[•ʙᴏᴛ-ᴏᴡɴᴇʀ•](https://t.me/ll_Oye_Zayn_ll) | [•ᴜᴘᴅᴀᴛᴇs•](https://t.me/ll_Bot_Promotion_ll)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


