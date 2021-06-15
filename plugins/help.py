from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def help(client, message):
    helptxt = f"Are You Confused With Me 🤣. \nJust Follow Up Below Instructions 😉.\n\n**Send Me A YouTube Video Link\nWait Bit For Analysis Your Link \nSelect Any Quality Button \nThen Select Upload Mode \nWait Few Seconds...I Will Upload It To Telegram.**"
    helpbtn = InlineKeyboardMarkup([[InlineKeyboardButton("Cahnnel", url ="https://t.me/EKBOTZ_UPDATE")]])
    await message.reply_text(helptxt), reply_markup = helpbtn
