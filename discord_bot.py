import discord
from discord.ext import commands
import time
import json
import os  

if not os.path.isfile('config.json'):
    exit 

f = open('config.json')
data = json.load(f)
TOKEN = data['token']
servers = data['servers']
message = data['message']
for i in range(len(servers)):
    servers[i] = int(servers[i])

bot = discord.Client(token=TOKEN)

@bot.event
async def on_guild_channel_create(channel):
    if channel.guild.id in servers:
        print(channel, "had just been created")
        await channel.send(message)
bot.run(TOKEN)