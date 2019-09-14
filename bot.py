from discord.ext import commands
import reply
import json
import discord
from datetime import datetime
from time import gmtime, strftime
from threading import Timer

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def ping(ctx):
    await ctx.send("pong!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await reply.checkIm(message)
    await reply.checkWalter(message)

    # record the messages sent
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\t" + str(message.author) + ":\t" + message.content)

    await bot.process_commands(message)

configData = json.loads(open("config.json", "r").read())
bot.run(configData["bot_token"])
