from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VipX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/970ec74964dd9707fec7d.jpg",
        caption=f"""🍁ᴄʟɪᴄᴋ🥰ʙᴇʟᴏᴡ💝ʙᴜᴛᴛᴏɴ✨ᴛᴏ🙊ᴅᴍ❤️ᴏᴡɴᴇʀ🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 ᴍᴀғɪᴀ ʀᴀᴊ 🌹", url=f"https://t.me/MAFIA_RJ")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/970ec74964dd9707fec7d.jpg",
        caption=f"""🍁ᴄʟɪᴄᴋ🥰ʙᴇʟᴏᴡ💝ʙᴜᴛᴛᴏɴ✨ᴛᴏ🙊ᴅᴍ❤️ᴏᴡɴᴇʀ🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 ᴍᴀғɪᴀ ʀᴀᴊ 🌹", url=f"https://t.me/MAFIA_RJ")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/970ec74964dd9707fec7d.jpg",
        caption=f"""🍁ᴄʟɪᴄᴋ🥰ʙᴇʟᴏᴡ💝ʙᴜᴛᴛᴏɴ✨ᴛᴏ🙊ɢᴇᴛ🌱ʀᴇᴘᴏ🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://t.me/QUEEN_MUSIC_NETWORK")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/970ec74964dd9707fec7d.jpg",
        caption=f"""🍁ᴄʟɪᴄᴋ🥰ʙᴇʟᴏᴡ💝ʙᴜᴛᴛᴏɴ✨ᴛᴏ🙊ɢᴇᴛ🌱ʀᴇᴘᴏ🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://t.me/QUEEN_MUSIC_NETWORK")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/970ec74964dd9707fec7d.jpg",
        caption=f"""🍁ᴄʟɪᴄᴋ🥰ʙᴇʟᴏᴡ💝ʙᴜᴛᴛᴏɴ✨ᴛᴏ🙊ɢᴇᴛ🌱ʀᴇᴘᴏ🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://t.me/QUEEN_MUSIC_NETWORK")
                ]
            ]
        ),
    )

