from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel ⭕️", url="https://t.me/EKBOTZ_UPDATE")],
        [InlineKeyboardButton(
            "Support 🔰", url="https://t.me/ekbotz_support")]])
    welcomed = f"Hey <b>{message.from_user.mention}</b>\nI am YouTube dl bot.**I Can Download YouTube Videos By Link, Send Me A Link To See That Magic.**\n**Hit /help for get an idea.\n\n**Join @EKBOTZ_UPDATE**"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
