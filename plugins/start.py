from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("owner", url="https://t.me/bot_beast")]


    ])
    welcomed = f"Hi! <b>{message.from_user.first_name}</b>\n/help Yo, I am a Powefull Youtube Download Bot 🤓! \n Send Me Youtube Link, So I Can Upload It To Telegram As File/Video!"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
