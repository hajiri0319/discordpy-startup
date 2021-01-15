import random
import discord
import os

client = discord.Client()
chID = '772312079590883368'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_member_join(member):
    str = f'{member.mention}さん、いらっしゃいませ～！'
    msg = await client.get_channel(chID).send(str)
    

token = os.environ['DISCORD_BOT_TOKEN']
