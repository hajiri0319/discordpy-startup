import random
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if client.user != message.author:
        dice = random.randint(1,5)
        if dice == 1:
            if '(´◉◞౪◟◉)' in message.content:
                m = "こっち見んな()"
                await message.channel.send(m)
            if 'ムワア' in message.content:
                m = "ムワアアアアアアア！！！！"
                await message.channel.send(m)
            if  'ンアー' in message.content:
                m = "ンアーッ!(≧Д≦)"
                await message.channel.send(m)
            if 'ムシャムシャ' in message.content:
                m = "ムワアアアアアアア！！！！"
                await message.channel.send(m)
            if 'ﾑｼｬﾑｼｬ' in message.content:
                m = "ムワアアアアアアア！！！！"
                await message.channel.send(m)
            if 'シモビト' in message.content:
                m = "ムワアアアアアアア！！！！"
                await message.channel.send(m)
        if 'dice' in message.content:
                    await message.channel.send(dice)
        if message.content == "おみくじ":
            num = random.randint(0,60)
            if num < 2:
                m = "おみくじ結果→大吉"
                await message.channel.send(m)
            elif 2 <= num < 10:
                m = "おみくじ結果→中吉"
                await message.channel.send(m)
            elif 10 <= num < 20:
                m = "おみくじ結果→小吉"
                await message.channel.send(m)
            elif 20 <= num < 40:
                m = "おみくじ結果→吉"
                await message.channel.send(m)
            elif 40 <= num < 50:
                m = "おみくじ結果→末吉"
                await message.channel.send(m)
            elif 50 <= num < 55:
                m = "おみくじ結果→凶"
                await message.channel.send(m)
            elif 55 <= num < 58:
                m = "おみくじ結果→中凶"
                await message.channel.send(m)
            else:
                m = "おみくじ結果→大凶"
                await message.channel.send(m)      


token = os.environ['DISCORD_BOT_TOKEN']
