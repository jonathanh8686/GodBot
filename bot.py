from discord.ext import commands
import discord
import time
import swear
from threading import Timer


client = discord.Client()

offenseCount = {}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.author)

    if(swear.isSwear(message.content)):
        if(message.author not in offenseCount):
            offenseCount[message.author] = 0
        offenseCount[message.author] += 1

        if(offenseCount[message.author] == 1):
            await message.channel.send("**First Offense.** WARNING")
        elif(offenseCount[message.author] >= 2):
            await message.channel.send("**Second Offense.** KICKED")
            await message.guild.kick(message.guild.members[3])

client.run("NjE1MDY3ODkyODQ4Nzg3NDU5.XWIozg.AtR6uSGEcmDiNHHYd1pw-hoM2as")
