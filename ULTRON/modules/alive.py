import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from ULTRON.events import register
from ULTRON import telethn as tbot


RISHABH = "https://telegra.ph/file/d7eff56f48fcaf2cea0f7.jpg"

@register(pattern=("/ULTRON"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm ULTRON bot.** \n\n"
  TEXT += "💞 **ULTRON IS ALIVE** \n\n"
  TEXT += f"💞 **Owner : [RISHABH](https://t.me/ULTRON_OWNER)** \n\n"
  TEXT += f"💞 **Library Version :** `{telever}` \n\n"
  TEXT += f"💞 **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"💞 **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For using ULTRON 💞**"
  BUTTON = [[Button.url("Help", "https://t.me/ULTRON_MANAGER_bot?start=help"), Button.url("Support", "https://t.me/ULTRON_BOTS")]]
  await tbot.send_file(event.chat_id, RISHABH, caption=TEXT,  buttons=BUTTON)
