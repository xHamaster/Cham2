import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from Codexun.utils.filters import command

from Codexun.config import BOT_USERNAME

APP_ID = "18854932"
API_HASH = "9d91a01f9cc8086e004c398c96c22d89"
BOT_TOKEN = "2031768448:AAHg-9Afi80ZsTwbHzmEzXEGLJl-M3KGXJI"
UPDATES_CHANNEL = "Codexun"
OWNER= [2056407064]
PREMIUM=[2056407064]
app = pyrogram.Client("app", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def Subscribe(lel, message):
   update_channel = UPDATES_CHANNEL
   if update_channel:
      try:
         user = await app.get_chat_member(update_channel, message.chat.id)
         if user.status == "kicked":
            await app.send_message(chat_id=message.chat.id,text="Sorry Sir, You are Banned. Contact My [Support Group](https://t.me/TeamCodexun).", parse_mode="markdown", disable_web_page_preview=True)
            return 1
      except UserNotParticipant:
         await app.send_message(chat_id=message.chat.id, text="**You Need To Join My Update Channel For Using Me and Working Properly.\n\njoin and press /start for check!**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🤖 Join Update Channel 🤖", url=f"https://t.me/{update_channel}")]]), parse_mode="markdown")
         return 1
      except Exception:
         await app.send_message(chat_id=message.chat.id, text="**Something Went Wrong. Contact My [Support Group](https://t.me/TeamCodexun).**", parse_mode="markdown", disable_web_page_preview=True)
         return 1

@Client.on_message(filters.private & filters.command(["start"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   id = message.from_user.id
   user_name = '@' + message.from_user.username if message.from_user.username else None
   await add_user(id, user_name)
   but = InlineKeyboardMarkup([[InlineKeyboardButton("Commands", callback_data="cbcmnds"), InlineKeyboardButton("About", callback_data="cbabout") ],[InlineKeyboardButton("Basic Guide", callback_data="cbguide")],[InlineKeyboardButton("✚ Add Bot in Your Group ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]])
   await message.reply_photo(
        photo=f"https://telegra.ph/file/9d1ee651cb815e49fb6ad.jpg",
        caption=f"""**Welcome {message.from_user.mention()} 👋**\n\nThis is the broken music bot, a bot for playing high quality and unbreakable music in your groups voice chat.

Just add me to your group and make a admin with needed admin permission to perform a right actions !

Use the given buttons for more 📍""", reply_markup=but)



@Client.on_message(command("dot") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9d1ee651cb815e49fb6ad.jpg",
        caption=f"""**Welcome {message.from_user.mention()}** 👋

This is the broken music bot, a bot for playing high quality and unbreakable music in your groups voice chat.

Just add me to your group and make a admin with needed admin permission to perform a right actions !

Use the given buttons for more 📍""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Commands", callback_data="cbcmnds"),
                    InlineKeyboardButton(
                        "About", callback_data="cbabout")
                ],
                [
                    InlineKeyboardButton(
                        "Basic Guide", callback_data="cbguide")
                ],
                [
                    InlineKeyboardButton(
                        "✚ Add Bot in Your Group ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
           ]
        ),
    )
