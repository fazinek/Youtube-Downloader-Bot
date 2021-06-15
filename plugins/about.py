from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["about"]))
async def start(client, message):

    about = """
- **Bot :** `Rename Bot`
- **Creator :** [Fayas](https://telegram.me/TheFayas)
- **Channel :** [Fayas Noushad](https://telegram.me/FayasNoushad)
- **Credits :** `Everyone in this journey`
- **Source :** [Click here](https://github.com/FayasNoushad/Rename-Bot)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""
await message.reply_text(helptxt)
