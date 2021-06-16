from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def help(client, message):
    helptxt = f"Are You Confused With Me 🤣. \nJust Follow Up Below Instructions 😉.\n\n**➲ Send Me A YouTube Video Link\n➲ Wait A Bit For Analysis Your Link \n➲ Select Any Quality Button \n➲ Then Select Upload Mode \n➲ Wait Few Seconds...I Will Upload It To Telegram.**\n\n\nJoin @EKBOTZ_UPDATE FOR KNOW MORE."
    helpbtn = InlineKeyboardMarkup([[InlineKeyboardButton("Channel ⭕️", url ="https://t.me/EKBOTZ_UPDATE")]])
    await message.reply_text(helptxt, reply_markup = helpbtn)
