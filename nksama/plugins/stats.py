from pyrogram import filters , Client
from nksama import bot
from pymongo import MongoClient 
from nksama.db import MONGO_URL as db_url

users_db = MongoClient(db_url)['users']
col = users_db['USER']

grps = users_db['GROUPS']


@bot.on_message(filters.command("stats"))
def stats(_,message):
  users = col.find({})
  mfs = [x['user_id'] for x in users]
  total = len(mfs)

  grp = grps.find({})
  grps_ = [x['chat_id'] for x in grp]
  total_ = len(grps_)

  bot.send_message(message.chat.id , f"Total Users: {total}\nTotal Groups: {total_}")
  


