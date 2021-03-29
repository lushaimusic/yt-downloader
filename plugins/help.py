from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Send Me Youtube Link To Be Uploaded To Telegram Powered by @bot_beast"
    await message.reply_text(helptxt)
