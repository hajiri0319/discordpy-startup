import random
import discord

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
    

token = 'Nzk5NTI0OTIwNzg2NDE5NzMz.YAE1mw.xY4cx7-JyvBN42huK7TUNtEwn5E'

client.run(token)
