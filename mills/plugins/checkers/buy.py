"""
≛ <b>Commands Available</b> ≛

──────────────────────────
- <code>/buy<code>: Check Available plans for unlocking paid checker gates.
──────────────────────────
"""
import inspect
import io
import json
import os
import time
from fuzzywuzzy.process import extractOne
from telethon import utils
# from telethon import Button
from telethon.tl.custom import Button

from mills import BOT_PIC, client
from mills.decorators import bot_cmd


@bot_cmd(pattern="buy$")
async def _(m):
    text = f"""

┌──────────────────────────┐
    • Premium Plans •

◦ 20$ - Get access to all gates for 28 days.
◦ 30$ - Get access to all gates. for 70 days
◦ 70$ - Get access to all gates. for 200 days

○ Payment methods: Crypto, Bank Transfer, Airtm (No Paypal)

└──────────────────────────┘
"""
    buttons = [
        Button.url('Buy Now', 'https://t.me/TheVenomXD'),
        Button.url('Support', 'https://t.me/Suzune_Support'),
    ]
    await m.reply(text,buttons= buttons, file = BOT_PIC)
