import re, os, random, asyncio, html,configparser,pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram import client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info

BOT_TOKEN = "2025136294:AAFWD_xVhesnF7hCh_FHtqdFQkdqhn0qN9E"
PAYMENT_CHANNEL = "@InducedPayment" #add payment channel here including the '@' sign
OWNER_ID = 2067504073 #write owner's user id here.. get it from @MissRose_Bot by /id
CHANNELS = ["@InducedBots"] #add channels to be checked here in the format - ["Channel 1", "Channel 2"] 
              #you can add as many channels here and also add the '@' sign before channel username
Daily_bonus = 5 #Put daily bonus amount here!
Mini_Withdraw = 1  #remove 0 and add the minimum withdraw u want to set
Per_Refer = 50 #add per refer bonus here\
APP_ID = 2681714
API_HASH = "48059e206028f3d626d0fe569701cf45"
app = pyrogram.Client("sessions/app", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.private & filters.command('send'))
async def send_text(bot, m: Message):
   try:
      query = await query_msg()
      a=0
      b=0
      number = await app.ask(chat_id=m.chat.id, text="**Now me message For Broadcast\n\nMade with ❤️ By @InducedBots**")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            await app.send_message(chat_id=int(chat_id), text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            await asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      await m.reply_text(f"Successfully Broadcasted to {a} Chats\nFailed - {b} Chats !")
   except Exception as e:
      await m.reply_text(f"**Error: {e}\n\nMade with ❤️ By @InducedBots**")

# ------------------------------- View Subscribers --------------------------------- #
@app.on_message(filters.private & filters.command('ishan'))
async def subscribers_count(bot, m: Message):
    msg = await m.reply_text("Please Wait...")
    messages = await users_info(bot)
    await m.delete()
    await msg.edit(f"Total:\n\nSubscribers - {messages[0]}\nBlocked - {messages[1]}")

def a():
    app.run()