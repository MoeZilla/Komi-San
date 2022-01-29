from nksama import bot
import os
from nksama.utils.sendlog import send_log
from pyrogram import filters

@bot.on_message(filters.command('rename'))
def rename(_,message):
  try:
    filename = message.text.replace(message.text.split(" ")[0] , "")

  except Exception as e:
    send_log(e)

  x = message.reply_text("Downloading.....")

  if reply := message.reply_to_message:
    path = reply.download(file_name=filename)
    x.edit("Uploading.....")
    message.reply_document(path)
    os.remove(path)
