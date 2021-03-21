import discord
import os 
from keep_alive import keep_alive

client = discord.Client()

@client.event 

async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  if message.author == client.user:
    return 

  msg = message.content

  if msg.startswith('.append'):
    #msg.split('.append', 1)[1]
    await message.channel.send('```> adicionando elemento na lista```')



keep_alive()
client.run(os.getenv('token'))
  
